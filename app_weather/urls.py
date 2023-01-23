

from django.urls import path
from .views import *
urlpatterns = [
    path('weather/<str:city>',Index.as_view(), name = 'Index' )

]
