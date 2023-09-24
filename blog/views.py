from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts' : posts,
        }
    )


def single_post_page(reqeust, pk):
    post = Post.objects.get(pk=pk)

    return render(
        reqeust,
        'blog/single_post_page.html',
        {
            'post' : post,
        }
    )