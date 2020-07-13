import unittest
from app.models import User
from os import urandom

class UserModelTest(unittest.TestCase):
    """
    Test class to test the behaviour of the user class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """

        self.new_user = User(username='cjjhvghxdf', password = 'potatopeel420')


    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)


    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password


    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('potatopeel420'))



    def tearDown(self):
        user = User.query.filter_by(username="cjjhvghxdf").first()
        if user:
            print("found")