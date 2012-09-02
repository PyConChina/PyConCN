#coding=utf-8
from __future__ import with_statement
from uliweb import expose
#from uliweb.orm import get_model
from uliweb import request

@expose('/2011')
class siteView(object):
    @expose('')
    def index(self):
        return {"year":2011, "title":"PyCon China 2011"}
    
    def about(self):
        
        return dict(page=dict(pagename='about',cndata='')) 
    
    def schedule(self):
        return dict(page=dict(pagename='schedule',cndata=''))
    
    def collections(self):
        return dict(page=dict(pagename='collections',cndata=''))    

    def registration(self):
        return dict(page=dict(pagename='registration',cndata=''))
        
    def sponsors(self):
        return dict(page=dict(pagename='sponsors',cndata=''))

    def volunteer(self):
        return dict(page=dict(pagename='volunteer',cndata=''))