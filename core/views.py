from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Produto, Pedido
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        try:
            user = User.objects.create_user(
                username=usuario,
                password=senha,
                first_name = nome,
                last_name = sobrenome
            )
            user.save()
            return redirect('login')
        
        except:
            return redirect('cadastro')

def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=usuario, password=senha)
        if user:
            login(request, user)
            return redirect('painel')
        else:
            return redirect('login')

@login_required()
def painel(request):
    pedidos = Pedido.objects.filter(user=request.user)
    return render(request, 'painel.html', {'pedidos': pedidos})
    

def logout_user(request):
    logout(request)
    return redirect('login')

def pedido_form(request):
    produtos = Produto.objects.all()
    if request.method == 'GET':
        return render(request, 'pedido_form.html', {'produtos': produtos})
    
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        produto_id = request.POST.get('produto_id')
        produto = Produto.objects.get(id=produto_id)
        endereco = request.POST.get('endereco')
        observacao = request.POST.get('observacao')
        user = request.user

        try:
            pedido = Pedido(
                descricao = descricao,
                produto = produto,
                endereco = endereco,
                observacao = observacao,
                user = user
            )
            pedido.save()
            return redirect('painel')
        except:
            return redirect('pedidoform')