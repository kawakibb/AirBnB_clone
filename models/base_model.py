#!/usr/bin/python3
"""This module defines a base class for all models in this project"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base class for all our classes"""

    def __init__(self, *args, **kwargs):
        """ deserialize and serialize a class """

        """initialize  if nothing is passed"""
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
            return

        """using Key words (deserialize)"""
        if 'id' not in kwargs:
            kwargs['id'] = str(uuid4())
        self.id = kwargs['id']

        for Key, val in kwargs.items():
            if Key == "__class_":
                continue
        if "created_at" in kwargs:
            self.created_at = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
        if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """overide string representation of self"""
        fmt = "[{}] ({}) {}"
        return fmt.format(
                type(self).__name__,
                self.id,
                self.__dict__)

    def save(self):
        """updates last variable update"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary"""
        temp = {**self.__dict__}
        temp['__class__'] = type(self).__name__
        temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        temp['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return temp

    @classmethod
    def all(cls):
        """Retrieve all current instances of classs"""
        return models.storage.find_all(cls.__name__)

    @classmethod
    def count(cls):
        """Get all current instances numbers of a class"""
        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def create(cls, *args, **kwargs):
        """Creates an Instance"""
        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def show(cls, instance_id):
        """Retrieve an instance"""
        return models.storage.find_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def destroy(cls, instance_id):
        """Deletes an instance"""
        return models.storage.delete_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def update(cls, instance_id, *args):
        """Updates an instance"""
        if not len(args):
            print("** attribute name missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(
                cls.__name__,
                instance_id,
                *arg
            )

