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
        restart()


def restart(name='pycon'):
    run('sudo supervisorctl restart %s' % name)
