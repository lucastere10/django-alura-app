from django.urls import path, include
from gallery.views import index


urlpatterns = [
    path('', index)
]