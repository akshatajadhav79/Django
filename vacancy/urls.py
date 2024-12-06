from . import views
from django.urls import path,include


urlpatterns = [
    path('createVacancy/',views.createVacancy,name='createVacancy'),
    path('Candidates/',views.Candidates,name='Candidates'),
    path('vacancyshow/',views.vshow,name='vacancyshow'),
    path('vacancyapply/<int:id>',views.vapply,name='vacancyapply'),
    path('delete_v/<int:id>/',views.delete_v,name='delete_v'),
    
]
