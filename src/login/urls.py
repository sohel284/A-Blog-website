from django.urls import path
from . import views



app_name = 'login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_page, name='login'), 
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('change-profile/', views.user_change, name='change_user'), 
    path('password/', views.pass_change, name='changed_passord'),
    path('add-picture/', views.add_pro_pic, name='add_pro_pic'),
    path('change-picture/', views.change_pro_pic, name='change_pro_pic'),
]


