from django.shortcuts import render


def homeView(request):
    return render(request,'index.html'),
# Create your views here.
