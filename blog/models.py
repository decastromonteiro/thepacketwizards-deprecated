from django.contrib.auth import get_user_model
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils.text import slugify
import re

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def get_name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


# Create your models here.
class BlogSeries(models.Model):
    title = models.CharField(max_length=80)
    # description = models.TextField(max_length=180)
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title


class BlogCategory(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(unique=True, editable=True, max_length=100)
    description = models.CharField(max_length=180)
    thumbnail = models.ImageField(blank=True, null=True)
    content = MarkdownxField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    publish_date = models.DateTimeField(null=True, blank=True)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    series_index = models.IntegerField(null=True, blank=True)
    # Relations
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1)
    series = models.ForeignKey(BlogSeries, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True)

    def formatted_markdown(self):
        """
        Transform content into HTML code
        """
        return markdownify(self.get_clean_content())

    def get_truncated_content(self):
        """
        Get content between ::begin:: and ::more:: Tag and return it.
        """
        pattern = re.compile(r'(?<=::begin::)(.*)(?=::more::)', re.DOTALL)
        truncated = self.content[:300]
        if '::more::' in self.content:

            truncated = re.search(pattern, self.content)
            if truncated:
                return markdownify(truncated.group())
        return markdownify(truncated)

    def get_clean_content(self):
        """
        Get content field and rip it off from ::more:: and ::begin:: Tags
        Return Content without those tags.
        """
        return self.content.replace('::more::', '').replace('::begin::', '')

    def __str__(self):
        return self.title

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)

        super(BlogPost, self).save()
