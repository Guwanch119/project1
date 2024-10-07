from django.shortcuts import render


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
