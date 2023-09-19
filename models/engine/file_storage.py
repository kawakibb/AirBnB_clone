import json
import os
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        if cls is None:
            return self.__objects
        return {key: value for key, value in self.__objects.items() if isinstance(value, cls)}

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(data, file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name, obj_id = key.split(".")
                    cls = eval(cls_name)
                    self.__objects[key] = cls(**value)
        else:
            return

    def close(self):
        self.reload()

if __name__ == "__main__":
    pass
