from django.db.models import (
    Model,
    BooleanField,
    CharField,
    IntegerField,
    DateField
)

class Entidade(Model):
    ativa = BooleanField(default=True)

    class Meta:
        abstract = True

class Endereco(Model):
    cep = IntegerField()
    cidade = CharField(max_length=100)
    bairro = CharField(max_length=100)
    rua = CharField(max_length=200)
    complemento = CharField()

    class Meta:
        abstract = True


class Igreja(Entidade, Endereco):
    nome = CharField(blank=False, null=False, max_length=200)

class Membro(Entidade, Endereco):

    STATUS_CHOICES = (
        (1, 'MEMBRO'),
        (3, 'DISCIPLINADO'),
        (4, 'DESVIADO'),
    )

    DEPARTAMENTO_CHOICES = (
        (0, 'MEMBRO'),
        (1, 'CRIANÇA'),
        (2, 'ADOLESCENTE'),
        (3, 'JOVEM'),
        (4, 'SENHORA'),
        (5, 'MINISTÉRIO'),
    )

    nome = CharField(max_length=200, blank=False, null=False)
    data_nascimento = DateField(blank=False, null=False)
    status = IntegerField(choices=STATUS_CHOICES)
    departamento = IntegerField(choices=DEPARTAMENTO_CHOICES)
    telefone = IntegerField()

