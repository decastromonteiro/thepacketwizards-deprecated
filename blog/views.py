from django.shortcuts import render
from .models import BlogPost


# Create your views here.
def home_page(request):
    title = "The Packet Wizards"
    qs = BlogPost.objects.all().order_by('-created')[:3]
    context = {"title": title, 'blog_list': qs}
    return render(request, "index/index.html", context)


def blog_index(request):
    title = "Blog - The Packet Wizards"
    qs = BlogPost.objects.all().order_by('-created')[:5]
    context = {"title": title, 'blog_list': qs}
    return render(request, "blog/index.html", context)


def blog_post(request, slug):
    qs = BlogPost.objects.get(slug=slug)
    context = {"title": qs.title, 'blog_post': qs}
    return render(request, "blog/blog_post.html", context)


def blog_category(request, category):
    pass