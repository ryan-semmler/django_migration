from django.http import HttpResponse


def index(request):
    return HttpResponse("OSU football db project")
