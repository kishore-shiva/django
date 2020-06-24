from django.urls import path

from . import views
from polls.views import index

urlpatterns = [
    path('', views.index, name='index'),
]
