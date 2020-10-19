from django.urls import path, include
from rest_framework.authtoken import views
from .views import home
urlpatterns = [

    path('', home, name="home"),
    path('category/', include('api.category.urls')),
    path('product/', include('api.products.urls')),
    path('user/', include('api.users.urls')),
]
