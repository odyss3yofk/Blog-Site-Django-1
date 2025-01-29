from django.shortcuts import render


def landing_page(request):
    return render(request, "blog/index.html")


def posts(request):
    pass


def post_details(request):
    pass
