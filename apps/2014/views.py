#coding=utf-8
from uliweb import expose
import json


pagetitle = "PyCon China 2014"


@expose('/2014')
class SiteView2014(object):
    @expose('')
    def index(self):
        return {"year": 2014, "title": pagetitle}

    def about(self):
        return dict(page=dict(pagename='about', cndata=''), title=pagetitle)

    def beijing(self):
        return dict(page=dict(pagename='beijing', cndata=''),
                    title=pagetitle, year=2014)

    def zhuhai(self):
        return dict(page=dict(pagename='zhuhai', cndata=''),
                    title=pagetitle, year=2014)

    def hangzhou(self):
        return dict(page=dict(pagename='zhangzhou', cndata=''),
                    title=pagetitle, year=2014)

    def shanghai(self):
        return dict(page=dict(pagename='shanghai', cndata=''),
                    title=pagetitle, year=2014)

    def collections(self):
        return dict(page=dict(pagename='collections', cndata=''),
                    title=pagetitle)

    def registration(self):
        return dict(page=dict(pagename='registration', cndata=''),
                    title=pagetitle)

    def sponsors(self):
        return dict(page=dict(pagename='sponsors', cndata=''),
                    title=pagetitle)

    def volunteer(self):
        return dict(page=dict(pagename='volunteer', cndata=''),
                    title=pagetitle)

    @expose('speakers.json')
    def speakers(self):
        from person import data
        return json(data)
