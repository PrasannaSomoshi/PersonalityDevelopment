from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Chart
import django.forms.widgets


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class ChartForm(forms.ModelForm):
    class Meta:
        model = Chart
        fields = '__all__'
        widgets = {'date': DateInput()}
