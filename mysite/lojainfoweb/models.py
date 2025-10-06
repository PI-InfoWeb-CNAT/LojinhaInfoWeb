from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    TIPO = {
        'a': 'Aluno de InfoWeb',
        'd': 'Aluno ou servidor da DIATINF',
        'i': 'Aluno ou servidor do IFRN',
        'o': 'Outros...'
    }
    tipo = models.IntegerField(choices=TIPO, default='o')
    valido = models.BooleanField(default=False)
    endereco = models.CharField(maxlength=100)

class Compra(models.Model):
    ESTADO = {
        1: 'Carrinho de compras',
        2: 'Compra finalizada',
        3: 'Entrega em curso',
        4: 'Entrega realizada',
        9: 'Cancelada'
    }
    estado = models.IntegerField(choices=ESTADO, default=1)
    data = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
