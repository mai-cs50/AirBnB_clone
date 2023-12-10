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
    @classmethod
    def setupcalss(self):
        ''' '''
        self.typing = console.HBNBCommand()

    @classmethod
    def teardownclass(self):
        ''' '''
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_console(self):
        ''' '''
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')

    def test_pep8_test_console(self):
        ''' '''
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["tasts/test_console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')

    def test_docstrings_in_console(self):
        ''' '''
        self.assertEqual(len(console.__dic__) >= 1)

    def test_docstrings_in_test_console(self):
        ''' '''
        self.assertEqual(len(self.__dic__) >= 1)

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand).prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=stringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHMNMCommand_help(unitest.TestCase):
    ''' '''

    def test_help_quit(self):
        h = "Quit Command"
        with patch("sys.stdout", new=stringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual("", output.getvalue().strip())

    def test_help_create(self):
        h = "create instant"
        with patch("sys.stdout", new=stringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual("", output.getvalue().strip())

    def test_help_EOF(self):
        h = "EOF signal to exit the program"
        with patch("sys.stdout", new=stringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual("", output.getvalue().strip())

    def test_help_show(self):
        h = "print string repr"
        with patch("sys.stdout", new=stringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual("", output.getvalue().strip())

    def test_help_destroy(self):
        h = "delet a class instant"
        with patch("sys.stdout", new=stringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual("", output.getvalue().strip())

    def test_help_all(self):
        h = "print all string"
        with patch("sys.stdout", new=stringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual("", output.getvalue().strip())

    def teat_help_count(self):
        h = "display count instant"
        with patch("sys.stdout", new=stringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help cout"))
            self.assertEqual("", output.getvalue().strip())

    def test_help_update(self):
        h = "update instant"
        with patch("sys.stdout", new=stringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual("", output.getvalue().strip())

    def test_help(self):
        h = "documented command"
        with patch("sys.stdout", new=stringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual("", output.getvalue().strip())


class TestHMNMCommand_exit(unitest.TestCase):
    ''' '''
