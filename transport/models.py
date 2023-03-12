from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg
from django.urls import reverse


User = get_user_model()


class Transportation(models.Model):
    """ Model for Transportation """

    class Type(models.TextChoices):
        """ Class for displaying the choices for transportation types """

        BUS = "bus", "Bus"
        MICROBUS = "microbus", "Microbus"
        TROLLEYBUS = "trolleybus", "Trolleybus"
        METRO = "metro", "Metro"
    number = models.IntegerField()
    type = models.CharField(max_length=120, choices=Type.choices)
    route = models.TextField()

    class Meta:
        ordering = ["number"]
        indexes = [
            models.Index(fields=["-route"])
        ]

    def __str__(self):
        return f"N{self.number} {self.type}"

    def get_absolute_url(self):
        return reverse('transportation:transportation', kwargs={'t_type': self.type})

    def average_rating(self):
        """ Returns the average rating for the transportation """

        return Review.objects.filter(transport=self).aggregate(Avg("rate"))["rate__avg"] or 0


class Review(models.Model):
    """ Model for Review """

    class Rate(models.IntegerChoices):
        """ Choices for the rating """

        ONE = 1, "1"
        TWO = 2, "2"
        THREE = 3, "3"
        FOUR = 4, "4"
        FIVE = 5, "5"

    review = models.TextField(blank=True, null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    transport = models.ForeignKey(Transportation, on_delete=models.CASCADE, related_name="reviews")
    rate = models.IntegerField(choices=Rate.choices)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.review


class Comment(models.Model):
    """ Model for comment """

    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created"]
        indexes = [
            models.Index(fields=["created"]),
        ]

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("feedback:comment", kwargs={"pk": self.pk})
