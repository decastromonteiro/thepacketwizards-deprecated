from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import BlogPost
from .forms import BlogPostForm


# Create your views here.
def home_page(request):
    title = "The Packet Wizards"
    qs = BlogPost.objects.all().order_by('-publish_date')[:3]
    context = {"title": title, 'blog_list': qs}
    return render(request, "index/index.html", context)


def blog_index(request):
    title = "Blog - The Packet Wizards"
    qs = BlogPost.objects.all().order_by('-publish_date')
    paginator = Paginator(qs, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {"title": title, 'blog_list': posts}
    return render(request, "blog/index.html", context)


def create_blog_post(request):
    title = 'The Packet Wizards Blog'
    if request.user.is_authenticated:
        form = BlogPostForm()
        context = {"title": title,
                   "form": form}
        return render(request, "blog/form.html", context)
    return redirect('/blog')


def blog_post(request, slug):
    qs = BlogPost.objects.get(slug=slug)
    context = {"title": qs.title, 'blog_post': qs}
    return render(request, "blog/blog_post.html", context)


def blog_category(request, category):
    qs = BlogPost.objects.filter(
        category__slug__exact=category
    ).order_by("-publish_date")
    category = qs.first().category.title
    context = {"title": 'Category: {}'.format(category),
               'blog_list': qs,
               'category': category}
    return render(request, "blog/category.html", context)


def blog_series(request, series):
    qs = BlogPost.objects.filter(
        series__slug__exact=series
    )
    series = qs.first().series.title
    context = {"title": 'Series: {}'.format(series),
               'blog_list': qs,
               'series': series}
    return render(request, "blog/series.html", context)
