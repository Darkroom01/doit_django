from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts' : posts,
#         }
#     )
#
def single_post_page(reqeust, pk):
    post = Post.objects.get(pk=pk)

    return render(
        reqeust,
        'blog/single_post_page.html',
        {
            'post' : post,
        }
    )