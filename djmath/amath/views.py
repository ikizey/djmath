from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("<h1>test</h1>")
    return render(request, "amath/index.html")
