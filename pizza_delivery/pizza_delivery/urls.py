from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizza-ordering/', include('pizza_ordering.urls')),
]
