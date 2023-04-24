from django import forms
from .models import Reviews
from django.forms import Textarea, TextInput, EmailInput


class ReviewForm(forms.ModelForm):
    '''''Форма для отзыва'''


    class Meta:
        model = Reviews
        fields = ("name", "email", "text")



   