from staff.views import *
from django.urls import path,include


urlpatterns = [
    path('Newstaff/',Newstaff,name='Newstaff'),
    path('staffType/',staffType, name='staffType'),
    # path('del_staff/<int:id>/',del_staff,name='del_staff/<int:id>/'),
    path('del_sm/<int:id>/',del_sm,name='del_sm/<int:id>/'),
    # path('upTy/<int:id>/',upTy,name='upTy/<int:id>/'),
    
    
] 