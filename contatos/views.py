from django.http.response import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required
CONTATOS_POR_PAGINA = 4

@login_required(redirect_field_name='login')
def index(request):
    
    contatos = Contato.objects.order_by('-id').filter(mostrar=True, usuario_agenda=request.user)
    paginator = Paginator(contatos, CONTATOS_POR_PAGINA)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

@login_required(redirect_field_name='login')
def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })

@login_required(redirect_field_name='login')
def busca(request):
    termo = request.GET.get('termo')
    
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'Campo de pesquisa vazio')
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')
    
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo),
        mostrar=True, usuario_agenda=request.user
        ).order_by('-id')
    if not contatos:
        messages.add_message(request, messages.WARNING, f'Nenhum contato encontrado para: {termo}')
        return redirect('index')
    
    
    paginator = Paginator(contatos, CONTATOS_POR_PAGINA)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })
