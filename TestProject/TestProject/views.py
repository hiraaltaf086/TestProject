from django.http import HttpResponse


def hello(request,name):
    return HttpResponse('<b>Hello '+name+'</b>')


def home(request):
    return HttpResponse('<b><h2>Home page</h2></b> ' )