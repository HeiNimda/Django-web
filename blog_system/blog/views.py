# _*_ coding: utf-8 _*_

import logging

from django.shortcuts import render
from django.conf import settings


logger = logging.getLogger('blog.views')

def global_settings(request):
    return {
        'SITE_NAME' : settings.SITE_NAME,
        'NICK_NAME' : settings.NICK_NAME,
        'MY_WORK' : settings.MY_WORK,
        'MY_HOMETOWN' : settings.MY_HOMETOWN,
        'MY_EMAIL' : settings.MY_EMAIL,
        'SITE_DESC' : settings.SITE_DESC,
        'SITE_FOOTER': settings.SITE_FOOTER,
    }

def index(request):
    try:
        pass
    except Exception as e:
        logger.error(e)
    return render(request, 'index.html', locals())