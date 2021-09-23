from django.urls import path, include
from .views import home_page, list_compo, another_one
app_name = 'main'
urlpatterns = [
    path('homepage/',list_compo,name='home'),
    path('anotherone/',another_one,name='another_one')
]
