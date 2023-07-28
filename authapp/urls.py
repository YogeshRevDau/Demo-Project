from django.urls import path

from . import views
urlpatterns=[
    path('',views.loginView),
    path('register/',views.RegisterView,name='register'),
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout')

]