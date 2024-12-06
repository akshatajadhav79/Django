from django.shortcuts import render
from staff.models import MenuMaster

from django.contrib.auth import authenticate ,logout,login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def base(request):
    all_urls= MenuMaster.objects.all()
    context = {"menu": all_urls}
    return render(request,"base/base.html", context)


def home(request):
    all_urls= MenuMaster.objects.all()
    context = {"menu": all_urls}
    return render(request,"products/index.html", context)