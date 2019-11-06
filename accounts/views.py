from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth

from pick_up_game_app.models import Player, Event



# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username_form = request.POST['username']
        email_form = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # validate that passwords match
        if password == password2:
            # check if username exists
            if User.objects.filter(username=username_form).exists():
                context = {'error': 'Username is already taken.'}
                return render(request, 'register.html', context)
            else:
                if User.objects.filter(email=email_form).exists():
                    context = {'error': 'That email already exists.'}
                    return render(request, 'register.html', context)
                else:
                    # if everything is ok, create account
                    user = User.objects.create_user(
                        username=username_form,
                        email=email_form,
                        password=password,
                        first_name=first_name,
                        last_name=last_name)
                    user.save()
                    return redirect('profile.html')
        else:
            context = {'error': 'Passwords do not match.'}
            return render(request, 'register.html', context)
    else:
        # if not post, back on register form
        return render(request, 'register.html')


# login

def login(request):
    if request.method == 'POST':
        username_form = request.POST['username']
        password_form = request.POST['password']
        # authenticate user
        user = auth.authenticate(
            username=username_form,
            password=password_form)

        if user is not None:
            # login and create session
            auth.login(request, user)
            return redirect('profile.html')
        else:
            context = {'error': 'Invalid Credentials'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')


# logout

def logout(request):
    auth.logout(request)
    # ANCHOR Change html name
    return redirect('home.html')


# def profile(request):
#     players = Player.objects.filter(user=request.user)
#     events = Event.objects.filter(player)
#     context = {'players': players}
#     return render(request, 'profile.html', context)
    