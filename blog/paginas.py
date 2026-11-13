from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post


def _posts_publicados():
    # O DateField do projeto original aceita um datetime e usa a data local.
    # Na versão com DateTimeField, o mesmo limite respeita a hora agendada.
    return Post.objects.filter(published_date__lte=timezone.now())


def _categoria(request):
    valor = request.GET.get("categoria")
    return valor if valor in dict(Post.CATEGORIAS) else "todas"


def post_list(request):
    categoria = _categoria(request)
    posts = _posts_publicados().order_by("-published_date", "-pk")
    if categoria != "todas":
        posts = posts.filter(category=categoria)
    return render(request, "blog/paginas/inicio.html", {
        "posts": posts,
        "categoria": categoria,
        "categorias": Post.CATEGORIAS,
    })


def post_detail(request, pk):
    post = get_object_or_404(_posts_publicados(), pk=pk)
    return render(request, "blog/paginas/post.html", {
        "post": post,
        "categoria": _categoria(request),
    })


def sobre(request):
    return render(request, "blog/paginas/sobre.html", {"categorias": Post.CATEGORIAS})
