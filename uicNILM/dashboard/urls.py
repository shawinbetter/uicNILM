from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('visualization/index', views.visualization_index, name='visualization_index')
]
