from django.shortcuts import render
from blog.models import BlogPost


def home_page(request):
    title = "The Packet Wizards"
    qs = BlogPost.objects.all().order_by('-publish_date').filter(
        published=True,
        featured=True
    )[:3]
    context = {"title": title, 'blog_list': qs}
    return render(request, "index/index.html", context)