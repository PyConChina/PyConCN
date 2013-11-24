#coding=utf-8
from uliweb import expose
import json


pagetitle = "PyCon China 2013"


@expose('/2013')
class SiteView2013(object):
    @expose('')
    def index(self):
        return {"year": 2013, "title": pagetitle}

    def about(self):
        return dict(page=dict(pagename='about', cndata=''), title=pagetitle)

    def beijing(self):
        return dict(page=dict(pagename='beijing', cndata=''),
                    title=pagetitle, year=2013)

    def zhuhai(self):
        return dict(page=dict(pagename='zhuhai', cndata=''),
                    title=pagetitle, year=2013)

    def hangzhou(self):
        return dict(page=dict(pagename='zhangzhou', cndata=''),
                    title=pagetitle, year=2013)

    def shanghai(self):
        return dict(page=dict(pagename='shanghai', cndata=''),
                    title=pagetitle, year=2013)

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

    def speakers(self):
        from person import data
        return json(data)
