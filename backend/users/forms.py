# from django import forms
# # from .models import Profile
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
        
# class UserLoginForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = ['email', 'password']


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email']

# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Community, CustomUser

class CustomUserCreationForm(UserCreationForm):
    community = forms.ModelChoiceField(queryset=Community.objects.all(), required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'community', 'password1', 'password2']

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data['password'])  # Hash password before saving
    #     if commit:
    #         user.save()
    #         profile = Profile.objects.get(user=user)
    #         profile.location = self.cleaned_data['location']
    #         profile.community, _ = Community.objects.get_or_create(name=profile.location)
    #         profile.save()
    #     return user

