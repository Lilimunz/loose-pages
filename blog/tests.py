from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Post


class CurtidaTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(author=get_user_model().objects.create(username="alicia"),
                                        title="Um post", published_date=timezone.localdate())
        self.detail = reverse("post_detail", args=[self.post.pk])
        self.url = reverse("curtir", args=[self.post.pk]) + "?categoria=jogos"

    def test_curtir_e_descurtir_por_sessao(self):
        for cliente in (self.client, Client()):
            self.assertContains(cliente.get(self.detail), 'aria-pressed="false"')
            for _ in range(2):
                resposta = cliente.post(self.url, {"acao": "curtir"}, follow=True)
                self.assertContains(resposta, 'aria-pressed="true"')
                self.assertIn("?categoria=jogos#curtida", resposta.redirect_chain[0][0])
        self.assertEqual(self.post.curtidas.count(), 2)
        for _ in range(2):
            resposta = self.client.post(self.url, {"acao": "descurtir"}, follow=True)
            self.assertContains(resposta, 'aria-pressed="false"')
        self.assertEqual(self.post.curtidas.count(), 1)

    def test_rascunho_e_metodo_get(self):
        self.assertEqual(self.client.get(self.url).status_code, 405)
        self.post.published_date = None
        self.post.save()
        self.assertEqual(self.client.post(self.url, {"acao": "curtir"}).status_code, 404)
