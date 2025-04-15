from django.urls import path  # Import path instead of url
from . import views

app_name = 'first_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('musician_details/<pk>/', views.MusicianDetail.as_view(), name='musician_details'),
    path('add_musician/', views.AddMusician.as_view(), name='add_musician'),
    path('update_musician/<pk>/', views.UpdateMucisican.as_view(), name='update_musician'),
    path('deletemusician/<pk>/', views.DeletMusician.as_view(), name='deletemusician'),
    
]
