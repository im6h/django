from django.urls import path, include
from rest_framework import routers
from .views import HeroViewSet, PowerViewSet

router = routers.DefaultRouter()
router.register(r'heroes', HeroViewSet)
router.register(r'powers', PowerViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
