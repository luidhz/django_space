from django.shortcuts import render, get_object_or_404, redirect

from galeria.models import Fotografia

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})

def filtrar_por_tag(request, tag_nome):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    # Filtra as fotografias que estão publicadas E que correspondem à tag
    # Importante: Substitua 'tag' (em negrito abaixo) pelo nome exato do campo no seu models.py 
    # (ex: 'categoria', 'tipo') que armazena os valores como "Nebulosa", "Estrela", etc.
    fotografias_filtradas = Fotografia.objects.order_by("data_fotografia").filter(
        publicada=True, 
        categoria=tag_nome # <-- Corrigido para 'categoria' (Exemplo)
    )

    contexto = {
        "cards": fotografias_filtradas,
        "tag_selecionada": tag_nome, # Adicional: para saber qual tag está ativa no template
    }

    return render(request, 'galeria/index.html', contexto)