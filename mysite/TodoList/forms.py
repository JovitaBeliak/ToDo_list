from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, TaskReview, Task
from django import forms


class TaskReviewForm(forms.ModelForm):
    class Meta:
        model = TaskReview
        fields = ['content']


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'photo']

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'doer', 'due_date']
        widgets = {'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})}


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'doer', 'due_date', 'status']
        widgets = {'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})}