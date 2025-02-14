from django.conf.urls.static import static
from django.urls import path

from . import views
from softmall import settings

urlpatterns = [
    path('register/', views.register, name='register'),
    path('company/register/', views.register_company, name='register_company'),
    path('group/register/', views.register_group, name='register_group'),
    path('user_roles/register/', views.register_user_roles, name='register_user_roles'),
    path('login/', views.login_view, name='login'),
    path('', views.home_view, name='home')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)