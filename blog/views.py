from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# POSTS = [
#     {
#         'author':'Bot 1',
#         'title':'Post 1',
#         'date_posted':'Mai 1st 1994',
#         'content': 'First post content',
#     },
#     {
#         'author':'Bot 2',
#         'title':'Post 2',
#         'date_posted':'December 31 1999',
#         'content': 'Second post content',
#     },
# ]

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "Django Blog About"})
