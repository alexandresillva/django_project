from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("This is a new project based in Django.")
