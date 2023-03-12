from django import forms
from django.forms import ModelForm

from .models import Comment, Transportation


class CommentForm(forms.ModelForm):
    """ Form for submitting a comment """

    class Meta:
        model = Comment
        fields = ["body",]


class TransportForm(ModelForm):
    """ Form for adding a transportation """

    class Meta:
        model = Transportation
        fields = '__all__'
