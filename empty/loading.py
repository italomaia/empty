# -*- coding:utf-8 -*-

__all__ = [
    'load_schema', 'load_model', 'load_blueprint',
    'import_variable', 'import_module']


def import_module(bp, module):
    try:
        return __import__('.'.join(bp.split('.') + [module]))
    except ImportError:
        print("Module %s is not available for %s" % (module, bp))


def import_variable(bp, module, varname):
    path = '.'.join(bp.split('.') + [module])
    mod = __import__(path, fromlist=[varname])

    try:
        return getattr(mod, varname)
    except AttributeError:
        return None


def load_blueprint(bp, module='views', varname='app'):
    return import_variable(bp, module, varname)


def load_schema(path):
    bp, model = path.split('.')
    return import_variable(bp, 'schemas', '%sSchema' % model)


def load_model(path):
    bp, model = path.split('.')
    return import_variable(bp, 'models', model)
