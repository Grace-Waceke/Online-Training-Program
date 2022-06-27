from atexit import register
from  django.urls import path
from .views import communities
urlpatterns =[
    path('', communities, name='communities')

]