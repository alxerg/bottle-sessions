import os
from gevent import monkey
monkey.patch_all()
monkey.patch_socket()

import bottle as web
from bottle import *
from bottlesessions import get_current_session, SessionMiddleware
from bottle.ext.sqlalchemy import SQLAlchemyPlugin
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

import datetime
import memcache
import time

#--- you should generate random cookie key---
COOKIE_KEY = '457rxK8ytkKiqkfqwfoiQS@kaJSFOo8h'

#--- Memcached setup ---
mc = memcache.Client(['127.0.0.1:11211'], debug=1)

#--- SQLA setup ---
engine = create_engine('mysql://user:password@localhost/session_database?charset=utf8&use_unicode=0', echo=False,pool_recycle=3600)
connection = engine.connect()
SASessionClass = sessionmaker(bind=engine)
install(SQLAlchemyPlugin(engine, declarative_base().metadata, create=True))

#--- Bottle init ---
app = web.default_app()

#--- Session setup ---
BottleApp = SessionMiddleware(app=app, sa_session_class=SASessionClass, mc_client=mc, cookie_key=COOKIE_KEY)

@web.get('/')
def index():
    session = get_current_session()
    session['dummy'] = True
    session['userid'] = 'stkim1'
    return '<b>It works</b>!'

port = int(os.environ.get("PORT", 8080))
web.debug(True)
web.run(app=BottleApp, reloader = True, host='0.0.0.0', port=port, server='gevent')