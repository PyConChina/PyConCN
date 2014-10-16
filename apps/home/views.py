#coding=utf-8
from uliweb import expose

@expose('/uli')
def index():
    return redirect('/uli/2013')
