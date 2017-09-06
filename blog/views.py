from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post
from blog.forms import BlogPostForm
from django.views.generic import ListView, DetailView

def post_list(request):
    post_blog_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {
        'post_blog_list': post_blog_list,
    }
    return render(request, 'blog/post_list.html',context)

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
