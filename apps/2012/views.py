#coding=utf-8
from uliweb import expose


@expose('/2012')
class SiteView2012(object):
    @expose('')
    def index(self):
        return {"year":2012, "title":"PyCon China 2012"}
    
    def about(self):
        return dict(page=dict(pagename='about', cndata=''))

    def schedulebj(self):
        return dict(page=dict(pagename='schedulebj', cndata=''))

    def schedulesh(self):
        return dict(page=dict(pagename='schedulesh', cndata=''))

    def collections(self):
        return dict(page=dict(pagename='collections', cndata=''))

    def registration(self):
        return dict(page=dict(pagename='registration', cndata=''))

    def sponsors(self):
        return dict(page=dict(pagename='sponsors', cndata=''))

    def volunteer(self):
        return dict(page=dict(pagename='volunteer', cndata=''))
