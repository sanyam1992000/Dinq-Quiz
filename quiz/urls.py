from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views as coreviews
from allauth.account import views as allauthviews

router = DefaultRouter()
router.register('categories', coreviews.CategoryAPIViewSet, basename='category')
router.register('questions', coreviews.QuestionAPIViewSet, basename='question')


urlpatterns = [
    path('', coreviews.HomeView, name='home'),

    path('accounts/logout/', coreviews.LogoutView, name='logout_url'),
    # path('accounts/login/', allauthviews.LoginView, name='account_login'),
    path('accounts/', include('allauth.urls')),

    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name='api'),
    path('api-auth/', include('rest_framework.urls')),

]
