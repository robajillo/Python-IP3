import os

class Config:
    

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
