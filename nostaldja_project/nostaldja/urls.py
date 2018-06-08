from django.urls import path
from . import views

urlpatterns = [
    # if we go to '/', go to the views, run the decade_list function.
    # third argument is naming this path.
    path('', views.decade_list, name='decade_list'),
    path('decades/<int:pk>', views.decade_detail, name='decade_detail'),
    path('decades/new', views.decade_create, name='decade_create'),
    path('decades/<int:pk>/edit', views.decade_edit, name='decade_edit'),
    path('decades/<int:pk>/delete', views.decade_delete, name='decade_delete'),
    path('songs/', views.fad_list, name='fad_list'),
    path('fads/<int:pk>', views.fad_detail, name='fad_detail'),
    path('fads/new', views.fad_create, name='fad_create'),
    path('fads/<int:pk>/edit', views.fad_edit, name='fad_edit'),
    path('fads/<int:pk>/delete', views.fad_delete, name='fad_delete'),
