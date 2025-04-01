from django.urls import path
from .views import home_view, createProject_view     

urlpatterns = [
    path('', home_view, name="home"),  
    path('create/<int:pk>', createProject_view, name="create-project")
]