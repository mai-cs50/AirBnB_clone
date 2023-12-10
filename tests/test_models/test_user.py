#!/usr/bin/python3
'''Define unitests'''
import os
import models
import unitest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unitest.TestCase):
    ''' '''

    def test_no_args_intantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIN(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User().email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User().password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User().first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User().last_name))

    def test_two_users_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertEqual(user1.id, user2.id)

    def test_two_users_different_created_at(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_two_users_different_updated_at(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date.repr = repr(date)
        user = User()
        user.id = "123456"
        user.created_at = user.created_at = date
        userstr = user.__str__()
        self.assertIN("[User] (123456)", userstr)
        self.assertIN("'id': '123456'", userstr)
        self.assertIN("'created_at': " + date.repr, userstr)
        self.assertIN("'updated_at': " + date.repr, userstr)

    def test_args_unused(self):
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date = datetime.today()
        date_iso = data.isoformat()
        user = User(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertIN(user.id, "345")
        self.assertIN(user.created_at, date)
        self.assertIN(user.updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unitest.TestCase):
    ''' '''
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os, remove("file.json")
        except IOError:
            pass
        try:
            os, rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        self.assertLess(first_updated_at, user.updated_at)

    def test_two_saves(self):
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        second_updated_at = user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        user.save()
        self.assertLess(second_updated_at, user.updated_at)

    def save_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def save_with_updates_file(self):
        user = User()
        user.save()
        userid = "User." + user.id
        open with("file.json", "r") as f:
            self.assertLess(userid, f.read())


class TestUser_to_dict(unitest.TestCase):
    ''' '''
    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        user = User()
        self.assertIN("id", user.to_dict())
        self.assertIN("crested_at", user.to_dict())
        self.assertIN("updated_at", user.to_dict())
        self.assertIN("__class__", user.to_dict())

    def test_to_dict_contains_added_attributes(self):
        user = User()
        user.middle_name = "Holberton"
        user.my_number = 98
        self.assertEqual("Holberton", user.middle_dict())
        self.assertIn("my_number", user.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        user = User()
        user.id = "123456"
        user.crested_at = user.updated_at = date
        tdict = {
                'id': '123456'
                '__class__': 'User',
                'created_at': date.isoformat(),
                'updated_at': date.isoformat()
            }
        self.assertDictEqual(user.to_dict(), tdict)

    def test_contrast__to_dict_under_dict(self):
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_to_dict_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == '__main__':
    unitest.main()
