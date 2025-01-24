from django.urls import path
from . import views

app_name = 'current'

urlpatterns = [
    path('', views.current, name="current"),
    path('keep_frame/', views.keep_frame, name="keep_frame"),
    path('new_frame/', views.new_frame, name="new_frame"),
    path('search_without_frame/', views.search_view, name="search_view"),
    path('search_with_frame/', views.new_frame_view, name="new_frame_view"),
    path('list/', views.doors_list, name="list"),
    path('new-door/', views.door_new, name="new-door"),
    path('page/<int:pk>/', views.doors_page, name="page"),
    path('my_doors/', views.my_doors, name='my_doors'),
    path('edit_door/<int:pk>/', views.edit_door, name='edit_door'),
    path('delete_door/<int:pk>/', views.delete_door, name='delete_door'),
]
