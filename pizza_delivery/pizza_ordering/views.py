from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PizzaBase, Cheese, Topping, Pizza, Order
from rest_framework.response import Response
from rest_framework import status
from .serializers import CheeseSerializer, PizzaBaseSerializer, ToppingSerializer,OrderSerializer,PizzaSerializer
from .tasks import update_order_status 
from django.utils import timezone 


@api_view(['POST'])
def create_cheese(request):
    serializer = CheeseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_pizza_base(request):
    serializer = PizzaBaseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_topping(request):
    serializer = ToppingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_pizza(request):
    serializer = PizzaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def create_order(request):
    request_data = request.data
    
    serializer = OrderSerializer(data=request_data)
    if serializer.is_valid():
        order = serializer.save()
        order.order_date = timezone.now()
        order.save()
        update_order_status.apply_async(args=(order.id,), countdown=30)

        return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_pizza_base_by_id(request, pk):
    try:
        pizza_base = PizzaBase.objects.get(pk=pk)
        serializer = PizzaBaseSerializer(pizza_base)
        return Response(serializer.data)
    except PizzaBase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_cheese_by_id(request, pk):
    try:
        cheese = Cheese.objects.get(pk=pk)
        serializer = CheeseSerializer(cheese)
        return Response(serializer.data)
    except Cheese.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_topping_by_id(request, pk):
    try:
        topping = Topping.objects.get(pk=pk)
        serializer = ToppingSerializer(topping)
        return Response(serializer.data)
    except Topping.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_pizza_by_id(request, pk):
    try:
        pizza = Pizza.objects.get(pk=pk)
        data = {
            'id': pizza.id,
            'base': pizza.base.name,
            'cheese': pizza.cheese.name,
            'toppings': [topping.name for topping in pizza.toppings.all()]
        }
        return Response(data)
    except Pizza.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_order_by_id(request, pk):
    try:
        order = Order.objects.get(pk=pk)
        data = {
            'id': order.id,
            'order_date': order.order_date,
            'customer_name': order.customer_name,
            'total_price': order.total_price,
            'status': order.status, 
            'pizzas': [
                {
                    'id': pizza.id,
                    'base': pizza.base.name,
                    'cheese': pizza.cheese.name,
                    'toppings': [topping.name for topping in pizza.toppings.all()]
                }
                for pizza in order.pizzas.all()
            ]
        }
        return Response(data)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_pizza_bases(request):
    try:
        pizza_bases = PizzaBase.objects.all().values('id', 'name')
        return Response(list(pizza_bases))
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_cheeses(request):
    try:
        cheeses = Cheese.objects.all().values('id', 'name')
        return Response(list(cheeses))
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_toppings(request):
    try:
        toppings = Topping.objects.all().values('id', 'name')
        return Response(list(toppings))
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_pizzas(request):
    try:
        pizzas = Pizza.objects.all().select_related('base', 'cheese').prefetch_related('toppings')
        data = [{'id': pizza.id, 'base': pizza.base.name, 'cheese': pizza.cheese.name, 'toppings': [topping.name for topping in pizza.toppings.all()]} for pizza in pizzas]
        return Response(data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_orders(request):
    try:
        orders = Order.objects.all().prefetch_related('pizzas__base', 'pizzas__cheese', 'pizzas__toppings')
        data = [
            {
                'id': order.id,
                'order_date': order.order_date,
                'customer_name': order.customer_name,
                'total_price': order.total_price,
                'status': order.status, 
                'pizzas': [
                    {
                        'id': pizza.id,
                        'base': pizza.base.name,
                        'cheese': pizza.cheese.name,
                        'toppings': [topping.name for topping in pizza.toppings.all()]
                    }
                    for pizza in order.pizzas.all()
                ]
            }
            for order in orders
        ]
        return Response(data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
