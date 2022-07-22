#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
import os
import datetime


class FileStorage:
    """
    class manages imported hbnb models in a JSON format
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Return objects of a dictionary.
        """
        if cls is not None:
            if isinstance(cls, str):
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if isinstance(v, cls):
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        """new list init"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """JSON Serializes the file"""
        odict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self):
        """Deserializing the translation catastrophy!"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        try:
            temp = {}
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass
