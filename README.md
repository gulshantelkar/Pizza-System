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
![image](https://github.com/gulshantelkar/Pizza-System/assets/99161604/533709a2-77aa-43c9-8e8f-e536ddda8243)


# Unit Testing for the API's 

1. I have added unit testing in the docker script so no need to expliclity run that
-<img width="910" alt="Screenshot 2023-11-24 at 4 11 09 PM" src="https://github.com/gulshantelkar/Pizza-System/assets/99161604/516daff2-c585-4abc-aa62-32447c8d0449">

   
## Running the System

1. Change the directory to ``` cd pizza_delivery```.

2. Build and run the system with Docker Compose: ``` docker-compose up --build ```

3. Open Postman and test the endpoints, Please follow the steps given below ( Need to add atleast 5 Toppings )

   
## Create Pizza Base Endpoint

- Endpoint: `localhost:8000/pizza-ordering/api/create_pizza_base/`
- <img width="1033" alt="281053710-401a426c-fd6b-41e6-80f4-45236aa8c261" src="https://github.com/gulshantelkar/Pizza-System/assets/99161604/e6d874b3-394a-46bd-80bb-6013a1f92417">


## Create Cheese Endpoint

- Endpoint: `localhost:8000/pizza-ordering/api/create_cheese/`
- ![image](https://github.com/gulshantelkar/Pizza-System/assets/99161604/a5cde771-e50e-46ac-9309-e0b03654dc80)


## Create Toppings Endpoint

- Endpoint: `localhost:8000/pizza-ordering/api/create_topping/`
- ![image](https://github.com/gulshantelkar/Pizza-System/assets/99161604/2f180f11-0c5c-4de7-b6f0-4159ea47bbb2)



## Create Pizza Endpoint

- Endpoint: `localhost:8000/pizza-ordering/api/create_pizzas/`
- Additional Info: You need to provide the ID assigned to the topping name.
- <img width="1047" alt="281054543-6875cf72-5102-40b1-9198-4f63e09b6f2c" src="https://github.com/gulshantelkar/Pizza-System/assets/99161604/0ab8a918-c3c6-45a3-b6ad-272d08e49e8f">



## Create Orders Endpoint

- Endpoint: `localhost:8000/pizza-ordering/api/create_orders/`
- Additional Info: Celery task will automatically be assigned; no need to run Redis server and Celery from your side. These services are also included in Docker.
- <img width="1039" alt="281054961-3d556f29-a3a4-4f0d-80b6-4529c286384f" src="https://github.com/gulshantelkar/Pizza-System/assets/99161604/18524814-5307-4da9-9f17-61faadd25b9c">


- The image shows that the Celery task is working on the conditions.
- <img width="1120" alt="281055437-29bd5256-e4b1-47ce-aa5c-83099342dce8" src="https://github.com/gulshantelkar/Pizza-System/assets/99161604/022ee7d7-5c91-48a7-846e-b2084aba79a8">


## List of All Orders Endpoint

- Endpoint: `http://localhost:8000/pizza-ordering/api/orders/`
- <img width="1010" alt="281055677-32882baf-d236-408e-996d-9e6a4a238bfc" src="https://github.com/gulshantelkar/Pizza-System/assets/99161604/018bcb99-bee7-4e2f-8ef4-d749fc578976">


## List of All Pizzas

- Endpoint: `http://localhost:8000/pizza-ordering/api/pizzas/`
- <img width="996" alt="281056332-582c3447-c8e4-4052-aba3-efa90620456e" src="https://github.com/gulshantelkar/Pizza-System/assets/99161604/329cbb1b-fc34-459f-8592-a14fd53e9c2a">


## Get a Single Entry of an Order

- Endpoint: `http://localhost:8000/pizza-ordering/api/order/id`
- <img width="996" alt="281056802-a46fc478-9c81-4d42-8493-109fa94f1242" src="https://github.com/gulshantelkar/Pizza-System/assets/99161604/e33d6709-cca0-4a59-bffa-6ff5139087c2">



## Get a Single Entry of Pizza Base, Cheese, Topping, Pizza

- Endpoints:
- `http://localhost:8000/pizza-ordering/api/pizza_base/id`
- `http://localhost:8000/pizza-ordering/api/cheese/id`
- `http://localhost:8000/pizza-ordering/api/topping/id`
- `http://localhost:8000/pizza-ordering/api/pizza/id`
- `http://localhost:8000/pizza-ordering/api/topping/id`
