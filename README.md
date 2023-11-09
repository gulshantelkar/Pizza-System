# Pizza-System

## Tech Stack
- Language: Python
- Framework: Django
- Database: PostgreSQL
- ORM: Django ORM
- Services: Docker, Celery, Redis

## Additonal Info   
- Added Unit Testing

- MySQL was causing problems with my path variables, which is why I switched to PostgreSQL.

   
## Database Design : 
<img width="1038" alt="image" src="https://github.com/gulshantelkar/Pizza-System/assets/99161604/f9a17200-48da-437b-b4f1-a5efa85c022c">

## Running the System

1. Change the directory to ``` cd pizza_delivery```.

2. Build and run the system with Docker Compose: ``` docker-compose up --build ```

3. Open Postman and test the endpoints, Please follow the steps given below ( Need to add atleast 5 Toppings )

   
## Create Pizza Base Endpoint

- Endpoint: `localhost:8000/pizza-ordering/api/create_pizza_base/`
- ![Image](https://github.com/gulshantelkar/Pizza-System/assets/99161604/401a426c-fd6b-41e6-80f4-45236aa8c261)

## Create Cheese Endpoint

- Endpoint: `localhost:8000/pizza-ordering/api/create_cheese/`
- ![Image](https://github.com/gulshantelkar/Pizza-System/assets/99161604/4a9db9eb-759f-4ee7-8054-2014d864b2c1)

## Create Toppings Endpoint

- Endpoint: `localhost:8000/pizza-ordering/api/create_topping/`
- ![Image](https://github.com/gulshantelkar/Pizza-System/assets/99161604/8fdbcac6-9fa9-4e22-8fb8-11416339be7f)

## Create Pizza Endpoint

- Endpoint: `localhost:8000/pizza-ordering/api/create_pizzas/`
- Additional Info: You need to provide the ID assigned to the topping name.
- ![Image](https://github.com/gulshantelkar/Pizza-System/assets/99161604/6875cf72-5102-40b1-9198-4f63e09b6f2c)

## Create Orders Endpoint

- Endpoint: `localhost:8000/pizza-ordering/api/create_orders/`
- Additional Info: Celery task will automatically be assigned; no need to run Redis server and Celery from your side. These services are also included in Docker.
- ![Image](https://github.com/gulshantelkar/Pizza-System/assets/99161604/3d556f29-a3a4-4f0d-80b6-4529c286384f)
- The image shows that the Celery task is working on the conditions.
- ![Image](https://github.com/gulshantelkar/Pizza-System/assets/99161604/29bd5256-e4b1-47ce-aa5c-83099342dce8)

## List of All Orders Endpoint

- Endpoint: `http://localhost:8000/pizza-ordering/api/orders/`
- ![Image](https://github.com/gulshantelkar/Pizza-System/assets/99161604/32882baf-d236-408e-996d-9e6a4a238bfc)

## List of All Pizzas

- Endpoint: `http://localhost:8000/pizza-ordering/api/pizzas/`
- ![Image](https://github.com/gulshantelkar/Pizza-System/assets/99161604/582c3447-c8e4-4052-aba3-efa90620456e)

## Get a Single Entry of an Order

- Endpoint: `http://localhost:8000/pizza-ordering/api/order/id`
- ![Image](https://github.com/gulshantelkar/Pizza-System/assets/99161604/a46fc478-9c81-4d42-8493-109fa94f1242)

# I have also added Unit Testing for the API's 

1. Open new terminal : ``` cd pizza_delivery ```
2. Run this Commabd: ```python manage.py test pizza_ordering.tests```

## Get a Single Entry of Pizza Base, Cheese, Topping, Pizza

- Endpoints:
- `http://localhost:8000/pizza-ordering/api/pizza_base/id`
- `http://localhost:8000/pizza-ordering/api/cheese/id`
- `http://localhost:8000/pizza-ordering/api/topping/id`
- `http://localhost:8000/pizza-ordering/api/pizza/id`
- `http://localhost:8000/pizza-ordering/api/topping/id`
