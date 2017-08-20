class Ext:
    def __init__(self, app=None, **kwargs):
        self.options = dict()

        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        self.options.update(kwargs)
        self.app = app

        if app is not None:
            if not hasattr(app, 'extensions'):
                app.extensions = {} # pragma: no cover
            app.extensions['ext'] = self


ext = Ext()


def ext_init_kwargs():
    return dict(test=True)
