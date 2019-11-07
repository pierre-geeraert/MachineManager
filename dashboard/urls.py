from django.urls import path
from . import views,function

urlpatterns = [
    path('manage/<id_proxmox>/<id_machine>/<action>/', function.action),
    path('article/<id_article>', function.test),
    path('manage/<id_proxmox>/<id_machine>/<action>', function.action),
    path('', views.home),
    path('dash',views.web)
]
