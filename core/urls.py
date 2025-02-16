from django.conf.urls.static import static
from django.urls import path

from core import views
from softmall import settings


urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('company/register/', views.register_company, name='register_company'),
    path('group/register/', views.register_group, name='register_group'),
    path('user_role/create_role/', views.create_role, name='register_user_roles'),
    path('user_role/assign_role/', views.assign_role, name='assign_role'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home_view, name='home')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)