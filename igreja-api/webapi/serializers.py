from rest_framework.serializers import (
    CharField,
    IntegerField,
    Serializer,
    DateField,
    EmailField
)

class EnderecoSerializer(Serializer):
    cidade = CharField()
    bairro = CharField()
    cep = IntegerField()
    rua = CharField()
    complemento = CharField()
    numero = CharField()

class ContatoSerializer(Serializer):
    celular = IntegerField()
    email = EmailField()
    rede_social = CharField()

class MembroSerializer(Serializer):
    nome = CharField()
    data_nascimento = DateField()
    endereco = EnderecoSerializer()
    contato = ContatoSerializer()


