from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "email", 
            "username", "password1", "password2"
        ]

    def clean_email(self):
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Email address already exists")
        return data
        

class UserEditForm(forms.ModelForm):
    date_of_birth = forms.CharField(label="Date of Birth", widget=forms.DateInput, required=False)
    image = forms.ImageField(label="Profile Image", required=False)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        labels = [
            "First Name", "Last Name", "Email Address", "Username"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.profile:
            self.fields["date_of_birth"].initial = self.instance.profile.date_of_birth
            self.fields["image"].initial = self.instance.profile.image

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        profile, created = Profile.objects.get_or_create(user=instance)
        if profile.date_of_birth:
            profile.date_of_birth = self.cleaned_data["date_of_birth"]
        profile.image = self.cleaned_data["image"]
        profile.save()
        return instance
        

# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ["date_of_birth", "image"]
#         labels = ["Date of Birth", "Image"]

#     def clean_email(self):
#         data = self.cleaned_data["email"]
#         qs = User.objects.exclude(id=self.instance.id).filter(email=data)
#         if qs.exists():
#             raise forms.ValidationError("Email address already exists")
#         return data
