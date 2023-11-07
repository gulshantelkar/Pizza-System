from django.urls import path
from . import views

urlpatterns = [
     path('api/create_cheese/', views.create_cheese, name='create_cheese'),
    path('api/create_pizza_base/', views.create_pizza_base, name='create_pizza_base'),
    path('api/create_topping/',views.create_topping, name='create_topping'),
    path('api/pizza-bases/', views.get_pizza_bases, name='pizza-base-list'),
    path('api/cheeses/', views.get_cheeses, name='cheese-list'),
    path('api/toppings/', views.get_toppings, name='topping-list'),
    path('api/pizzas/', views.get_pizzas, name='pizza-list'),
    path('api/orders/', views.get_orders, name='order-list'),
    path('api/create_pizzas/', views.create_pizza, name='create-pizza'),
    path('api/create_orders/', views.create_order, name='create-order'),
    path('api/pizza_base/<int:pk>/', views.get_pizza_base_by_id,name='get_pizza_base_by_id'),
    path('api/cheese/<int:pk>/', views.get_cheese_by_id, name='get_cheese_by_id'),
    path('api/topping/<int:pk>/', views.get_topping_by_id,name='get_topping_by_id'),
    path('api/pizza/<int:pk>/', views.get_pizza_by_id,name ='get_pizza_by_id'),
    path('api/order/<int:pk>/', views.get_order_by_id,name='get_order_by_id'),
]
