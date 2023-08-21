from django.urls import path

from apps.pages.views import HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("about/", AboutPageView.as_view(), name='about')

]
