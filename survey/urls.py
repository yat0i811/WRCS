from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sample1', views.sample1, name='sample1'),
    path('sample2', views.sample2, name='sample2'),
    path('sample2a', views.sample2a, name='sample2a'),
    path('sample2b', views.sample2b, name='sample2b'),
    path('sample2c', views.sample2c, name='sample2c'),
    path('sample2d', views.sample2d, name='sample2d'),
    path('sample2e', views.sample2e, name='sample2e'),
    path('sample2f', views.sample2f, name='sample2f'),
    path('sample2g', views.sample2g, name='sample2g'),
    path('sample3', views.sample3, name='sample3'),
    path('sample3/<int:id>/', views.sample3_detail, name='sample3_detail'),
    path('post_survey', views.post_survey, name='post_survey'),
    path('thanks',views.thanks, name='thanks'),
    path('download_survey',views.download_survey, name='download_survey'),
]