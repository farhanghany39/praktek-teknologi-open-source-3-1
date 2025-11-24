import sys
import os

class Mahasiswa:
    def __init__(self, nim=0, nama="", ip=None, grades=None):
        self.nim = nim
        self.nama = nama
        self.ip = ip
        self.grades = grades if grades is not None else {}

dataSiswa = []

# Konfigurasi mata kuliah dan SKS
MATA_KULIAH = {
    "Statistik": 2,
    "Pancasila": 2,
    "Pemrograman": 3
}
TOTAL_SKS = sum(MATA_KULIAH.values())
MAX_IP = 4.0

def menu():
    os.system('cls')
    print("Menu Aplikasi Data Siswa LinkedList python")
    print("")
    print("1. Input Data Siswa ")
    print("2. Tampilkan Data Siswa")
    print("3. Update Data Siswa")
    print("4. Hapus Data Siswa")
    print("5. Author")
    print("6. Hitung / Update Nilai IP ")
    print("7. Keluar Aplikasi")
    try:
        pilih = int(input("Masukkan pilihan anda : "))
    except ValueError:
        print("Input tidak valid, masukkan angka antara 1-7")
        input("Tekan Enter untuk kembali...")
        return menu()

    if pilih == 1:
        pilihl()
    elif pilih == 2:
        tampil()
        input("kembali menu utama")
        menu()
    elif pilih == 3:
        update_data()
    elif pilih == 4:
        hapus_data()
    elif pilih == 5:
        author()
        input("\n\n kembali menu utama")
        menu()
    elif pilih == 6:
        input_nilai_ip()
    elif pilih == 7:
        sys.exit()
    else:
        print("Pilihan tidak tersedia")
        input("Tekan Enter untuk kembali...")
        menu()

def tampil():
    os.system('cls')
    print("DATA MAHASISWA")
    if not dataSiswa:
        print("Belum ada data mahasiswa.")
        return
    for data in dataSiswa:
        print("Nim : " + str(data.nim))
        print("Nama : " + data.nama)
        # Tampilkan nilai per mata kuliah
        if data.grades:
            print("Nilai per Mata Kuliah:")
            for mk, sks in MATA_KULIAH.items():
                nilai = data.grades.get(mk)
                if nilai is None:
                    print(f"  - {mk} ({sks} SKS): Belum diinput")
                else:
                    print(f"  - {mk} ({sks} SKS): {nilai:.2f}")
        else:
            print("Nilai per Mata Kuliah: Belum diinput")
        # Tampilkan IP jika ada
        if data.ip is None:
            print("IP : Belum diinput/hitung")
        else:
            print("IP : " + "{:.2f}".format(data.ip))
        print("---------------")

def author():
    os.system('cls')
    print("alvin meko | 672010193")
    print("uksw 2015")

def pilihl():
    ulang = 'Y'
    while ulang in ('y', 'Y'):
        os.system('cls')
        siswaBaru = Mahasiswa()
        print("INPUT DATA MAHASISWA ")
        try:
            siswaBaru.nim = int(input("masukkan nim : "))
        except ValueError:
            print("NIM harus berupa angka")
            input("Tekan Enter untuk ulang input...")
            continue
        siswaBaru.nama = input("masukkan nama siswa : ")

        # Input nilai tiap mata kuliah dan hitung IP langsung
        print("Masukkan nilai untuk mata kuliah berikut (skala 0.0 - 4.0).")
        grades = {}
        total_point = 0.0
        for mk, sks in MATA_KULIAH.items():
            while True:
                try:
                    val = float(input(f"{mk} ({sks} SKS) nilai: "))
                except ValueError:
                    print("Nilai harus angka (contoh: 3.5). Coba lagi.")
                    continue
                if val < 0 or val > MAX_IP:
                    print(f"Nilai harus antara 0 dan {MAX_IP}. Coba lagi.")
                    continue
                grades[mk] = val
                total_point += val * sks
                break

        ip_hitung = total_point / TOTAL_SKS
        if ip_hitung > MAX_IP:
            ip_hitung = MAX_IP

        siswaBaru.grades = grades
        siswaBaru.ip = ip_hitung

        dataSiswa.append(siswaBaru)
        print(f"Mahasiswa {siswaBaru.nama} (NIM {siswaBaru.nim}) berhasil ditambahkan dengan IP {siswaBaru.ip:.2f}")
        ulang = input("Apakah Anda Ingin Mengulang (Y/ T) ? ")
    menu()

def update_data():
    index_update = -1
    tampil()
    if not dataSiswa:
        input("kembali menu utama")
        menu()
        return
    try:
        id_edit = int(input("Input Nim yang akan di update : "))
    except ValueError:
        print("NIM harus berupa angka")
        input("kembali menu utama")
        menu()
        return
    for a in range(0, len(dataSiswa)):
        if id_edit == dataSiswa[a].nim:
            index_update = a
            break
    if index_update > -1:
        print("INPUT DATA YANG DI UPDATE ")
        siswa = Mahasiswa()
        try:
            siswa.nim = int(input("masukkan nim : "))
        except ValueError:
            print("NIM harus berupa angka")
            input("kembali menu utama")
            menu()
            return
        siswa.nama = input("masukkan nama siswa : ")
        # Pertahankan IP dan grades lama jika ada
        siswa.ip = dataSiswa[index_update].ip
        siswa.grades = dataSiswa[index_update].grades
        dataSiswa[index_update] = siswa
        print("berhasil update data siswa")
    else:
        print("nim tidak ditemukan")
    input("kembali menu utama")
    menu()

def hapus_data():
    index_delete = -1
    tampil()
    if not dataSiswa:
        input("kembali menu utama")
        menu()
        return
    try:
        id_hapus = int(input("Input Nim yang akan di hapus : "))
    except ValueError:
        print("NIM harus berupa angka")
        input("kembali menu utama")
        menu()
        return
    for a in range(0, len(dataSiswa)):
        if id_hapus == dataSiswa[a].nim:
            index_delete = a
            break
    if index_delete > -1:
        del dataSiswa[index_delete]
        print("Data Telah di hapus")
    else:
        print("nim tidak ditemukan")
    input("kembali menu utama")
    menu()

def input_nilai_ip():
    os.system('cls')
    print("INPUT / HITUNG NILAI IP MAHASISWA (update nilai untuk mahasiswa yang sudah ada)")
    if not dataSiswa:
        print("Belum ada data mahasiswa.")
        input("kembali menu utama")
        menu()
        return
    try:
        id_nim = int(input("Masukkan NIM mahasiswa: "))
    except ValueError:
        print("NIM harus berupa angka")
        input("kembali menu utama")
        menu()
        return
    mahasiswa = None
    for m in dataSiswa:
        if m.nim == id_nim:
            mahasiswa = m
            break
    if mahasiswa is None:
        print("NIM tidak ditemukan")
        input("kembali menu utama")
        menu()
        return

    total_point = 0.0
    print("Masukkan nilai untuk mata kuliah berikut (skala 0.0 - 4.0).")
    grades = {}
    for mk, sks in MATA_KULIAH.items():
        while True:
            try:
                val = float(input(f"{mk} ({sks} SKS) nilai: "))
            except ValueError:
                print("Nilai harus angka (contoh: 3.5). Coba lagi.")
                continue
            if val < 0 or val > MAX_IP:
                print(f"Nilai harus antara 0 dan {MAX_IP}. Coba lagi.")
                continue
            grades[mk] = val
            total_point += val * sks
            break

    ip_hitung = total_point / TOTAL_SKS
    if ip_hitung > MAX_IP:
        ip_hitung = MAX_IP
    mahasiswa.grades = grades
    mahasiswa.ip = ip_hitung
    print(f"IP untuk {mahasiswa.nama} (NIM {mahasiswa.nim}) berhasil dihitung: {mahasiswa.ip:.2f}")
    input("kembali menu utama")
    menu()

if __name__ == "__main__":
    menu()