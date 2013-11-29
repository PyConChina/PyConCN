#coding=utf-8
from __future__ import with_statement
from uliweb import expose
#from uliweb.orm import get_model
from uliweb import request

pagetitle = "PyCon China 2011"
@expose('/2011')
class siteView(object):
    @expose('')
    def index(self):
        return {"year":2011, "title":"PyCon China 2011"}
    
    def about(self):
        return dict(page=dict(pagename='about',cndata=''),title=pagetitle) 
    
    def schedule(self):
        return dict(page=dict(pagename='schedule',cndata=''),title=pagetitle)
    
    def collections(self):
        return dict(page=dict(pagename='collections',cndata=''),title=pagetitle)    

    def registration(self):
        return dict(page=dict(pagename='registration',cndata=''),title=pagetitle)
        
    def sponsors(self):
        return dict(page=dict(pagename='sponsors',cndata=''),title=pagetitle)

    def volunteer(self):
        return dict(page=dict(pagename='volunteer',cndata=''),title=pagetitle)