# DEBUG REPORT

**Masalah:** Harga akhir selalu 10% lebih tinggi dari ekspektasi.
**Input:** Harga 1000, Diskon 10% (Ekspektasi: 900.0)

## Langkah Debugging (menggunakan pdb):
1. Aktifkan `pdb.set_trace()` sebelum baris `harga_akhir`.
2. Jalankan script. Program berhenti di dalam fungsi.
3. Periksa nilai variabel:
   - `(Pdb) p harga_awal` -> Output: `1000`
   - `(Pdb) p jumlah_diskon` -> Output: `100.0`
   - `(Pdb) n` (menjalankan baris berikutnya)
   - `(Pdb) p harga_akhir` -> Output: `990.0` 

**Analisis:** Hasil pengurangannya seharusnya $1000 - 100 = 900$. Namun, saat dicek dengan `p harga_akhir`, muncul angka `990.0`. Ini membuktikan ada operasi tambahan $900 * 1.1$ (PPN 10%) yang tidak seharusnya ada.