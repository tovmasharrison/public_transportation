from django.urls import path

from . import views

app_name = "feedback"
urlpatterns = [
    path("feedbacks/", views.IndexView.as_view(), name="feedbacks"),
    path("feedback/all_reviews/", views.AllReviews.as_view(), name="all_reviews"),
    path('feedback/<int:review_id>/like/', views.like_review, name='like_review'),
    path("<int:pk>/comment/", views.post_comment, name="comment"),
    path("reviews/<int:pk>/delete/", views.DeleteReview.as_view(), name="delete_review")
]
