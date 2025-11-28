from django.urls import path
from .views import health, favicon


urlpatterns = [
    path('', health, name='health'),
    path('favicon.ico', favicon, name='favicon'),
]


path('api/classes/', views.get_classes, name='get_classes'),
path('api/classes/', views.get_classes, name='get_classes'),
path('api/classes/', views.get_classes, name='get_classes'),
