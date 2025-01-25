from django.urls import path
from . import views
from .views import MarkerListView

app_name = 'historic'

urlpatterns = [
    path('', views.map_view, name='map_view'),
    path('api/markers/', MarkerListView.as_view(), name='marker-list'),
    path('map/', views.map_view, name='map'),
    path('marker/', views.marker, name='marker'),
    path('map/info/<int:pk>/', views.marker_info, name='marker_info'),
]
