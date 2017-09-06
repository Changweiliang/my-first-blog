from django.forms import ModelForm
from blog.models import PostComment

class BlogPostForm(ModelForm):
    class Meta:
        model = PostComment
        fields = [ 'comment_post', 'comment_author','comment_text']
