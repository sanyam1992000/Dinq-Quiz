from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory, inlineformset_factory
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, status, authentication
from core import serializers
from . import models, forms
from quiz import settings
# Create your views here.

@login_required
def HomeView(request):
    user = request.user
    QuestionFormSet = inlineformset_factory(models.Category, models.Question, exclude=('category',),
                                                  can_delete=True, extra=1)

    if request.method == 'POST':
        categoryform = forms.CategoryForm(request.POST)
        if categoryform.is_valid():
            print(categoryform)
            name = request.POST['name']
            category = models.Category(name=name)
            category.save()

            formset = QuestionFormSet(request.POST, instance=category, prefix='Question', )
            print(request.POST)

            if formset.is_valid():
                for form1 in formset:
                    print(form1)
                    # option1 = form1.cleaned_data['correct-answer']
                    # print(option1)
                    form1.save()

            return redirect('home')

    else:
        formset = QuestionFormSet(prefix='Question')
        categoryform = forms.CategoryForm()

        context = {
            'user': user,
            'form': categoryform,
            'formset': formset,
        }
        return render(request, 'testquiz1.html', context)

@login_required
def LogoutView(request):
    logout(request)
    return redirect('home')


class CategoryAPIViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    permission_classes = (AllowAny,)


class QuestionAPIViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuestionsSerializer
    queryset = models.Question.objects.all()
    permission_classes = (AllowAny,)

