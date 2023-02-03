from django.urls import path

from . import views

urlpatterns = [
    # user account
    path('', views.UserLoginView.as_view(), name='index'),
    path('register/', views.register_page, name='register-page'),
    path('home/', views.home_page, name='home'),
    path('logout/', views.logout_view, name="logout"),

    #  user passwords
    path('add-password/', views.add_new_password, name="add-password"),
    path('all-passwords/', views.manage_passwords, name="manage-passwords")
]
