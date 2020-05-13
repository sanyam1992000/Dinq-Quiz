from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory, inlineformset_factory
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, status, authentication
from core import serializers
from . import models, forms
from quiz import settings
# Create your views here.

@login_required
def HomeView(request):
    id = request.user.id
    categories = models.Category.objects.filter(user__id=id)
    user = User.objects.get(id=id)
    context = {
        'categories': categories,
        'user': user,
    }
    return render(request, 'home.html', context)

@login_required
def EmptyFormView(request):
    username = request.user.username
    user = User.objects.get(username=username)
    QuestionFormSet = inlineformset_factory(models.Category, models.Question, exclude=('category',),
                                                  can_delete=True, extra=1)

    if request.method == 'POST':
        categoryform = forms.CategoryForm(request.POST)

        if categoryform.is_valid():
            name = request.POST['name']
            dedicated = request.POST.get('dedicated', '') == 'on'
            slug = name.replace(' ', '-')
            category = models.Category(name=name, dedicated=dedicated, user=user, slug=slug)
            category.save()

            formset = QuestionFormSet(request.POST, instance=category, prefix='Question')
            print(request.POST)

            if formset.is_valid():
                for form1 in formset:
                    form1.save()

            return redirect('home')
        else:
            return HttpResponse("invalid", status=500)
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
def EditFormView(request, slug):
    user = request.user
    quiz = models.Category.objects.get(slug=slug, user=user)
    QuestionFormSet = inlineformset_factory(models.Category, models.Question, exclude=('category',),
                                                  can_delete=True, extra=1)

    if request.method == 'POST':
        categoryform = forms.CategoryForm(request.POST, instance=quiz)
        formset = QuestionFormSet(request.POST, prefix='Question', instance=quiz)
        if categoryform.is_valid():
            categoryform.save()

        print("########################################")
        print(request.POST)
        print(formset.errors)
        if formset.is_valid():
            formset.save()
        # for form1 in formset:
        #     # option1 = form1.cleaned_data['correct-answer']
        #     print(form1.errors)
        #     form1.save()

        return redirect('home')

    else:
        formset = QuestionFormSet(prefix='Question', instance=quiz)
        categoryform = forms.CategoryForm(instance=quiz)

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

