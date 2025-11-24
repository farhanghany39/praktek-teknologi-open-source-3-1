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
        if data.ip is None:
            print("IP : Belum diinput/hitung")
        else:
            print("IP : " + "{:.2f}".format(data.ip))
        print("---------------")

def author():
    os.system('cls')
    print("alvin meko | 672010193")
    print("uksw 2015")

def simpan_ke_file(mahasiswa):
    """Membuat file TXT otomatis berisi data mahasiswa"""
    filename = f"Mahasiswa_{mahasiswa.nim}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"NIM : {mahasiswa.nim}\n")
        f.write(f"Nama : {mahasiswa.nama}\n")
        f.write("Nilai per Mata Kuliah:\n")
        for mk, sks in MATA_KULIAH.items():
            nilai = mahasiswa.grades.get(mk)
            if nilai is None:
                f.write(f"  - {mk} ({sks} SKS): Belum diinput\n")
            else:
                f.write(f"  - {mk} ({sks} SKS): {nilai:.2f}\n")
        if mahasiswa.ip is None:
            f.write("IP : Belum diinput/hitung\n")
        else:
            f.write(f"IP : {mahasiswa.ip:.2f}\n")
    print(f"File TXT '{filename}' berhasil dibuat.")

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

        # Simpan otomatis ke file TXT
        simpan_ke_file(siswaBaru)

        ulang = input("Apakah Anda Ingin Mengulang (Y/ T) ? ")
    menu()

def update_data():
    os.system('cls')
    print("UPDATE DATA MAHASISWA")
    try:
        nim = int(input("Masukkan NIM mahasiswa yang akan diupdate: "))
    except ValueError:
        print("NIM harus angka")
        input("Tekan Enter untuk kembali...")
        menu()
        return
    for m in dataSiswa:
        if m.nim == nim:
            print(f"Data ditemukan: {m.nama}")
            print("1. Ubah nama\n2. Ubah nilai mata kuliah\n3. Kembali")
            choice = input("Pilih: ")
            if choice == '1':
                m.nama = input("Masukkan nama baru: ")
                simpan_ke_file(m)
                print("Nama berhasil diupdate.")
                input("Tekan Enter untuk kembali...")
                menu()
                return
            elif choice == '2':
                total_point = 0.0
                for mk, sks in MATA_KULIAH.items():
                    cur = m.grades.get(mk)
                    prompt = f"{mk} ({sks} SKS) nilai [{cur if cur is not None else 'kosong'}] (enter untuk lewati): "
                    val_str = input(prompt)
                    if val_str.strip() == '':
                        if cur is None:
                            val = 0.0
                        else:
                            val = cur
                    else:
                        try:
                            val = float(val_str)
                        except ValueError:
                            print("Nilai tidak valid, menggunakan nilai lama (atau 0.0 jika belum ada)")
                            val = cur if cur is not None else 0.0
                        if val < 0 or val > MAX_IP:
                            print(f"Nilai harus antara 0 dan {MAX_IP}, menggunakan 0.0")
                            val = 0.0
                    m.grades[mk] = val
                    total_point += val * sks
                m.ip = total_point / TOTAL_SKS
                simpan_ke_file(m)
                print("Nilai dan IP berhasil diupdate.")
                input("Tekan Enter untuk kembali...")
                menu()
                return
            else:
                menu()
                return
    print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
    input("Tekan Enter untuk kembali...")
    menu()


def hapus_data():
    os.system('cls')
    print("HAPUS DATA MAHASISWA")
    try:
        nim = int(input("Masukkan NIM mahasiswa yang akan dihapus: "))
    except ValueError:
        print("NIM harus angka")
        input("Tekan Enter untuk kembali...")
        menu()
        return
    for i, m in enumerate(dataSiswa):
        if m.nim == nim:
            confirm = input(f"Yakin ingin menghapus {m.nama} (NIM {nim})? (Y/T): ")
            if confirm.lower() == 'y':
                del dataSiswa[i]
                filename = f"Mahasiswa_{nim}.txt"
                if os.path.exists(filename):
                    try:
                        os.remove(filename)
                        print(f"File {filename} dihapus.")
                    except OSError:
                        print(f"File {filename} tidak dapat dihapus.")
                print("Data mahasiswa berhasil dihapus.")
                input("Tekan Enter untuk kembali...")
                menu()
                return
            else:
                print("Batal menghapus.")
                input("Tekan Enter untuk kembali...")
                menu()
                return
    print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
    input("Tekan Enter untuk kembali...")
    menu()


def input_nilai_ip():
    os.system('cls')
    print("INPUT / UPDATE NILAI IP MAHASISWA")
    try:
        nim = int(input("Masukkan NIM mahasiswa: "))
    except ValueError:
        print("NIM harus angka")
        input("Tekan Enter untuk kembali...")
        menu()
        return
    for m in dataSiswa:
        if m.nim == nim:
            total_point = 0.0
            for mk, sks in MATA_KULIAH.items():
                while True:
                    try:
                        val = input(f"{mk} ({sks} SKS) nilai (kosong untuk pakai nilai lama): ")
                        if val.strip() == '':
                            valf = m.grades.get(mk, 0.0)
                        else:
                            valf = float(val)
                        if valf < 0 or valf > MAX_IP:
                            print(f"Nilai harus antara 0 dan {MAX_IP}. Coba lagi.")
                            continue
                        m.grades[mk] = valf
                        total_point += valf * sks
                        break
                    except ValueError:
                        print("Nilai harus angka. Coba lagi.")
            m.ip = total_point / TOTAL_SKS
            simpan_ke_file(m)
            print(f"IP mahasiswa {m.nama} (NIM {m.nim}) diperbarui menjadi {m.ip:.2f}")
            input("Tekan Enter untuk kembali...")
            menu()
            return
    print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
    input("Tekan Enter untuk kembali...")
    menu()

if __name__ == "__main__":
    menu()