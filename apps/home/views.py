#coding=utf-8
from uliweb import expose

@expose('/')
def index():
    return redirect('/2012')
