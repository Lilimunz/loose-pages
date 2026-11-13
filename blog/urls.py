from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path

from . import paginas, views

urlpatterns = [
    path("", paginas.post_list, name="post_list"),
    path("post/<int:pk>/", paginas.post_detail, name="post_detail"),
    path("sobre/", paginas.sobre, name="sobre"),
    path("streak/", staff_member_required(views.streak), name="streak"),
]
