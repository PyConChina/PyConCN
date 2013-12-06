# -*- coding: utf-8 -*-
from fabric.api import (
    run,
    env,
    cd
)

env.hosts = ['cn.pycon.org']
env.port = 9022
env.user = 'pycon'
code_dir = '/opt/app/PyConCN'


def deploy():
    with cd(code_dir):
        run('git pull')
        run('bin/uliweb exportstatic static')
        run('/opt/sbin/_package_linux_amd64/qrsync -skipsym /opt/sbin/7niu-conf.json')
        restart()


def restart(name='pycon'):
    run('sudo supervisorctl restart %s' % name)
