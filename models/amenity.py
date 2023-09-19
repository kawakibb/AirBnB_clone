#!/usr/bin/python3

""" Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.
    The name of the amenity.
    """

    name = ""
