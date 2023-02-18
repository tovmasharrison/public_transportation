from django import forms
from django.forms import ModelForm
from .models import Comment, Review, Transportation


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body",]
        

class TransportForm(ModelForm):
    
    class Meta:
        model = Transportation
        fields = '__all__'
        # exclude = ['type']
        