from django.shortcuts import render


posts = [
    {
        'author': 'Salaza Slytherin',
        'title': 'Blog Post 1',
        'content': 'FIrst post contene',
        'date_posted': 'August 27, 2018'
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
