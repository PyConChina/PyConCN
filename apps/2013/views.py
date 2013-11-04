#coding=utf-8
from uliweb import expose

pagetitle = "PyCon2013China "
@expose('/2013')
class SiteView2013(object):
    @expose('')
    def index(self):
        return {"year":2013, "title":pagetitle}
    
    def about(self):
        return dict(page=dict(pagename='about', cndata=''),title=pagetitle)

    def schedulezh(self):
        return dict(page=dict(pagename='schedulezh', cndata=''),title=pagetitle, year=2012)

    def schedulesh(self):
        return dict(page=dict(pagename='schedulesh', cndata=''),title=pagetitle, year=2012)

    def collections(self):
        return dict(page=dict(pagename='collections', cndata=''),title=pagetitle)

    def registration(self):
        return dict(page=dict(pagename='registration', cndata=''),title=pagetitle)

    def sponsors(self):
        return dict(page=dict(pagename='sponsors', cndata=''),title=pagetitle)

    def volunteer(self):
        return dict(page=dict(pagename='volunteer', cndata=''),title=pagetitle)

    def speakers(self):
        from person import data
        return json(data)


