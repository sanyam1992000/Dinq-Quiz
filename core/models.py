from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def child_list(self):
        return Question.objects.filter(category=self)

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    ques = models.TextField()
    description = models.TextField(blank=True, null=True)
    option_1 = models.CharField(max_length=10000,)
    option_2 = models.CharField(max_length=10000, blank=True, null=True)
    option_3 = models.CharField(max_length=10000, blank=True, null=True)
    option_4 = models.CharField(max_length=10000, blank=True, null=True)
    correct_answer = models.CharField(max_length=10000, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Questions'
        ordering = ['category__name']

    def __str__(self):
        return str(self.ques)


