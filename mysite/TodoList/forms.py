from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, TaskReview
from django import forms


class TaskReviewForm(forms.ModelForm):
    class Meta:
        model = TaskReview
        fields = ['content']


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

