#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
import datetime


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}


    def classes(self):
        """ Returns dict of classes """

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        return {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            return {key: self.__objects[key]
                    for key in self.__objects
                    if self.__objects[key].__class__ == cls}
        return FileStorage.__objects

    def new(self, obj):
          temp[key] = val.to_dict()
          json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
    def reload(self):
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                       self.all()[key] = classes[val['__class__']](**val)
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj in self.__objects.values():
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects.pop(key, None)
        elif obj is None:
            return

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
