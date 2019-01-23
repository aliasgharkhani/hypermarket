from django.shortcuts import render
from hyper_site.models import *


# Create your views here.

def store(request):
    materials = Material.objects.get()
    return render(request, 'store.html', {'materials': materials, })
