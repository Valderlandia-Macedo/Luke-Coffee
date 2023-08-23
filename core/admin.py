from django.contrib import admin
from core.models import Produto, Pedido

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'produto', 'user', 'status')