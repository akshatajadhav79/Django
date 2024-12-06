from . import views
from django.urls import path,include


urlpatterns = [
    path('login/',views.login_page,name='login'),
    path('logout',views.logout_user,name="logout"),
    path('register/',views.register,name="register"),
    path("reset_password/",views.reset_password,name="reset_password"),
    
    path('Userview/',views.User_view,name='Userview'),
    path('delete_user/<int:id>/',views.delete_user,name='delete_user'),
    path('update_muser/<int:id>/',views.update_muser,name='update_muser'),
    # path('activate/<email_token>/',views.activate_email,name='activate'),
    
    path('contact/',views.contact_master,name="contact"),
    path('contactview/',views.contactview,name="contactview"),
    path('delete_cust/<id>/',views.delete_cust, name="delete_cust"),
    
    path('services/',views.service_master,name="services"),
    
    path('advature',views.advature_master,name="advature"),
    
    path('book',views.booking_master,name="book"),
    path('bookview',views.bookview,name="bookview"),
    
     
]
