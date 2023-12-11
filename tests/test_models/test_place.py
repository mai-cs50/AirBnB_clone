#!/usr/bin/python4
'''Define unittests'''
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    ''' '''

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(Place.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(Place.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(Place.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(Place.last_name))

    def test_two_places_unique_ids(self):
        place2 = Place()
        place3 = Place()
        self.assertNotEqual(place2.id, place2.id)

    def test_two_places_different_created_at(self):
        place2 = Place()
        sleep(1.05)
        place3 = Place()
        self.assertLess(place2.created_at, place2.created_at)

    def test_two_places_different_updated_at(self):
        place2 = Place()
        sleep(1.05)
        place3 = Place()
        self.assertLess(place2.updated_at, place2.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date.repr = repr(date)
        place = Place()
        place.id = "123457"
        place.created_at = place.created_at = date
        placestr = place.__str__()
        self.assertIn("[Place] (123457)", placestr)
        self.assertIn("'id': '123457'", placestr)
        self.assertIn("'created_at': " + date.repr, placestr)
        self.assertIn("'updated_at': " + date.repr, placestr)

    def test_args_unused(self):
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date = datetime.today()
        date_iso = data.isoformat()
        place = Place(id="346", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(place.id, "346")
        self.assertEqual(place.created_at, date)
        self.assertEqual(place.updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    ''' '''
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        place = Place()
        sleep(1.05)
        first_updated_at = place.updated_at
        place.save()
        self.assertLess(first_updated_at, place.updated_at)

    def test_two_saves(self):
        place = Place()
        sleep(1.05)
        first_updated_at = place.updated_at
        place.save()
        second_updated_at = place.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(1.05)
        place.save()
        self.assertLess(second_updated_at, place.updated_at)

    def test_save_with_arg(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.save(None)

    def test_save_updates_file(self):
        place = Place()
        place.save()
        placeid = "Place." + place.id
        with open("file.json", "r") as f:
            self.assertIn(placeid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    ''' '''
    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        place = Place()
        self.assertIn("id", place.to_dict())
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())
        self.assertIn("__class__", place.to_dict())

    def test_to_dict_contains_added_attributes(self):
        place = Place()
        place.middle_name = "Holberton"
        place.my_number = 99
        self.assertEqual("Holberton", place.middle_dict())
        self.assertIn("my_number", place.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(str, type(place_dict["id"]))
        self.assertEqual(str, type(place_dict["created_at"]))
        self.assertEqual(str, type(place_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        place = Place()
        place.id = "123457"
        place.crested_at = place.updated_at = date
        tdict = {
                'id': '123457'
                '__class__': 'Place',
                'created_at': date.isoformat(),
                'updated_at': date.isoformat()
            }
        self.assertDictEqual(place.to_dict(), tdict)

    def test_contrast_to_dict_under_dict(self):
        place = Place()
        self.assertNotEqual(place.to_dict(), place.__dict__)

    def test_to_dict_with_arg(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.to_dict(None)


if __name__ == '__main__':
    unittest.main()
