from django.forms import ModelForm
from blog.models import BlogPost


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'slug',
            'description', 'thumbnail', 'content', 'published', 'featured',
            'publish_date', 'previous_post', 'next_post', 'series_index',
            'author', 'series', 'category'

        ]
