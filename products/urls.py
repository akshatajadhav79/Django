from django.urls import path
from products import views


urlpatterns = [
    path('base/',views.base,name='base'),
    path('',views.home,name='home'),
    
     
]
