#!/usr/bin/python3
import json
from os.path import exists
from datetime import datetime
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """ Path to the JSON file """
    __file_path = "file.json"
    """ Dictionary to store objects by class name and id """
    __objects = {}

    def all(self):
        """ Return the dictionary of objects """
        return self.__objects

    def new(self, obj):
        """ Set a new object in the dictionary with key: 
            <class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serialize __objects to JSON and save it to the file """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ Deserialize JSON from the file 
            to __objects (if the file exists) """
        if exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
            for key, obj_data in obj_dict.items():
                class_name, obj_id = key.split(".")
                cls = class_name
                obj_data["created_at"] = datetime.strptime(obj_data["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
                obj_data["updated_at"] = datetime.strptime(obj_data["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
                self.__objects[key] = eval(cls)(**obj_data)
    def reload(self):
        try:
            with open(self.__file_path, mode='r') as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name = value['__class__']
                    if cls_name == 'BaseModel':
                        obj = BaseModel(**value)
                    elif cls_name == 'User':  # Handle User objects
                        obj = User(**value)
                    else:
                        continue
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
