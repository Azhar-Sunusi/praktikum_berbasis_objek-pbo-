1. Kode Sebelum Refactoring (Masalah)
Kode ini buruk karena satu fungsi menangani semua logika perhitungan dan output, sehingga sulit dikembangkan (melanggar SRP dan OCP).

Python

class PayrollSystem:
    def hitung_gaji(self, nama, tipe, gaji_pokok, jam_kerja=0, tunjangan=0):
        if tipe == "tetap": gaji = gaji_pokok + tunjangan
        elif tipe == "kontrak": gaji = gaji_pokok * 1.10
        elif tipe == "parttime": gaji = jam_kerja * 50000
        else: gaji = 0
        print(f"Gaji {nama} ({tipe}) : Rp {gaji:,.0f}")
2. Kode Setelah Refactoring (Solusi SOLID)
Kode ini memisahkan data (Model), kontrak (Abstraksi), dan logika (Implementasi) agar lebih fleksibel.

Python

from abc import ABC, abstractmethod
from dataclasses import dataclass

# MODEL DATA
@dataclass
class Karyawan:
    nama: str
    gaji_pokok: float
    jam_kerja_bulan: int = 0
    tunjangan: float = 0.0

# ABSTRAKSI & IMPLEMENTASI (OCP/DIP)
class ISalaryCalculator(ABC):
    @abstractmethod
    def calculate(self, karyawan: Karyawan) -> float: pass

class PermanentSalaryCalculator(ISalaryCalculator):
    def calculate(self, karyawan: Karyawan): return karyawan.gaji_pokok + karyawan.tunjangan

class ContractSalaryCalculator(ISalaryCalculator):
    def calculate(self, karyawan: Karyawan): return karyawan.gaji_pokok * 1.10

class PartTimeSalaryCalculator(ISalaryCalculator):
    def calculate(self, karyawan: Karyawan): return karyawan.jam_kerja_bulan * 50000

# KOORDINATOR (SRP)
class PayrollProcessor:
    def __init__(self, calculator: ISalaryCalculator):
        self.calculator = calculator # Dependency Injection

    def process_payroll(self, karyawan: Karyawan):
        gaji = self.calculator.calculate(karyawan)
        print(f"Gaji {karyawan.nama} ({self.calculator.__class__.__name__}): Rp {gaji:,.0f}")

# EKSEKUSI
if __name__ == "__main__":
    joko = Karyawan("Joko", 8000000, tunjangan=1000000)
    PayrollProcessor(PermanentSalaryCalculator()).process_payroll(joko)
    
    rudi = Karyawan("Rudi", 0, jam_kerja_bulan=160)
    PayrollProcessor(PartTimeSalaryCalculator()).process_payroll(rudi)
Ringkasan Analisis:
SRP (Single Responsibility): Perhitungan gaji dipisah dari proses cetak/koordinasi.

OCP (Open-Closed): Menambah tipe karyawan baru cukup buat kelas baru, tanpa mengubah kode lama.

DIP (Dependency Inversion): PayrollProcessor bergantung pada interface ISalaryCalculator, bukan pada logika spesifik.