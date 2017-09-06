from django.forms import ModelForm
from blog.models import Post

class BlogPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'create_date', 'published_date']
