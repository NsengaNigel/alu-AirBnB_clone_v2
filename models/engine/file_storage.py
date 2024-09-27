#!/usr/bin/python3
""" Module for FileStorage class, which handles storage of object data in JSON format. """

import json
from models.base_model import BaseModel

class FileStorage:
    """ This class manages storage of model instances in JSON format. """
    
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ 
        Returns a dictionary of all objects or objects of a specific class.

        Args:
            cls (type): The class to filter objects by. If None, returns all objects.

        Returns:
            dict: A dictionary of objects.
        """
        if cls is None:
            return FileStorage.__objects
        return {key: obj for key, obj in FileStorage.__objects.items() if isinstance(obj, cls)}

    def new(self, obj):
        """ 
        Adds a new object to the storage.

        Args:
            obj (BaseModel): The object to add.
        """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """ 
        Saves the current state of objects to a JSON file.
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, f)

    def delete(self, obj=None):
        """ 
        Deletes an object from storage.

        Args:
            obj (BaseModel, optional): The object to delete. If None, does nothing.
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
    def reload(self):
        """ 
        Loads the state of objects from the JSON file.
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = key.split('.')[0]
                    cls = globals().get(cls_name)
                    if cls:
                        self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
