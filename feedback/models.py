from django.contrib.auth import get_user_model
from django.db import models

from transport.models import Review


User = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="likes")

    def __str__(self):
        return f"{self.user.username} likes {self.review.name}s review"
