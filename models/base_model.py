#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        # Initialize id with a unique UUID converted to string
        self.id = str(uuid.uuid4())
        # Initialize created_at with the current datetime
        self.created_at = datetime.now()
        # Initialize updated_at with the current datetime
        self.updated_at = datetime.now()

    def __str__(self):
        # Define a string representation for the object
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        # Update the updated_at attribute with the current datetime
        self.updated_at = datetime.now()

    def to_dict(self):
        # Create a dictionary representation of the object
        obj_dict = self.__dict__.copy()
        # Add the __class__ attribute with the class name
        obj_dict['__class__'] = self.__class__.__name__
        # Convert created_at and updated_at to ISO format strings
        obj_dict['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        obj_dict['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return obj_dict
