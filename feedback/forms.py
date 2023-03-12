from django import forms

from transport.models import Review


class ReviewForm(forms.ModelForm):
    """ Form for submitting a review """

    class Meta:
        model = Review
        fields = ["transport", "rate", "review"]
