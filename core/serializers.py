from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class QuestionsSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="question-detail")
    # category = CategorySerializer(many=False)

    class Meta:
        model = models.Question
        fields = "__all__"


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="category-detail")
    questions = QuestionsSerializer(many=True)

    class Meta:
        model = models.Category
        fields = ["url", "name", 'questions']