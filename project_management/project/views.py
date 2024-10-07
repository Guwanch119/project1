from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login
from .forms import studentloginform


def student_login(request):
    if request.method == "POST":
        form = studentloginform(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect('homeURL')
    else:
        form = studentloginform()
    return render(request,'login.html',{'form':form})

def logout(request):
    logout(request)
    return redirect('homeURL')



def homeView(request):
    return render(request,'index.html')



def bizbaradaView(request):
    return render(request,'bizbarada.html')

def yasalymlarView(request):
    return render(request,'yasalymlar.html')

def yumuslarView(request):
    return render(request,'yumuslar.html')

def statistikaView(request):
    return render(request,'statistika.html')

def kalendarView(request):
    return render(request,'kalendar.html')
