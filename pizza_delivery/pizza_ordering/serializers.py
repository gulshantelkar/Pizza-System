from rest_framework import serializers
from .models import PizzaBase, Cheese, Topping, Pizza, Order

class PizzaBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaBase
        fields = '__all__'

class CheeseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheese
        fields = '__all__'

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'

    def create(self, validated_data):
        # Get the base, cheese, and toppings from the validated data
        base = validated_data.get('base')
        cheese = validated_data.get('cheese')
        toppings = validated_data.get('toppings')

        # Ensure that there's exactly one base, one cheese, and five toppings
        if not base or not cheese or len(toppings) != 5:
            raise serializers.ValidationError("A pizza must have exactly one base, one cheese, and five toppings.")

        # Create the pizza with the validated data
        pizza = Pizza.objects.create(base=base, cheese=cheese)
        
        # Add the toppings to the pizza
        pizza.toppings.set(toppings)

        return pizza

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('order_date',)