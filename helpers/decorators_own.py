from functools import wraps

from django.shortcuts import redirect

from transport.models import Review


def action_superuser(func: callable):
    """ Checks if the user is a superuser """

    @wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if request.user.is_superuser:
            return func(*args, **kwargs)
        return redirect("transportation:index")
    return wrapper


def is_review_owner(view_func):
    """ Checks if the user is the owner of the review and allows to proceed forward"""

    def wrapper(request, *args, **kwargs):
        review = Review.objects.get(pk=kwargs['pk'])
        if review.name != request.user:
            return redirect("feedback:feedbacks")
        return view_func(request, *args, **kwargs)
    return wrapper


def authenticated_user(view_func):
    """ Checks if user is authenticated redirects to home page """

    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("transportation:index")
        return view_func(request, *args, **kwargs)
    return wrapper
