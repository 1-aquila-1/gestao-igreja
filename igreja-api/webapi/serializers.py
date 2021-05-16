from collections import OrderedDict
from rest_framework.serializers import (
    CharField,
    IntegerField,
    Serializer,
    DateField
)

from igreja.models import Membro


class EnderecoSerializer(Serializer):
    cidade = CharField()
    bairro = CharField()
    cep = IntegerField()
    rua = CharField()
    complemento = CharField()
    numero = CharField()

class ContatoSerializer(Serializer):
    telefone = IntegerField()
    celular = IntegerField()
    redes_socias = CharField()

class MembroSerializer(Serializer):
    STATUS_CHOICES = (
        (1, 'MEMBRO'),
        (3, 'DISCIPLINADO'),
        (4, 'DESVIADO'),
    )


    nome = CharField()
    data_nascimento = DateField()
    endereco = EnderecoSerializer()
    contato = ContatoSerializer()

    def create(self, validated_data):
        p = Membro()
        endereco = validated_data.pop('endereco')
        contato = validated_data.pop('contato')

        p.nome = validated_data.pop('nome')
        p.data_nascimento = validated_data.pop('data_nascimento')
        
        p.cep = endereco.pop('cep')
        p.cidade = endereco.pop('cidade')
        p.bairro = endereco.pop('bairro')
        p.rua = endereco.pop('rua')
        p.complemento = endereco.pop('complemento')

        p.telefone = contato.pop('telefone')
        p.celular = contato.pop('celular')
        p.rede_social = contato.pop('redes_socias')

        return p
    
    def to_representation(self, instance):
        rep = OrderedDict()
        rep['nome'] = instance.nome
        rep['data_nascimento'] = instance.data_nascimento

        rep['endereco'] = OrderedDict([
            ('cep', instance.cep),
            ('cidade', instance.cidade),
            ('bairro', instance.bairro),
            ('rua', instance.rua),
            ('complemento', instance.complemento)
        ])
        rep['contato'] = OrderedDict([
            ('telefone', instance.telefone),
            ('celular', instance.celular),
            ('rede_social', instance.redes_socias)
        ])
        
        return rep
