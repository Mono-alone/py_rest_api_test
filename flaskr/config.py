from pathlib import Path


class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{Path.home()}\\test.db'
