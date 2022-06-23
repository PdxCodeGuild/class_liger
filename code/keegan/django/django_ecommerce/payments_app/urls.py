from django.urls import path

from . import views

app_name = 'payments_app'

urlpatterns = [
    path('config/', views.stripe_config, name='stripe_config'),
    path('checkout/', views.checkout, name="stripe_checkout"),
    path('receipt/<str:username>', views.receipt, name='receipt')
]