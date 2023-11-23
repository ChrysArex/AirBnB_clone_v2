#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects

        try:
            if isinstance(cls, str):
                target_class = globals().get(cls)
                if issubclass(target_class, BaseModel):
                    class_dict = {
                        k: v for k, v in self.__objects.items()
                        if isinstance(v, target_class)
                    }
                    return class_dict
        except (TypeError, AttributeError):
            pass

        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
        }
        try:
            if exists(self.__file_path):
                with open(self.__file_path, 'r') as f:
                    temp = json.load(f)
                    for key, val in temp.items():
                        class_name = val['__class__']
                        if class_name in classes:
                            self.__objects[key] = classes[class_name](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes the specified object from the internal storage if it exists.
        """
        if obj is None:
            return

        try:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del FileStorage.__objects[key]
        except (AttributeError, KeyError):
            pass
