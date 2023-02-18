from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from stop.models import BusStop


class Transportation(models.Model):
    class Type(models.TextChoices):
        BUS = "bus", "Bus"
        MICROBUS = "microbus", "Microbus"
        TROLLEYBUS = "trolleybus", "Trolleybus"
        METRO = "metro", "Metro"
    number = models.IntegerField()
    type = models.CharField(max_length=30, choices=Type.choices)
    route = models.TextField()
    stop = models.ManyToManyField(BusStop, related_name = 'transports')
    # amortization

    class Meta:
        ordering = ["number"]
        indexes = [
            models.Index(fields=["-number"])
        ]
    
    def __str__(self):
        return f"N{self.number} {self.type}"

    
    def get_absolute_url(self):
        return reverse('transportation:transportation', kwargs={'t_type' : self.type})

    #Amortization
    # def calculate_wear_and_tear(self):
    #     age_in_months = "The difference between the date of today and created_at"

    #     wear_and_tear = self.number_of_miles_driven_per_day * age_in_months

    #     return wear_and_tear

    # def get_absolute_url(self):
    #     return reverse("transport:transport_details")


class Review(models.Model):
    review = models.TextField(blank=True, null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    transport = models.ForeignKey(Transportation, on_delete=models.CASCADE, related_name="reviews")
    rate = models.IntegerField(validators=[
                                            MinValueValidator(0, message="Minimum value must be 0."),
                                            MaxValueValidator(5, message="Maximum value must be 5.")
                                            ])
    
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.review


class BusStop(models.Model):
    # location = 
    transport = models.ForeignKey(Transportation, on_delete=models.PROTECT, related_name = "stops")


class Comment(models.Model):
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
        return reverse("feedback/comment.html")




