from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postview/<int:id>', views.post_de, name='view'),
    path('publish/', views.setpost, name='setpublish'),
]