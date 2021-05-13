from rest_framework import routers
from django.urls import path, include

from cadastro.views import MembroViewSet

router = routers.DefaultRouter()
router.register('membro', MembroViewSet, basename='membro')

urlpatterns = [
    path('', include(router.urls)),
]
