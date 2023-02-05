from django.urls import path

from . import views
from .views import generate_password

urlpatterns = [
    # user account
    # path('', views.UserLoginView.as_view(), name='index'),
    path('', views.user_login_view, name='index'),
    path('register/', views.register_page, name='register-page'),
    path('home/', views.home_page, name='home'),
    path('logout/', views.logout_view, name="logout"),

    #  user passwords
    path('add-password/', views.add_new_password, name="add-password"),
    path('manage-passwords/', views.manage_passwords, name="manage-passwords"),
    path('edit-password/<str:pk>/', views.edit_password, name="edit-password"),
    path('search/', views.search, name='search'),

    # path for generating random password
    path('generate-password/', generate_password, name='generate-password'),
]
