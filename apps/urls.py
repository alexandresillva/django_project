from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.pages.urls")),
    path("posts/", include("apps.posts.urls")),
    path("blog/", include("apps.blog.urls")),
]
