from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles

from lnbits.db import Database
from lnbits.helpers import template_renderer

db = Database('ext_jitsi')

jitsi_ext = APIRouter(
    prefix = '/jitsi', 
    tags = ['jitsi']
)

jitsi_static_files = [
         {
             'path': '/jitsi/static',
             'app' : StaticFiles(directory = 'lnbits/extensions/jitsi/static'),
             'name': 'jitsi_static',
             }
         ]

def jitsi_renderer():
    return template_renderer(['lnbits/extensions/jitsi/templates'])


from .views_api import *  # noqa
from .views import *  # noqa
