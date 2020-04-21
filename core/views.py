from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, status, authentication
from core import serializers
from . import models

# Create your views here.

class CategoryAPIViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    permission_classes = (AllowAny,)


class QuestionAPIViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuestionsSerializer
    queryset = models.Question.objects.all()
    permission_classes = (AllowAny,)

