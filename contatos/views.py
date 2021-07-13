from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator


def index(request):
    contatos = Contato.objects.order_by('-id').filter(mostrar=True)
    paginator = Paginator(contatos, 1)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
