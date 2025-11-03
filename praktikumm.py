import sys
import os

class Mahasiswa:
    def __init__(self, nim='', nama=''):
        self.nim = nim
        self.nama = nama

pilih = 0
datasiswa = []

def menu():
    os.system('cls')
    print("MENU APLIKASI DATA SISWA LINKED LIST PYTHON")
    print("---------------------------------------------")
    print("1. INPUT DATA SISWA")
    print("2. TAMPILKAN DATA SISWA")
    print("3. UPDATE DATA SISWA")
    print("4. HAPUS DATA SISWA")
    print("5. AUTHOR")
    print("6. KELUAR APLIKASI")
    pilih = int(input("MASUKKAN PILIHAN ANDA : "))
    if pilih == 1:
        input_data()
        menu()
    elif pilih == 2:
        tampil()
        input("KEMBALI MENU UTAMA")
        menu()
    elif pilih == 3:
        index_update = -1
        tampil()
        id_edit = int(input("INPUT NIM YANG AKAN DI UPDATE: "))
        for a in range(len(datasiswa)):
            if id_edit == datasiswa[a].nim:
                index_update = a
                break
        if index_update > -1:
            print("INPUT DATA YANG DI UPDATE")
            siswa = Mahasiswa()
            siswa.nim = int(input("MASUKAN NIM : "))
            siswa.nama = input("MASUKAN NAMA SISWA : ")
            datasiswa[index_update] = siswa
            print("BERHASIL UPDATE DATA SISWA")
        else:
            print("NIM TIDAK DITEMUKAN")
        input("KEMBALI KE MENU UTAMA")
        menu()
    elif pilih == 4:
        os.system('cls')
        tampil()
        index_delete = -1
        id_hapus = int(input("INPUT NIM YANG AKAN DI HAPUS: "))
        for a in range(len(datasiswa)):
            if id_hapus == datasiswa[a].nim:
                index_delete = a
                break
        if index_delete > -1:
            del datasiswa[index_delete]
            print("DATA TELAH DI HAPUS")
        else:
            print("NIM TIDAK DI TEMUKAN")
        input("KEMBALI MENU UTAMA")
        menu()
    elif pilih == 5:
        author()
        input("\n\n KEMBALI MENU UTAMA")
        menu()
    elif pilih == 6:
        sys.exit()

def tampil():
    os.system('cls')
    print("DATA MAHASISWA")
    for data in datasiswa:
        print("NIM : " + str(data.nim))
        print("NAMA : " + data.nama)
        print("----------------------------------")

def author():
    os.system('cls')
    print("alvin meko | 232370008")
    print("uks 2015")

def input_data():
    ulang = 'Y'
    while ulang in ('y', 'Y'):
        os.system('cls')
        siswabaru = Mahasiswa()
        print("INPUT DATA MAHASISWA")
        siswabaru.nim = int(input("masukkan nim : "))
        siswabaru.nama = input("MASUKAN NAMA SISWA: ")
        datasiswa.append(siswabaru)
        ulang = input("APAKAH ANDA INGIN MENGULANG (Y/T)?")

menu()
