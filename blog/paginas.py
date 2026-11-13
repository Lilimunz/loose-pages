from uuid import uuid4

from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Curtida, Post


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
    if "leitor" not in request.session:
        request.session["leitor"] = str(uuid4())
    return render(request, "blog/paginas/post.html", {
        "curtido": post.curtidas.filter(leitor=request.session["leitor"]).exists(),
        "post": post,
        "categoria": _categoria(request),
    })


@require_POST
def curtir(request, pk):
    post = get_object_or_404(_posts_publicados(), pk=pk)
    leitor = request.session.get("leitor")
    if leitor is None:
        return HttpResponseBadRequest("Reabra o post com os cookies ativados para curtir.")
    acao = request.POST.get("acao")
    if acao == "curtir":
        Curtida.objects.get_or_create(post=post, leitor=leitor)
    elif acao == "descurtir":
        post.curtidas.filter(leitor=leitor).delete()
    else:
        return HttpResponseBadRequest("Ação inválida.")
    return HttpResponseRedirect(reverse("post_detail", args=[pk],
                                        query={"categoria": _categoria(request)},
                                        fragment="curtida"))


def sobre(request):
    return render(request, "blog/paginas/sobre.html", {"categorias": Post.CATEGORIAS})
