import xadmin

from blog.models import *

class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

#指定哪个地方使用ueditor
class ArticleAdmin(object):
    style_fields = {'content': 'ueditor'}

class CommentAdmin(object):
    style_fields = {'content': 'ueditor'}

xadmin.site.unregister(User)
xadmin.site.register(User)
xadmin.site.register(Ad)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Tag)
xadmin.site.register(Category)
xadmin.site.register(Comment,CommentAdmin)
xadmin.site.register(Links)
