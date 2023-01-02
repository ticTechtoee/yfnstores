from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('prod-details/<int:pk>', views.prod_details, name='productDetails'),

]
