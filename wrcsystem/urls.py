from django.urls import path
from . import views

urlpatterns = [
    path('login',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path("",views.index,name="index"),
    
    path('test_list', views.test_list, name='test_list'),
    path('water_temperature_list', views.water_temperature_list, name='water_temperature_list'),
    path('delete_test', views.delete_test, name="delete_test"),
    path('delete_water_temperature', views.delete_water_temperature, name="delete_water_temperature"),
    path('raspost_test', views.raspost_test, name="ras_post_test" ),
    path('raspost_water', views.raspost_water, name="ras_post_water" ),
]