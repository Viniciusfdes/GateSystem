from django.urls import path
from . import views 

urlpatterns = [
    path('user/', views.user_list, name='UserList'),
    path('user_add/', views.user_add, name='UserAdd'),
    path('user_edit/<int:user_pk>', views.user_edit, name='UserEdit'),
    path('user_remove/<int:user_pk>', views.user_remove, name='UserRemove'),
    path('veh/', views.veh_list, name = 'VehList'),
    path('veh_add/', views.veh_add, name='VehAdd'),
    path('veh_edit/<int:vehicle_pk>', views.veh_edit, name='VehEdit'),
    path('veh_remove/<int:vehicle_pk>', views.veh_remove, name='VehRemove')
]
