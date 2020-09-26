from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from login.models import UserProfile


class SignupForm(UserCreationForm):
    email = forms.EmailField(label='Email Adddress', required=True, )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', )


        
class ProfilePic(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic', ]
        
