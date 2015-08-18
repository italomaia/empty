from empty import app_factory


class Config:
    pass


app = app_factory(Config, 'myapp')
