#!/usr/bin/python3
'''tested with unit tests'''
import unittest
import console
import os
import pep8
import sys
import json
from models import storage
from console import HBNBCommand
from unittest.mock import patch
from models.engine.file_storage import FileStorage

class TestHBNBCommand_prompting(unittest.TestCase):
    ''' '''
