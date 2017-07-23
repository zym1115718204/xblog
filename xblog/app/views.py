#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
# from app.models import Post
from flask import render_template, url_for


@app.route('/home')
def home():
    """
    Home Page
    :return:
    """
    return render_template("base.html", title="Welcome")


@app.route('/')
def index():
    """
    Welcome Index
    :return:
    """
    import random
    img_no = random.randint(1, 14)
    background_img = "background{0}".format(img_no)

    return render_template("welcome.html", title="Welcome", background_img=background_img)


# @app.route('/home')
# def home():
#     posts = Post.objects.all()
#     return render_template('post.html', title="Home", posts=posts)
#

# @app.route('/post/<string:title>')
# def read_more(title):
#     post = Post.objects.get_or_404(title=title)
#     return render_template('read_more.html', title="Post", post=post)
#
#
# @app.route('/archive')
# def archive():
#     posts = Post.objects.all()
#     return render_template('archive.html', title='Archive', posts=posts)

