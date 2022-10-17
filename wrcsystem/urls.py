from django.urls import path
from . import views

urlpatterns = [
    path('login',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path("",views.index,name="index"),
    
    path('test_list', views.test_list, name='test_list'),
    path('delete', views.delete, name="delete"),
    path('raspost', views.raspost, name="ras_post" ),
]