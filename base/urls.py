from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('room/create/',views.createRoom,name='create_room'),
    path('room/edit/<int:pk>/',views.updateRoom,name='edit_room'),
    path('room/delete/<int:pk>/',views.deleteRoom,name='delete_room'),
    path('room/<int:pk>/',views.room,name='room'),
]
