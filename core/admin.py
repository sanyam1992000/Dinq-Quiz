from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
admin.site.site_header = 'Dlinq'

# Register your models here.


class InlineQuestions(admin.StackedInline):
    model = models.Question


class CategoryAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    inlines = [InlineQuestions]


class QuestionAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    list_display = ('ques', 'description', 'correct_answer', 'category')
    list_display_links = ('ques', 'description', 'correct_answer', 'category')
    list_filter = ('category',)
    search_fields = ('ques', 'description', 'category', 'correct_answer')
    list_max_show_all = 100


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Question, QuestionAdmin)
