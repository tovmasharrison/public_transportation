from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import Profile


User = get_user_model()


class RegisterForm(UserCreationForm):
    """ Form for user registration """

    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "email",
            "username", "password1", "password2"
        ]

    def clean_email(self):
        """ Checks if email is unique """

        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Email address already exists")
        return data


class UserEditForm(forms.ModelForm):
    """ Form for editing user information """

    date_of_birth = forms.CharField(label="Date of Birth", widget=forms.DateInput, required=False)
    image = forms.ImageField(label="Profile Image", required=False)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        labels = [
            "First Name", "Last Name", "Email Address", "Username"
        ]

    def __init__(self, *args, **kwargs):
        """ Assignes profile fields to the user fields """

        super().__init__(*args, **kwargs)
        if self.instance and self.instance.profile:
            self.fields["date_of_birth"].initial = self.instance.profile.date_of_birth
            self.fields["image"].initial = self.instance.profile.image

    def save(self, commit=True):
        """ Saves the updated information """

        instance = super().save(commit=False)
        if commit:
            instance.save()
        profile, created = Profile.objects.get_or_create(user=instance)
        if profile.date_of_birth:
            profile.date_of_birth = self.cleaned_data["date_of_birth"]
        profile.image = self.cleaned_data["image"]
        profile.save()
        return instance
