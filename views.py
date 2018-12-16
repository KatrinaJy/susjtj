
from django.http import HttpResponse
from django.shortcut import redirect
def index(request):
    return HttpResponse("ok")

def register(request):
    return redirect("")
