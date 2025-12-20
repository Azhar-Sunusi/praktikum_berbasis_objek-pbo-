import unittest
from diskon_service import DiskonCalculator

class TestDiskonCalculator(unittest.TestCase):
    
    def setUp(self):
        """Arrange: Siapkan instance Calculator sebelum tiap tes."""
        self.calc = DiskonCalculator()

    # --- TES STANDAR (Langkah 3) ---
    def test_diskon_standar_10_persen(self):
        """Tes 1: Memastikan diskon 10% pada 1000 menghasilkan 900."""
        hasil = self.calc.hitung_diskon(1000, 10)
        self.assertEqual(hasil, 900.0)

    def test_diskon_nol(self):
        """Tes 2 (Boundary): Memastikan diskon 0% tidak mengubah harga."""
        hasil = self.calc.hitung_diskon(500, 0)
        self.assertEqual(hasil, 500.0)

    def test_diskon_batas_atas(self):
        """Tes 3 (Boundary): Memastikan diskon 100% menghasilkan 0."""
        hasil = self.calc.hitung_diskon(750, 100)
        self.assertEqual(hasil, 0.0)

    def test_input_negatif(self):
        """Tes 4 (Boundary): Memastikan input diskon negatif tidak merusak harga."""
        # Asumsi: Kalau diskon -5%, harga tetap (atau error), tidak boleh nambah.
        hasil = self.calc.hitung_diskon(500, -5)
        # Logika: Diskon negatif = 500 - (500 * -5 / 100) = 500 - (-25) = 525 (Malah nambah mahal)
        # Tapi di soal diminta "assertGreaterEqual(hasil, 500)" -> Harga tidak boleh turun
        self.assertGreaterEqual(hasil, 500)

    # --- TES LANJUTAN (Latihan Mandiri D.3) ---
    def test_diskon_float(self):
        """Tes 5: Uji nilai float (diskon 33% pada 999)."""
        # 999 * 33% = 329.67. Harga akhir = 999 - 329.67 = 669.33
        hasil = self.calc.hitung_diskon(999, 33)
        # assertAlmostEqual berguna untuk membandingkan angka koma (float)
        self.assertAlmostEqual(hasil, 669.33, places=2)

    def test_harga_nol(self):
        """Tes 6: Uji Edge Case (harga awal 0)."""
        hasil = self.calc.hitung_diskon(0, 50)
        self.assertEqual(hasil, 0.0)

if __name__ == '__main__':
    unittest.main()