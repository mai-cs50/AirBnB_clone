#!/usr/bin/python3
''' '''
import json
from models.base import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''storage engine'''
    __file_path = 'file.json'
    __objicts = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "PLace": Place, "City": City, "State": State}
    
    def all(self):
        ''' '''
        return self.__objects

    def new(self, obj):
        ''' '''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        ''' '''
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
            with open(self.__file_path, 'w', encoding='utf-8') as f:
                json.dump(obj_dict, f)

    def reload(self):
        ''' '''
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj

        except FileNotFounderError:
            pass
