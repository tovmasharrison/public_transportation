from django import forms

from transport.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["transport", "rate", "review"]

    # def save(self, commit: bool = True):
    #     return super().save(commit)
