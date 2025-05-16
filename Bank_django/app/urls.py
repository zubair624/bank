from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('1',views.create, name="create"),
    path('pin',views.pin,name="pin"),
    path('bal',views.balance,name="bal"),
    path('deposit',views.deposit,name="deposit"),
    path('withdrawl',views.withdrawl,name="withdrawl"),
    path('acc',views.acc_transfer,name="transfer")
]