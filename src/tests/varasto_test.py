import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_konstruktori_nollaa_varaston(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_konstruktori_nollaa_saldon(self):
        self.varasto = Varasto(1,-1)
        self.assertAlmostEqual(self.varasto.saldo,0)

    def test_konstruktori_hukkaa_ylimaaraisen(self):
        self.varasto = Varasto(10,20)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_neg_maaran_lisays(self):
        apu = self.varasto.saldo
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(apu,self.varasto.saldo)
    
    def test_lisataan_liikaa(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus+1)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_neg_maaran_ottaminen(self):
        saatu_maara = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_otetaan_liikaa(self):
        apu = self.varasto.saldo
        saatu_maara = self.varasto.ota_varastosta(self.varasto.saldo +1)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(apu,saatu_maara)

    def test_str(self):
        self.varasto = Varasto(10,3)
        self.assertEqual(str(self.varasto), "saldo = 3, vielä tilaa 7")
