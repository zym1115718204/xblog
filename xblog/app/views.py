#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
from flask import render_template, url_for


@app.route('/test')
def test():
    return "Hello World!"


# @app.route('/')
# def disabled_index():
#     return render_template("welcome.html", title="Welcome")


@app.route('/home')
def home():
    return render_template("base.html", title="Welcome")


@app.route('/')
def index():
    return render_template("welcome.html", title="Welcome")

