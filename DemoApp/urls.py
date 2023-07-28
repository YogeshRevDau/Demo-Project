from django.urls import path

from . import views
urlpatterns=[
    #path('form/',views.homeView),
    path('show/',views.showView,name='showdata'),
    path('cart/',views.CartView,name='cart'),
    path('final/',views.finalPaymentView,name='final')
]