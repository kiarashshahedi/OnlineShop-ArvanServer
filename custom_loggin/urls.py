from django.urls import path
from . import views


urlpatterns = [

    #Register with Mobile and OTP
    path('register/', views.register_view, name='register_view'),
    
    #verify OTP code TRUE or FALSE 
    path('verify/', views.verify, name='verify'),

    #User dashboard page
    path('dashboard/', views.dashboard, name='dashboard'),
    #logout(for all parts used)
    path('logout/', views.logout_view, name='logout_view'), 

    #Login with Mobile and password
    path('login/', views.login_user, name='login'),

    #Register with Mobile and Password
    path ('passRegister/', views.UsernameRegister, name='passRegister'),

    path('edit/', views.edit_user_info, name='edit_info'),

    #update_user
    path('update_user/', views.update_user, name='update_user'),

    #update_pass
    path('update_password/', views.update_password, name='update_password'),

    #update_User_info
    path('update_info/', views.update_info, name='update_info'),

    #about page
    path('about-us/', views.about_us, name="about_us" ),

]


