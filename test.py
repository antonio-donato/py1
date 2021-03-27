import asta
from unittest.mock import patch
import unittest


class TestAll(unittest.TestCase):
    def test_mail1(self):
        self.assertFalse(asta.email_check("doannt"))

    def test_mail2(self):
        self.assertFalse(asta.email_check("donant.it"))

    def test_mail3(self):
        self.assertFalse(asta.email_check("donant@donant"))

    def test_mail4(self):
        self.assertTrue(asta.email_check("donant@donant.it"))

    def test_duplicati_email_in_lista(self):
        #avoid the same email in the list




if __name__ == '__main__':
    unittest.main()
