from django.urls import path

from apps.blog.views import BlogCreateView
from apps.pages.views import HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("about/", AboutPageView.as_view(), name='about'),
    path("blog/post/new/", BlogCreateView.as_view(), name="post_new"),

]
