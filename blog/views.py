from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post, PostComment
from blog.forms.form import BlogPostForm


def post_list(request):
    post_blog_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {
        'post_blog_list': post_blog_list,
    }
    return render(request, 'blog/post_list.html',context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_comment = post.postcomment_set.all()
    print(request.method)
    if request.method == 'POST':
        comment_form = BlogPostForm(request.POST)

        # print(comment_form.is_valid())
        if comment_form.is_valid():
            comment_cd = comment_form.cleaned_data
            comment_cd['comment_post'] = post
            comment_cd['comment_published_date'] = timezone.now()
            new_comment = PostComment(**comment_cd)
            new_comment.save()
            print(comment_form.cleaned_data)
            # print(PostComment.objects.all())
            context = {
                'blog_detail': post,
                'blog_comment': post_comment,
                'comment_form': comment_form,
            }
            return render(request, 'blog/post_detail.html', context)
    else:
        comment_form = BlogPostForm()
        context = {
                'blog_detail': post,
                'blog_comment': post_comment,
                'comment_form': comment_form,
        }
        return render(request, 'blog/post_detail.html', context)
