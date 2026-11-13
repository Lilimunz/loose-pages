from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(
        "categoria",
        max_length=20,
        choices=[
            ("programacao", "Programação"),
            ("leituras", "Leituras"),
            ("jogos", "Jogos"),
            ("pensamentos", "Pensamentos"),
        ],
        blank=True,
        default="",
    )
    CATEGORIAS = category.choices
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title    


class Curtida(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="curtidas")
    leitor = models.UUIDField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["post", "leitor"], name="uma_curtida_por_leitor"),
        ]
