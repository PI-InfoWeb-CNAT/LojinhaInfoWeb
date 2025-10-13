from django.db import models
from django.contrib.auth.models import User

#####
## 1. Classe Usuário
class Usuario(models.Model):
    TIPO = {
        1: 'Administrador',
        2: 'Gerente',
        3: 'Aluno InfoWeb',
        4: 'DIATINF',
        5: 'IFRN',
        9: 'Outros'
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.IntegerField(choices=TIPO, default=9)
    valido = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username


#####
## 2. Classe Comprador
class Comprador(Usuario):
    endereco = models.CharField(maxlength=100)
    def __str__(self):
        return 'Comprador: {}'.format(super())


#####
## 3. Classe Categoria
class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    def __str__(self):
        return self.nome


#####
## 4. Classe Produto
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='produtos')
    descricao = models.models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=15, decimal_places=2)
    quant_estoque = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, default=None, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.nome


#####
## 5. Classe Reserva
class Reserva(models.Model):
    data = models.DateField(auto_now_add=True)
    quantidade = models.IntegerField(default=1)
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    proxima = models.OneToOneField('Reserva', null=True, default=None)
    def __str__(self):
        return 'Reserva de {} para {}'.format(self.fila_reserva.produto.nome, self.comprador.user.username)


#####
## 6. Classe Fila de Reservas
class FilaReserva(models.Model):
    produto = models.OneToOneField(Produto)
    inicio = models.OneToOneField(Reserva, null=True, blank= True, default=None)
    fim = models.OneToOneField(Reserva, null=True, blank=True, default=None)
    def __str__(self):
        return 'Fila de reservas para {}'.format(self.produto.nome)
    def enfileirar(self, reserva):
        if self.inicio == None and self.fim == None:
            self.inicio = reserva
            self.fim = reserva
            self.save()
        else:
            self.fim.proximo = reserva
            self.fim.save()
            self.fim = reserva
            self.save()
    
#####
## 7. Classe Compra
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
    comprador = models.ForeignKey(Comprador, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return 'Compra de {} em {}'.format(self.comprador, self.data)

#####
## 8. Classe ItemDeCompra
class ItemDeCompra(models.Model):
    quantidade = models.IntegerField(default=1)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    def __str__(self):
        return 'Item da compra #{}'.format(self.compra.id)

