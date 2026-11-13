# Páginas soltas

**English** · [Português (Brasil)](README.pt-BR.md)

I think everyone’s wanted to be a writer at some point, or at least had a day when they needed to get something out of their head and put it into words. I made *Páginas soltas* (“Loose Pages”) for the Alicia who always wanted a blog and thought building one was beyond her. Now she has one.

I wanted this to be my own *Magic Shop*, like the BTS song. Some days I come here to write about a book. Other days I jot down a thought, share something I’ve been playing, or record a small discovery from everyday life. This is a place for whatever catches my attention, without needing to fit into one subject. If you’re here to read, pull up a chair.

Welcome to my world! (If you play Viper in Valorant, you probably heard that in her voice.)



## Around the blog

The blog is written in Brazilian Portuguese. You can browse posts from newest to oldest or pick a category: **Programação** (coding), **Leituras** (books), **Jogos** (games), or **Pensamentos** (thoughts). When you return from a post, your category stays selected. You can find a little more about me under **Sobre mim**.

I write and publish through the Django admin. Drafts stay private, and my writing streak is only visible to signed-in staff.

## Want to make your own blog?

If you’d like to build a blog from scratch, the [Django Girls tutorial](https://tutorial.djangogirls.org/en/) walks you through it. You can also find the [tutorial on GitHub](https://github.com/DjangoGirls/tutorial).

If you like this one, feel free to clone *Páginas soltas* and use it as a starting point for yours. Try opening `blog/templates/blog/paginas/sobre.html` and replacing my introduction with your own. Then write your first post.

### Run your copy locally

The project uses Python, Django, SQLite, HTML templates, and CSS. In your terminal, run the following commands.

```shell
git clone https://github.com/Lilimunz/loose-pages.git
cd loose-pages
python -m venv djangogirls_venv
```

In **Windows Command Prompt**, activate it with `djangogirls_venv\Scripts\activate.bat`. On **macOS or Linux**, use `source djangogirls_venv/bin/activate`. If your system uses `python3`, use that name to create the environment.

```shell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open [the blog locally](http://127.0.0.1:8000/). The database starts empty. To write your first post, run `python manage.py createsuperuser` in a second terminal with the environment active. Then sign in to the [admin](http://127.0.0.1:8000/admin/) and set a publication date when you’re ready for the post to appear.
