"""blog_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
import xadmin

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include,re_path
from django.conf.urls.static import static
from blog.views import *

xadmin.autodiscover()
# xversion模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    #url('admin/', admin.site.urls),
    # url('^$',include('blog.urls')
    url(r'^$', index, name='index'),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'xadmin/', xadmin.site.urls),
]

if settings.DEBUG:
    media_root = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if not settings.DEBUG:
#     static = [
#         re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),  # Debug为False时可以加载静态文件
#     ]
#     urlpatterns = urlpatterns + static