from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Grievance, Message

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['type', 'description', 'department', 'severity']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']
