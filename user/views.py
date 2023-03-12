from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from helpers.decorators_own import authenticated_user

from .forms import RegisterForm, UserEditForm
from .models import Profile

User = get_user_model()


class SuccessUrlMixin:
    def get_success_url(self):
        return reverse("transport:index")


@method_decorator(authenticated_user, name="dispatch")
class RegisterView(SuccessUrlMixin, CreateView):
    """ Registers new user """

    model = User
    form_class = RegisterForm
    template_name = "user/register.html"

    def get_success_url(self):
        return reverse("login")


@method_decorator(authenticated_user, name="dispatch")
class LoginUser(SuccessUrlMixin, LoginView):
    """ Logs user in """

    template_name = "user/login.html"


class LogoutUser(LoginRequiredMixin, LogoutView):
    """ Logs user out """

    next_page = "login"


class EditView(LoginRequiredMixin, SuccessUrlMixin, UpdateView):
    """ View for editing user profile """

    model = User
    template_name = "user/edit.html"
    form_class = UserEditForm

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        valid_form = super().form_valid(form)
        messages.success(self.request, "Your profile has been successfully updated.")
        return valid_form


class ProfileView(LoginRequiredMixin, ListView):
    """ View for users to view thier profile. Also calculates the times for
        their submitted reviews and shows them on their profile along with their reviews """

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


class DeleteUser(DeleteView):
    """ View for Deleting user profile """

    model = User
    template_name = 'user/delete.html'

    def get(self, request):
        return render(self.request, self.template_name)

    def post(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        user = profile.user
        user.delete()
        return redirect("transport:index")
