from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post


# Create your views here.


def home(request):
    allPosts = Post.objects.all()
    allPosts = allPosts[0:3]
    context = {'allPosts': allPosts}
    return render(request, 'home/index.html', context)


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if len(name) < 3 or len(email) < 3 or len(subject) < 2 or len(message) < 3:
            messages.error(request, 'Please fill the form correctly!')
            return redirect('/')
        else:
            newContact = Contact(name=name, email=email,
                                 subject=subject, message=message)
            newContact.save()
            messages.success(request, 'Form has been successfully submitted!')
            return redirect('/')

    return render(request, 'home/contact.html')


def search(request):
    query = request.GET.get('query')
    postTitle = Post.objects.filter(title__icontains=query)
    postContent = Post.objects.filter(content__icontains=query)
    allPosts = postTitle.union(postContent)
    context = {"allPosts": allPosts, 'query': query}
    return render(request, 'home/search.html', context)


def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST.get('username')
        loginpassword = request.POST.get('password')
        print(loginusername)
        print(loginpassword)

        user = authenticate(request, username=loginusername,
                            password=loginpassword)
        print(user)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are successfully logged in!')
            return redirect('/')

        else:
            messages.error(request, 'Invalid Credentials, Plase try again!')
            return redirect('/')
    return render(request, 'home/login.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if len(username) < 3:
            messages.error(
                request, "Username must have atleast 3 chars, Please try again!")
            return redirect('/')

        if pass1 != pass2:
            messages.error(request, "Password do not match, Please try again!")
            return redirect('/')

        user = User.objects.create_user(username, email, pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, "You account has been created successully!")
        return redirect('/')

    return render(request, 'home/signup.html')


def handleLogout(request):
    logout(request)
    return redirect('/')
