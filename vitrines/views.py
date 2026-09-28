from django import forms
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Produto, Vitrine


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['name', 'description', 'category', 'price', 'image_url', 'partner_url', 'active']


class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'password1', 'password2')


def cadastro(request):
    form = CadastroForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'vitrines/cadastro.html', {'form': form})


def home(request):
    query = request.GET.get('q', '').strip()
    products = Produto.objects.filter(active=True).select_related('vitrine', 'vitrine__owner')
    if query:
        products = products.filter(name__icontains=query)
    return render(request, 'vitrines/home.html', {'products': products, 'query': query})


def vitrine_publica(request, slug):
    shop = get_object_or_404(Vitrine, slug=slug)
    return render(request, 'vitrines/vitrine.html', {'shop': shop, 'products': shop.produtos.filter(active=True)})


def institucional(request, page):
    pages = {
        'vitrines': ('Vitrines', 'Conheça vitrines e indicações de vendedores independentes.'),
        'como-funciona': ('Como funciona', 'Você encontra o produto, abre o link do parceiro e conclui a compra diretamente na loja escolhida.'),
        'suporte': ('Suporte e perguntas frequentes', 'Tire dúvidas sobre vitrines, links de afiliado e compras em parceiros.'),
        'termos': ('Termos de uso', 'A plataforma não vende produtos nem processa pagamentos. Cada parceiro é responsável pela sua venda.'),
    }
    title, body = pages[page]
    return render(request, 'vitrines/institucional.html', {'title': title, 'body': body, 'page': page})


@login_required
def dashboard(request):
    return render(request, 'vitrines/dashboard.html', {'shops': request.user.vitrines.all()})


@login_required
def produto_novo(request):
    shop = request.user.vitrines.first()
    if not shop:
        shop = Vitrine.objects.create(owner=request.user, name=f'Vitrine de {request.user.username}', slug=f'{request.user.username}-vitrine')
    form = ProdutoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        product = form.save(commit=False)
        product.vitrine = shop
        product.save()
        return redirect('dashboard')
    return render(request, 'vitrines/produto_form.html', {'form': form})
