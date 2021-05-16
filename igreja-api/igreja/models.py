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
    complemento = CharField(max_length=200)

    class Meta:
        abstract = True

class Contato(Model):

    telefone = IntegerField()
    celular = IntegerField()
    rede_social = CharField(max_length=50)

    class Meta:
        abstract = True


class Igreja(Entidade, Endereco):
    nome = CharField(blank=False, null=False, max_length=200)

class Membro(Entidade, Endereco, Contato):

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

    def __str__(self):
        return f'{self.nome} | {self.data_nascimento}'
