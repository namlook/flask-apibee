==============
Flask-API
==============
.. currentmodule:: flaskext.api

Flask-API allow you to easily build and publish an API for your Flask applications. If you find bugs or want to support this extension you can find the source code `here`_.

.. _here: http://github.com/namlook/apibee

Installation
============
The installation is thanks to the Python Package Index and `pip`_ really simple::

   $ pip install Flask-API

If you only can use `easy_install` than use::

   $ easy_install Flask-API

.. _pip: http://pip.openplans.org/

Flask-API requires to run some packages (they will be installed automatically if they not already installed):

* apibee
* decorator

Building the API
================

Building your API is simple, you just have to import the `api` decorator and decorate your views::

    from flask import Flask, Blueprint, route
    from flaskext.api import api

    tasks = Blueprint('tasks', __name__, url_prefix='/tasks')

    @app.route('/new', methods=["GET", "POST"])
    @api(required=['title'], optional={"description":None})
    def new_task(\*\*args):
        task = db.Task()
        task.title = args['title']
        task.text = args['text']
        task.save()
        return task['_id']

This will return the created task id into the following json structure:

    {"status": "ok", "result": "123", "time": 0.00022578239440917969}


Using the Client
================

Now that the api is built, you can use the provided client to query it::

    >>> from flaskext.api import Client
    >>> api = Client('http://localhost:5000')
    >>> api.task.new(title="foo", description="bar")
    {"status": "ok", "result": "123", "time": 0.00022578239440917969}

