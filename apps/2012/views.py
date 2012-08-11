#coding=utf-8
from uliweb import expose


@expose('/2012/')
def index():
    return {}


@expose('/2012')
class SiteView(object):

    def about(self):
        return dict(page=dict(pagename='about', cndata=''))

    def schedule(self):
        return dict(page=dict(pagename='schedule', cndata=''))

    def collections(self):
        return dict(page=dict(pagename='collections', cndata=''))

    def registration(self):
        return dict(page=dict(pagename='registration', cndata=''))

    def sponsors(self):
        return dict(page=dict(pagename='sponsors', cndata=''))

    def volunteer(self):
        return dict(page=dict(pagename='volunteer', cndata=''))
