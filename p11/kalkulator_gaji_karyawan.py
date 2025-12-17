from abc import ABC, abstractmethod
from dataclasses import dataclass

# ===========================
# MODEL SEDERHANA
# ===========================
@dataclass
class Karyawan:
    nama: str
    gaji_pokok: float
    jam_kerja_bulan: int = 0
    tunjangan: float = 0.0

# ===========================
# ABSTRAKSI (Contract untuk OCP/DIP)
# ===========================
class ISalaryCalculator(ABC):
    """Kontrak: Semua kalkulator harus punya method calculate"""
    
    @abstractmethod
    def calculate(self, karyawan: Karyawan) -> float:
        pass

# ===========================
# IMPLEMENTASI KONKRIT (Plug-in)
# ===========================
class PermanentSalaryCalculator(ISalaryCalculator):
    """Karyawan Tetap"""
    
    def calculate(self, karyawan: Karyawan) -> float:
        gaji_bersih = karyawan.gaji_pokok + karyawan.tunjangan
        return gaji_bersih

class ContractSalaryCalculator(ISalaryCalculator):
    """Karyawan Kontrak"""
    
    def calculate(self, karyawan: Karyawan) -> float:
        # Gaji pokok + bonus 10%
        gaji_bersih = karyawan.gaji_pokok * 1.10
        return gaji_bersih

class PartTimeSalaryCalculator(ISalaryCalculator):
    """Karyawan Part Time (Rp 50.000 / jam)"""
    
    def calculate(self, karyawan: Karyawan) -> float:
        gaji_bersih = karyawan.jam_kerja_bulan * 50000
        return gaji_bersih

# ===========================
# KELAS KOORDINATOR (SRP & DIP)
# ===========================
class PayrollProcessor:
    def __init__(self, calculator: ISalaryCalculator):
        self.calculator = calculator
        
    def process_payroll(self, karyawan: Karyawan) -> float:
        gaji = self.calculator.calculate(karyawan)
        print(
            f"Gaji {karyawan.nama} "
            f"({self.calculator.__class__.__name__}): Rp {gaji:,.0f}"
        )
        return gaji

# ===========================
# PROGRAM UTAMA
# ===========================
if __name__ == "__main__":
    # 1. Karyawan Tetap
    joko = Karyawan("Joko (Tetap)", 8000000, tunjangan=1000000)
    permanent_calc = PermanentSalaryCalculator()
    payroll_joko = PayrollProcessor(permanent_calc)
    payroll_joko.process_payroll(joko)
    
    # 2. Karyawan Kontrak
    sinta = Karyawan("Sinta (Kontrak)", 4500000)
    contract_calc = ContractSalaryCalculator()
    payroll_sinta = PayrollProcessor(contract_calc)
    payroll_sinta.process_payroll(sinta)
    
    # 3. Karyawan Part Time
    rudi = Karyawan("Rudi (Paruh Waktu)", gaji_pokok=0, jam_kerja_bulan=160)
    part_time_calc = PartTimeSalaryCalculator()
    payroll_rudi = PayrollProcessor(part_time_calc)
    payroll_rudi.process_payroll(rudi)