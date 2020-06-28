from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, CustomerViewSet, OrderViewSet, OrderDetailViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'customsers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orders-detail', OrderDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
