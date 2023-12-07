#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

''' '''




class BaseModel:
    '''parent class defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''initialize attribute'''
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        date_format)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        date_format)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''returns class name, id, dictionary'''
        return('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        '''returns string repr'''
        return (self.__str__())

    def save(self):
        '''save to serialization file'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''return dictionary'''
        dic = self.__dict__.copy()
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict
