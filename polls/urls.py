from django.urls import path

from . import views

urlpatterns = [
    # 127.0.0.1/polls/''
    path('', views.index, name="index"),
]

