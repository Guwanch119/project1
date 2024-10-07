from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeView,name="homeURL"),
    path('bizbarada',views.bizbaradaView,name="bizbaradaURL"),
    path('yasalymlar',views.yasalymlarView,name="yasalymlarURL"),
    path('yumuslar',views.yumuslarView,name="yumuslarURL"),
    path('statistika',views.statistikaView,name="statistikaURL"),
    path('kalendar',views.kalendarView,name="kalendarURL"),
]