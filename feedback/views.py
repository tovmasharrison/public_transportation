from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, TemplateView, ListView
from django.views.generic.edit import FormMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from .forms import ReviewForm
from .models import Like
from transport.models import Review, Transportation, Comment
from transport.forms import CommentForm


class IndexView(LoginRequiredMixin, CreateView):
    template_name = 'feedback/index.html'
    model = Review
    form_class = ReviewForm
    success_url = "."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transportation'] = Transportation.objects.all()
        context['latest_reviews'] = Review.objects.order_by("-created_at")[:5]
        # print(context['latest_reviews'])
        return context

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


# class CommentView(TemplateView):
#     template_name = "feedback/comment.html"




class AllReviews(LoginRequiredMixin, ListView):
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



@require_POST
@login_required
def like_review(request, review_id):
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
    review = get_object_or_404(Review, pk=pk)
    comments = review.comments.order_by("-created")
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.review = review
        comment.name = request.user
        comment.save()
    return render(request, "feedback/comment.html", {
        "review": review, "form": form, "comment": comment, "comments": comments
    })

# class CommentSubmit(LoginRequiredMixin, CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = "feedback/comment.html"
#     success_url = "."
#     pk_url_kwarg = "pk"

#     def form_valid(self, form):
#         review = get_object_or_404(Review, pk=self.kwargs['pk'])
#         form.instance.review = review
#         form.instance.name = self.request.user
#         return super().form_valid(form)

    
