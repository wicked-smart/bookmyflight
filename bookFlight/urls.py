from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:name>/', views.hello, name="hello")

]