from django.db import models
from django.contrib.auth import get_user_model

class Produto(models.Model):
    name = models.CharField('Nome', max_length=255)
    value = models.DecimalField('Valor', max_digits=4, decimal_places=2)
    image = models.ImageField('Imagem', upload_to='produtos/')

    class Meta:
        verbose_name_plural = 'Produtos'
    
    def __str__(self) :
        return self.name

class Pedido(models.Model):
    descricao = models.CharField('Descrição', max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    endereco = models.CharField('Endereço', max_length=255)
    observacao = models.TextField('Observação', null=True, blank=True)
    status = models.BooleanField('Entregue', default=False)

    class Meta:
        verbose_name_plural = 'Pedidos'
    
    def __str__(self) :
        return self.descricao