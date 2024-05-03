import unittest
from slowo import Slowo_1
import slowo

ocena = Slowo_1(word='ocena')
real = Slowo_1(word='real')
oabcell = Slowo_1(word='oabcell')


class MyTestCase(unittest.TestCase):
    def test_incorrect_input(self):
        self.assertRaises(ValueError, slowo.Slowo_1, 'qwrtp')
        self.assertRaises(ValueError, slowo.Slowo_1, 'ttttt')


# ocena.possibilites
# assert ocena.possibilites == {'o-cena', 'o-ce-na', 'o-cen-a', 'oc-ena', 'oc-e-na', 'ocen-a', 'oce-na', 'ocen-a', 'ocen-a'}
