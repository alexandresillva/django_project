from django.urls import path

from apps.pages.views import home_page_view

urlpatterns = [
    path("", home_page_view, name='home')
]