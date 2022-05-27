from app import constants
from pydantic import BaseSettings


class Config(BaseSettings):
    authentication = constants.Authentication
    database = constants.Database


config = Config()
