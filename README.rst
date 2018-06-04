Fortune Cookie
==============

Exam#2 Fortune Cookie

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Setup
^^^^^^^^^^^^^


Requirements
----------

* Python 3.6.5.
* Use of virtualenv is advised.


Virtualenv Wrapper
----------

* Install virtualenvwrapper::

  $ pip install virtualenvwrapper

* Create virtualenv, it'll auto activates upon success::

  $ mkvirtualenv exam2


Installation
----------

* Clone from this source::

  https://github.com/jrsinel/exam2-fortune-cookie.git

* Install necessary packages of the project::

  $ pip install -r requirements/local.txt

* Create DB::

  $ python manage.py migrate

* Supply initial data::

  $ python manage.py loaddata fortune_cookie/fixtures/initial_users.json
  $ python manage.py loaddata fortune_cookie/fixtures/initial_seed_fortunes.json

* Runserver::

  $ python manage.py runserver

* Check if it works, access::

  http://localhost:8000/

* To check the seed fortunes, go to::

  http://localhost:8000/admin/pool/seedfortune/


Initial Credentials
----------

username: admin

password: admin1234!

