from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Post
# Create your views here.


@login_required(login_url='login')
def home(request):
    
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}
    return render(request, 'base/home.html', context)


def loginuser(request):
    context = {'page': 'login'}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print('helllllo11111')
        if user is not None:
            print('helllllo')
            login(request, user)
            return redirect('home')
        else:
            print('no no nono')
    return render(request, 'base/login_register.html', context)


def register(request):
    context = {'page': 'register'}

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'base/login_register.html', context)

        # Check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'base/login_register.html', context)

        # Create user
        user = User.objects.create_user(
            username=username, email=email, password=password1)
        login(request, user)
        messages.success(
            request, f'Welcome {username}, account created successfully!')
        return redirect('home')

    return render(request, 'base/login_register.html', context)


def createPost(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content.strip():
            Post.objects.create(
                author=request.user.student_profile, content=content)
            return redirect('home')

    return render(request, 'base/create_post.html')


def logoutUser(request):
    logout(request)
    return redirect('home')
