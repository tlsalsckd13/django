from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name="index"),
    path('single/', views.single, name="single"),
    path('chart/', views.chart, name="chart"),
    path('playlist/', views.playlist, name="playlist"),
    path('list_add/<int:music_no>', views.list_add, name='list_add'),
    path('albumdetail/<int:list_id>/', views.albumdetail, name="albumdetail"),
    path('list_delete/<int:music_no>', views.list_delete, name='list_delete'),
    path('musicdetail/<int:list_id>', views.musicdetail, name="musicdetail"),
]