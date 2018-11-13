from django.urls import path

from landing import views

urlpatterns = [
    path('order/', views.OrderView.as_view(), name='order'),
    path('', views.IndexView.as_view(), name='index'),
]
