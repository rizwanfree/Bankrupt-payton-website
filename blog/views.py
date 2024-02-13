from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.views.generic import ListView
# Create your views here.

def blog_index(request):
    posts = Post.published.all()
    recent_posts = Post.published.all().order_by('-id')[:10]
    context = {
        'posts': posts,
        'recent_posts': recent_posts
        }
    return render(request, 'blog/post/blog.html', context)


# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'blog/post/blog.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    context = {
        'post': post 
    }
    return render(request, 'blog/post/blog-single.html', context)