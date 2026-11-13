# Páginas soltas

[English](README.md) · **Português (Brasil)**

Acho que todo mundo já pensou em ser escritor, ou pelo menos já teve um dia em que precisava tirar da cabeça o que estava acontecendo e colocar em palavras. Fiz o *Páginas soltas* pra Alicia que sempre quis ter um blog e achava que fazer um era coisa de outro mundo. Agora ela tem um.

Quis fazer daqui a minha *Magic Shop*, como na música do BTS. Tem dia que eu entro pra escrever sobre um livro. Tem dia que é só pra anotar algo aleatório. Se você veio ler, puxa uma cadeira.

Bem-vindo ao meu mundo! (Quem joga de Viper no Valorant leu isso na voz dela, né?)



## Pelo blog

Na página inicial, dá pra ler os textos do mais recente pro mais antigo ou escolher entre **Programação**, **Leituras**, **Jogos** e **Pensamentos**. Quando você volta de um texto, a categoria que escolheu continua selecionada. Em **Sobre mim**, eu me apresento.

Escrevo e publico pelo admin do Django. Os rascunhos ficam privados, e a página da minha sequência de escrita pede uma conta com acesso de equipe.

## Quer criar o seu blog?

Se quiser construir um blog do zero, o [tutorial do Django Girls](https://tutorial.djangogirls.org/pt/) ensina passo a passo. O material também está no [GitHub do Django Girls](https://github.com/DjangoGirls/tutorial).

Se gostou deste aqui, pode clonar o *Páginas soltas* e usar como base pro seu. Um bom lugar pra começar é `blog/templates/blog/paginas/sobre.html`: troque a minha apresentação pela sua. Depois, publique seu primeiro texto.

### Rodar sua cópia no computador

O projeto usa Python, Django, SQLite, templates HTML e CSS. No terminal, rode:

```shell
git clone https://github.com/Lilimunz/loose-pages.git
cd loose-pages
python -m venv djangogirls_venv
```

No **Prompt de Comando do Windows**, ative com `djangogirls_venv\Scripts\activate.bat`. No **macOS ou Linux**, use `source djangogirls_venv/bin/activate`. Se o seu sistema usa `python3`, use esse nome para criar o ambiente.

```shell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abra [o blog local](http://127.0.0.1:8000/). O banco começa vazio. Para escrever o primeiro post, crie sua conta com `python manage.py createsuperuser` em outro terminal com o ambiente ativo. Depois entre no [admin](http://127.0.0.1:8000/admin/) e preencha a data de publicação quando quiser que o texto apareça no blog.