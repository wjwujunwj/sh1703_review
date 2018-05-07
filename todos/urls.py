from django.urls import path
from . import views

urlpatterns = [
    path(r'hello/', views.hello),
    path(r'hello1/', views.hello_tpl),

]
