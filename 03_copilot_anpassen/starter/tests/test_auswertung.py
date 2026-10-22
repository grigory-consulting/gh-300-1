import unittest

from lager.artikel import Artikel
from lager.auswertung import bestellmenge, unter_mindestbestand


class TestAuswertung(unittest.TestCase):
    def setUp(self):
        self.artikel = [
            Artikel("KT-1100", "Kette 11-fach", "C1", 3, 5, 12),
            Artikel("BR-1043", "Scheibenbremsbeläge gesintert", "A1", 4, 8, 24),
            Artikel("KT-0900", "Kette 9-fach", "C1", 9, 5, 12),
        ]

    def test_unter_mindestbestand(self):
        knapp = unter_mindestbestand(self.artikel)
        self.assertEqual([a.nummer for a in knapp], ["BR-1043", "KT-1100"])

    def test_bestellmenge(self):
        self.assertEqual(bestellmenge(self.artikel[0]), 9)
        self.assertEqual(bestellmenge(self.artikel[2]), 0)
