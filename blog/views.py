from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from collections import Counter
from datetime import timedelta

from .models import Post


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.localdate()
    ).order_by("-published_date", "-pk")

    return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(
        Post,
        pk=pk,
        published_date__lte=timezone.localdate(),
    )
    return render(request, "blog/post_detail.html", {"post": post})

def _nivel(qtd):
    """Quanto mais posts no dia, mais escuro o quadradinho (0 a 4)."""
    if qtd == 0:
        return 0
    if qtd == 1:
        return 1
    if qtd == 2:
        return 2
    if qtd <= 4:
        return 3
    return 4


def streak(request):
    hoje = timezone.localdate()
    posts = Post.objects.filter(published_date__lte=hoje)
    por_dia = Counter(post.published_date for post in posts)

    # Últimas 53 semanas, começando num domingo
    inicio = hoje - timedelta(days=52 * 7 + (hoje.weekday() + 1) % 7)
    semanas, semana = [], []
    dia = inicio
    while dia <= hoje:
        qtd = por_dia.get(dia, 0)
        semana.append({"data": dia, "qtd": qtd, "nivel": _nivel(qtd)})
        if len(semana) == 7:
            semanas.append(semana)
            semana = []
        dia += timedelta(days=1)
    if semana:
        semanas.append(semana)

    # Sequência atual (conta a partir de hoje, ou de ontem se hoje ainda não postou)
    atual = 0
    d = hoje if por_dia.get(hoje) else hoje - timedelta(days=1)
    while por_dia.get(d):
        atual += 1
        d -= timedelta(days=1)

    # Maior sequência de todos os tempos
    maior, seguidos, anterior = 0, 0, None
    for d in sorted(por_dia):
        seguidos = seguidos + 1 if anterior and d - anterior == timedelta(days=1) else 1
        maior = max(maior, seguidos)
        anterior = d

    totais = Counter(p.category for p in posts)
    categorias = [
        {"slug": slug, "nome": nome, "total": totais.get(slug, 0)}
        for slug, nome in Post._meta.get_field("category").choices
    ]

    return render(request, "blog/streak.html", {
        "semanas": semanas,
        "streak_atual": atual,
        "maior_streak": maior,
        "total_posts": sum(por_dia.values()),
        "categorias": categorias,
    })
