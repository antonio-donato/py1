import asta
from unittest.mock import patch
import unittest
import rounding_ITA


class TestAll(unittest.TestCase):
    def test_mail1(self):
        self.assertFalse(asta.email_check("doannt"))

    def test_mail2(self):
        self.assertFalse(asta.email_check("donant.it"))

    def test_mail3(self):
        self.assertFalse(asta.email_check("donant@donant"))

    def test_mail4(self):
        self.assertTrue(asta.email_check("donant@donant.it"))

    # avoid the same email in the list
    def test_duplicati_email_in_lista(self):
        self.assertTrue(
            asta.search_email_in_list([["donant@gmail.com", 10], ["donant@outlook.com", 20]], "donant@gmail.com"))

    def test_media_offerte(self):
        lista = [("donant@gmail.com", 10), ("lucapicci@gmail.com", 30), ("marifu@gmail.com", 30),
                 ("donant@outlook.com", 50)]
        self.assertEqual(asta.mediaOfferte(lista), 30)

    def test_min(self):
        lista = [("donant@gmail.com", 100), ("lucapicci@gmail.com", 30), ("marifu@gmail.com", 60),
                 ("donant@outlook.com", 50)]
        minimo = asta.minimo(lista)
        self.assertEqual(minimo[1], 30)

    def test_max(self):
        lista = [("donant@gmail.com", 100), ("lucapicci@gmail.com", 30), ("marifu@gmail.com", 60),
                 ("donant@outlook.com", 50)]
        massimo = asta.massimo(lista)
        self.assertEqual(massimo[1], 100)


class TestArrotondamento(unittest.TestCase):

    def test_arrotonda1(self):
        self.assertTrue((rounding_ITA.rounding(10.37) == 10.35))

    def test_arrotonda2(self):
        self.assertTrue((rounding_ITA.rounding(10.31) == 10.3))

    def test_arrotonda3(self):
        self.assertTrue((rounding_ITA.rounding(10.39) == 10.4))


if __name__ == '__main__':
    unittest.main()
