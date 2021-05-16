from rest_framework.viewsets import ModelViewSet

from igreja.models import Membro
from webapi.serializers import MembroSerializer

class MembroViewSet(ModelViewSet):
    queryset = Membro.objects.all()
    serializer_class =  MembroSerializer

    http_method_names = ['get', 'post', 'put']
