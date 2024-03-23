from django.urls import path
from .views import add_laptop, show_laptop, update_laptop, delete_laptop


urlpatterns = [
    path('add/', add_laptop, name='add_url'),
    path('show/', show_laptop, name='show_url'),
    path('update/<int:pk>/', update_laptop, name='update_url'),
    path('delete/<int:pk>/', delete_laptop, name='delete_url'),
]
