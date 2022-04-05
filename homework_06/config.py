from os import getenv


SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+pg8000://app:password@localhost/horoscope",
)


class Config:
    DEBUG = False
    TESTING = False
    ENV = "development"

    SECRET_KEY = "\x0b\xe2\x8d\xee\xb60I\xe5f\xe9v\x88\x18L\x97\x17"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    ENV = "production"
    SECRET_KEY = "\xa9q\x1c\x0e>f^3,\xf4$w\x8e\x0e\xcdu"

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
