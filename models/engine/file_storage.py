#!/usr/bin/python3
import json


class FileStorage:
    """ Private class attributes """
    __file_path = "file.json"
    __objects = {}

    """ Public instance methods """
    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """ Deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists) """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    class_name = class_name.strip()
                    obj_id = obj_id.strip()
                    """ Convert 'created_at' and 'updated_at' strings to datetime objects """
                    value['created_at'] = datetime.strptime(value['created_at'],
                                                            '%Y-%m-%dT%H:%M:%S.%f')
                    value['updated_at'] = datetime.strptime(value['updated_at'],
                                                            '%Y-%m-%dT%H:%M:%S.%f')
                    """ Create objects and store them in __objects """
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
