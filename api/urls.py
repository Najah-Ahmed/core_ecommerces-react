from django.urls import path, include
from rest_framework.authtoken import views
from .views import home
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [

    path('', home, name="home"),
    path('category/', include('api.category.urls')),
    path('product/', include('api.products.urls')),
    # path('user/', include('api.users.urls')),
    path('user/', include('api.user_app.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
