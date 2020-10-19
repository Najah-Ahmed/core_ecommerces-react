from rest_framework import routers
from django.urls import path, include
from .views import CategoryViewSet

# *** routers vd as_view()

router = routers.DefaultRouter()
router.register(r'', CategoryViewSet)
urlpatterns = [
    path('', include(router.urls)),

    # path('', CategoryGenerics.as_view())
]
