from django.shortcuts import render, HttpResponse

# Create your views here.


def blogHome(request):
    return render(request, 'blog/blog.html')


def blogPost(request, slug):
    return render(request, 'blog/post.html')
