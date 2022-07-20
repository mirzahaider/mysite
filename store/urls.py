from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.show_store),
    path('products/', views.product_list),
    path('products/<int:product_id>/', views.product_detail),
]
