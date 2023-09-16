#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Constructor for BaseModel """
        if kwargs:
            """ If kwargs (dictionary representation) is provided,
                initialize attributes from it """
            for key, value in kwargs.items():
                if key != '__class__':
                    """ Skip setting '__class__' attribute from kwargs """
                    if key == 'created_at' or key == 'updated_at':
                        """ Convert 'created_at' and 'updated_at'
                            strings to datetime objects """
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
            if 'id' not in kwargs:
                """ Generate a unique id if not provided in kwargs """
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                """ Set 'created_at' to the current
                datetime if not provided in kwargs """
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                """ Set 'updated_at' to the current
                    datetime if not provided in kwargs """
                self.updated_at = datetime.now()
        else:
            """ If kwargs is empty, create a new instance
                with random id and current datetime """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Define a string representation for the object """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update the updated_at attribute with the current datetime """
        self.updated_at = datetime.now()
        """ Call save method of storage to save the object to the JSON file """
        storage.save()

    def to_dict(self):
        """ Create a dictionary representation of the object """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        obj_dict['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return obj_dict
