========
News Crawler
========

:author: Mostafa Sadeghi
:date: 2019/05/04

News clawer provides search for some news websites in Iran


Getting Help
============

Please contact me for any question ( mostafasadeghi97@gmail.com )

Installation
=============
create a virtual environment to create a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages needed by this project.

virtualenv -p pyhton3 .env
--------------------------

activate the virtualenv

source .env/bin/activate
-----------------------

git clone https://github.com/mostafasadeghi97/news_crawl.git
------------------------------------------------------------

cd news_crawl
-------------

pip install -r requirements.txt
-------------------------------

python3 manage.py migrate
-------------------------

python3 manage.py runserver
---------------------------

in your browser go to localhost:8000
------------------------------------

