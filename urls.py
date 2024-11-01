from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_page, name='add'),
    path('add2/', subtract_page, name='subtract'),
    path('add3/', multiply_page, name='multiply'),
    path('add4/', divide_page, name='divide'),

]

