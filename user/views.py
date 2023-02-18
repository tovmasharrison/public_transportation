from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, UpdateView, ListView, DeleteView)
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import RegisterForm, UserEditForm
from .models import Profile


User = get_user_model()

class SuccessUrlMixin:
    def get_success_url(self):
        return reverse("transport:index")


class RegisterView(SuccessUrlMixin, CreateView):
    model = User
    form_class = RegisterForm
    template_name = "user/register.html"

    def get_success_url(self):
        return reverse("login")


class LoginUser(SuccessUrlMixin, LoginView):
    template_name = "user/login.html"


class LogoutUser(LoginRequiredMixin, LogoutView):
    next_page = "login"


class EditView(LoginRequiredMixin, SuccessUrlMixin, UpdateView):
    model = User
    template_name = "user/edit.html"
    form_class = UserEditForm

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        valid_form = super().form_valid(form)
        messages.success(self.request, "Your profile has been successfully updated.")
        return valid_form

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["profile_form"] = ProfileEditForm(self.request.POST, self.request.FILES, instance=self.request.user)
    #     return context

    # def form_valid(self, form):
    #     valid_form = super().form_valid(form)
    #     profile_form = ProfileEditForm(self.request.POST, self.request.FILES, instance=self.request.user)
    #     if profile_form.is_valid():
    #         profile_form.save()
    #         messages.success(self.request, "Changes have been saved")
    #         return valid_form



class ProfileView(LoginRequiredMixin, ListView):
    model = User
    template_name = "user/profile.html"
    context_object_name = "reviews"
    paginate_by = 3

    def get_queryset(self):
        user = self.request.user
        reviews = user.review.all().order_by("-created_at")

        now = timezone.now()
        for review in reviews:
            review.created_at = timezone.localtime(review.created_at)

            if (now - review.created_at).days == 0:
                review.created_relative_date = "Today"
            elif (now - review.created_at).days == 1:
                review.created_relative_date = "Yesterday"
            else:
                review.created_relative_date = review.created_at.strftime("%B %d, %Y")

            review.created_relative_time = review.created_at.strftime("%H:%M")

        return reviews


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profilee"] = Profile.objects.all()
        return context
# class ProfileView(LoginRequiredMixin, ListView):
#     model = User
#     template_name = "user/profile.html"
#     context_object_name = "reviews"
#     paginate_by = 3

#     def get_queryset(self):
#         user = self.request.user
#         reviews = user.review.all().order_by("-created_at")

#         now = timezone.now()
#         for review in reviews:
#             if (now - review.created_at).days == 0:
#                 review.created_relative_date = "Today"
#             elif (now - review.created_at).days == 1:
#                 review.created_relative_date = "Yesterday"
#             else:
#                 review.created_relative_date = review.created_at.strftime("%B %d, %Y")

#             review.created_relative_time = review.created_at.strftime("%H:%M")

#         return reviews


    # def get_queryset(self):
    #     user = self.request.user
    #     return user.review.all().order_by("-created_at")

    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['reviews'] = [self.format_review_date(review) for review in context['reviews']]
    #     return context

    
    # def format_review_date(self, review):
    #     today = datetime.now().date()
    #     created_at = datetime.combine(review.created_at.date(), review.created_at.time())
    #     if (today - created_at.date()).days == 0:
    #         return "Today"
    #     elif (today - created_at.date()).days == 1:
    #         return "Yesterday"
    #     else:
    #         return created_at.strftime("%B %d, %Y")

        # now = datetime.now()
        # review_date = review.created_at.date()
        # if (now - review_date).days == 0:
        #     review.created_at_formatted = "today"
        # elif (now - review_date).days == 1:
        #     review.created_at_formatted = "yesterday"
        # else:
        #     review.created_at_formatted = review_date.strftime("%b %d, %Y")
        # return review



   
    # def get_queryset(self):
    #     print(self.kwargs)
    #     user = get_object_or_404(User, username=self.kwargs.get("username"))
    #     return user.review.all().order_by("-created_at")[:5]
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["user"] = get_object_or_404(User, username=self.kwargs.get("username"))
    #     return context


class DeleteUser(DeleteView):
    model = User
    template_name = 'user/delete.html'
    # success_url = reverse_lazy("login")

    def get(self, request):
        return render(self.request, self.template_name)

    def post(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        user = profile.user
        user.delete()
        return redirect("transport:index")

