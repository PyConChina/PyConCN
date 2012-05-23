def prepare_default_env(sender, env):
    from uliweb.i18n import gettext_lazy
    env['_'] = gettext_lazy
