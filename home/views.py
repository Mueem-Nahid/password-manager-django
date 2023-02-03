from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from home.forms import RegistrationForm, LoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

from home.models import UserPassword


# home page
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home_page(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/', request.path))
    return render(request, 'pages/home.html')


# user login
class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'pages/index.html'


# register new user
def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("Account created successfully!")
            form.save()
            return redirect('/')
        else:
            print("Registration failed!")
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'pages/register.html', context)


# logout
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('/')
    logout(request)
    return redirect('/')


# add new password
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_new_password(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/', request.path))
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            application_type = request.POST['application_type']
            if application_type == 'Website':
                website_name = request.POST['website_name']
                website_url = request.POST['website_url']
                print(username, password, application_type, website_name, website_url)
                UserPassword.objects.create(username=username, password=password, application_type=application_type,
                                            website_name=website_name, website_url=website_url, user=request.user)
                messages.success(request, f"New password added for {website_name}")
            elif application_type == 'Desktop application':
                application_name = request.POST['application_name']
                print(username, password, application_type, application_name)
                UserPassword.objects.create(username=username, password=password, application_type=application_type,
                                            application_name=application_name, user=request.user)
                messages.success(request, f"New password added for {application_name}.")
            elif application_type == 'Game':
                game_name = request.POST['game_name']
                game_developer = request.POST['game_developer']
                print(username, password, application_type, game_name, game_developer)
                UserPassword.objects.create(username=username, password=password, application_type=application_type,
                                            game_name=game_name, game_developer=game_developer, user=request.user)
                messages.success(request, f"New password added for {game_name}.")
            return HttpResponseRedirect("/add-password")
        except Exception as error:
            print("Error: ", error)

    return render(request, 'pages/add-password.html')


# all passwords
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def manage_passwords(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/', request.path))
    logged_in_user = request.user
    print("logged_in_user", logged_in_user)
    user_passwords = UserPassword.objects.filter(user=logged_in_user).order_by('-date_created')
    web_app = user_passwords.filter(application_type='Website')
    desktop_app = user_passwords.filter(application_type='Desktop application')
    game = user_passwords.filter(application_type='Game')
    password_obj = {
        'web_app': web_app,
        'desktop_app': desktop_app,
        'game': game
    }
    print(password_obj)
    if not user_passwords:
        return render(request, 'pages/manage-passwords.html',
                      {'no_password': "No password available. Please add password."})
    return render(request, 'pages/manage-passwords.html', {'all_passwords': password_obj})
