from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, DeleteView, ListView

from helpers.decorators_own import is_review_owner
from transport.forms import CommentForm
from transport.models import Review, Transportation

from .forms import ReviewForm
from .models import Like


class IndexView(LoginRequiredMixin, CreateView):
    """ Home page for Feedback """

    template_name = 'feedback/index.html'
    model = Review
    form_class = ReviewForm
    success_url = "."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transportation'] = Transportation.objects.order_by("type", "number")
        context['latest_reviews'] = Review.objects.order_by("-created_at")[:5]
        return context

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class AllReviews(LoginRequiredMixin, ListView):
    """ Page to see all the reviews and likes """

    model = Review
    template_name = 'feedback/all_reviews.html'
    context_object_name = "reviews"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user_review_likes = Like.objects.filter(user=self.request.user, review__in=context['reviews'])
            context['user_review_likes'] = user_review_likes.values_list('review_id', flat=True)
        return context


@method_decorator(is_review_owner, name="dispatch")
class DeleteReview(LoginRequiredMixin, DeleteView):
    """ Class based view for deleting a review """

    model = Review
    success_url = reverse_lazy("feedback:all_reviews")
    template_name = "feedback/delete_review.html"


@require_POST
@login_required
def like_review(request, review_id):
    """ Function for allowing users to like a review """

    review = get_object_or_404(Review, pk=review_id)

    try:
        like = Like.objects.get(user=request.user, review=review)
        like.delete()
        liked = False
    except Like.DoesNotExist:
        like = Like.objects.create(user=request.user, review=review)
        liked = True

    likes_count = review.likes.count()
    data = {
        'liked': liked,
        'likes_count': likes_count,
    }
    return JsonResponse(data)


def post_comment(request, pk):
    """ Function for allowing users to comment on a review """

    review = get_object_or_404(Review, pk=pk)
    comments = review.comments.order_by("-created")
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.review = review
        comment.name = request.user
        comment.save()
        return redirect(".")
    return render(request, "feedback/comment.html", {
        "review": review, "form": form, "comment": comment, "comments": comments
    })
