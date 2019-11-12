"""thepacketwizards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from blog.views import (home_page,
                        blog_index,
                        blog_post,
                        blog_category,
                        blog_series, create_blog_post)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('home/', home_page),
                  path("", home_page),
                  path("blog/", blog_index),
                  path('blog/create', create_blog_post),
                  path("blog/<slug:slug>", blog_post),
                  path("blog/category/<slug:category>", blog_category),
                  path("blog/series/<slug:series>", blog_series),
                  path('markdownx/', include('markdownx.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
