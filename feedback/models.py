from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from transport.models import Review


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="likes")

    def __str__(self):
        return f"{self.user.username} likes {self.review.name}s review"
