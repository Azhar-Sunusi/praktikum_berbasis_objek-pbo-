# sebelum_refactoring.py

class PayrollSystem:
    def hitung_gaji(self, nama, tipe, gaji_pokok, jam_kerja=0, tunjangan=0):
        if tipe == "tetap":
            gaji = gaji_pokok + tunjangan
        elif tipe == "kontrak":
            gaji = gaji_pokok * 1.10
        elif tipe == "parttime":
            gaji = jam_kerja * 50000
        else:
            gaji = 0
            
        print(f"Gaji {nama} ({tipe}) : Rp {gaji:,.0f}")
        return gaji

if __name__ == "__main__":
    payroll = PayrollSystem()
    payroll.hitung_gaji("Joko (Tetap)", "tetap", 8000000, tunjangan=1000000)
    payroll.hitung_gaji("Sinta (Kontrak)", "kontrak", 4500000)
    payroll.hitung_gaji("Rudi (Paruh Waktu)", "parttime", 0, jam_kerja=160)