#!/usr/bin/python3
"""City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.
    The name of the city.
    """

    state_id = ""
    name = ""
