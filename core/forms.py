from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        exclude = ('category',)

