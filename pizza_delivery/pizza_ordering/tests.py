from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import PizzaBase, Cheese, Topping, Pizza
from django.urls import reverse

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_cheese(self):
        data = {'name': 'Mozzarella'}
        response = self.client.post(reverse('create_cheese'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_pizza_base(self):
        data = {'name': 'Thin Crust'}
        response = self.client.post(reverse('create_pizza_base'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_topping(self):
        data = {'name': 'Pepperoni'}
        response = self.client.post(reverse('create_topping'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_pizza(self):
        base = PizzaBase.objects.create(name='Thin Crust')
        cheese = Cheese.objects.create(name='Mozzarella')
        toppings = [Topping.objects.create(name='Pepperoni') for _ in range(5)]

        data = {
            'base': base.id,
            'cheese': cheese.id,
            'toppings': [topping.id for topping in toppings]
        }

        response = self.client.post(reverse('create-pizza'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_get_pizza_base_by_id(self):
        pizza_base = PizzaBase.objects.create(name='Thin Crust')
        response = self.client.get(reverse('get_pizza_base_by_id', kwargs={'pk': pizza_base.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_pizza_base_by_id_not_found(self):
        response = self.client.get('/api/pizza_base/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_get_cheese_by_id(self):
        cheese = Cheese.objects.create(name='Mozzarella')
        response = self.client.get(reverse('get_cheese_by_id', kwargs={'pk': cheese.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_cheese_by_id_not_found(self):
        response = self.client.get('/api/cheese/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_topping_by_id(self):
        topping = Topping.objects.create(name='Pepperoni')
        response = self.client.get(reverse('get_topping_by_id', kwargs={'pk': topping.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_topping_by_id_not_found(self):
        response = self.client.get('/api/get_topping_by_id/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_pizza_by_id(self):
        base = PizzaBase.objects.create(name='Thin Crust')
        cheese = Cheese.objects.create(name='Mozzarella')
        toppings = [Topping.objects.create(name='Pepperoni') for _ in range(5)]
        pizza = Pizza.objects.create(base=base, cheese=cheese)
        pizza.toppings.set(toppings)
        response = self.client.get(reverse('get_pizza_by_id', kwargs={'pk': pizza.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_pizza_by_id_not_found(self):
        response = self.client.get('/api/get_pizza_by_id/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_pizza_bases(self):
        response = self.client.get(reverse('pizza-base-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_cheeses(self):
        response = self.client.get(reverse('cheese-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_toppings(self):
        response = self.client.get(reverse('topping-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_pizzas(self):
        response = self.client.get(reverse('pizza-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_orders(self):
        response = self.client.get(reverse('order-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
