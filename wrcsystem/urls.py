from django.urls import path
from . import views

urlpatterns = [
    path('login',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path("",views.index,name="index"),
    
    path("data_all",views.data_all,name="data_all"),
    path("data_water_level",views.data_water_level,name="data_water_level"),
    path("data_out",views.data_out,name="data_out"),
    path("data_in",views.data_in,name="data_in"),
    path("data_water_temp",views.data_water_temp,name="data_water_temp"),
    path("data_ground",views.data_ground,name="data_ground"),
    
    path('raspost_all', views.raspost_all, name="raspost_all" ),
    path('raspost_access_check', views.raspost_access_check, name="raspost_access_check" ),
    
    path('test_list', views.test_list, name='test_list'),
    path('water_temperature_list', views.water_temperature_list, name='water_temperature_list'),
    path('water_high_list', views.water_high_list, name='water_high_list'),
    path('riskmap_list', views.riskmap_list, name='riskmap_list'),
    path('delete_test', views.delete_test, name="delete_test"),
    path('delete_water_temperature', views.delete_water_temperature, name="delete_water_temperature"),
    path('delete_water_high', views.delete_water_high, name="delete_water_high"),
    path('raspost_test', views.raspost_test, name="ras_post_test" ),
    path('raspost_water_temp', views.raspost_water_temp, name="ras_post_water_temp" ),
    path('raspost_water_high', views.raspost_water_high, name="ras_post_water_high" ),
    path('raspost_risk_map', views.raspost_risk_map, name="raspost_risk_map"),
    
    path("survey",views.survey,name="survey"),
]