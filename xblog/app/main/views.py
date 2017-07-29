#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from . import main
# from flask import render_template, url_for
#
#
# @main.route('/home')
# def home():
#     """
#     Home Page
#     :return:
#     """
#     return render_template("base.html", title="Welcome")
#
#
# @main.route('/index')
# def index2():
#     """
#     Welcome Index
#     :return:
#     """
#     import random
#     img_no = random.randint(1, 13)
#     background_img = "background{0}".format(img_no)
#
#     return render_template("welcome.html", title="Welcome", background_img=background_img)


from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db
from ..models import User
from flask.ext.login import login_required


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # ...
        return redirect(url_for('.index'))

    return render_template('index.html',
        form=form,
        name=session.get('name'),
        known=session.get('known', False),
        current_time=datetime.utcnow())

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

