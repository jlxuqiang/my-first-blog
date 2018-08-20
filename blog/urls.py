from django.urls import path
from . import views

urlpatterns = [
path('jet/', views.post_list, name='post_list'),
]