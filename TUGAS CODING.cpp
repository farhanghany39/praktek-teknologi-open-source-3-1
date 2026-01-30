//Tugas Kelompok Double Linked List Selena
//Nama Kelompok : SELENA(2)
//Inaya Nur Wahidah(232370041)
//Selpi Amalia(232370025)
//Nabila Meisya Lubis(232370036)
//1.1 Pagi Sistem Informasi..
//Program: Daftar Inventaris Kantor
#include <conio.h>
#include <windows.h>
#include <iostream>
using namespace std;

struct daftarInventarisKantor {
    char namainventaris[50];
    int jumlah;
    char fungsi[50];
    daftarInventarisKantor*next, *prev;
};
daftarInventarisKantor *awal=NULL,*akhir=NULL,*bantu,*baru,*hapus;

void inputDatadepan(){
	//Penambahan Data Di Depan DLL
    baru = new daftarInventarisKantor;
	baru->next = NULL;
    baru->prev = NULL;
    cout<< "Nama Inventaris : ";
    cin>> baru->namainventaris;
    cout<< "Jumlah\t\t: ";
    cin>> baru->jumlah;
    cout<< "Fungsi\t\t: ";
    cin>> baru->fungsi;
    if (awal == NULL){
        awal = akhir = baru;
    }
    else {
        baru->next = awal;
        awal->prev = baru;
        awal = baru;
    }
    system ("cls");
}

void inputDatabelakang(){
	//Penambahan Data Di Belakang Dll
    baru = new daftarInventarisKantor;
    baru->next = NULL;
    baru->prev = NULL;
    cout << "Nama Inventaris\t\t\t : ";
    cin >> baru->namainventaris;
    cout << "Jumlah\t\t\t: ";
    cin >> baru->jumlah;
    cout << "Fungsi\t\t\t: ";
    cin >> baru->fungsi;
    if (awal == NULL){
        awal = akhir = baru;
    }
    else {
        akhir->next = baru;
        baru->prev = akhir;
        akhir = baru;
    }
    system ("cls");
}

void hapusDatadepan(){
	//Penghapusan Data Di Depan DLL
    if(awal->next == NULL){
        awal=akhir=NULL;
        cout << "Inputan Inventaris Telah Kosong";
    }else{
        hapus = awal;
        awal = awal->next;
        awal->prev = NULL;
        delete hapus;
    }
}

void outputData (){
	//Tampilan
    bantu=awal;
    while (bantu != NULL){
    cout << "Nama Inventaris\t\t: "<< bantu->namainventaris<<endl;
    cout << "Jumlah\t\t\t: "<< baru->jumlah<<endl;
    cout << "Fungsi\t\t\t: "<< bantu->fungsi<<endl;
	bantu = bantu->next;
    }
}

int main()
{
    int pilihan;
    do {
        cout << "-----------DOUBLE LINKED LIST SELENA-----------\n";
        cout << "++++++++SELAMAT DATANG DI KANTOR SELENA++++++++\n";
        cout << "-----------DAFTAR INVENTARIS KANTOR----------: \n";
        cout << "1. Input data di depan\n";
        cout << "2. Input data di belakang\n";
        cout << "3. Hapus data di depan\n";
        cout << "4. Output data\n";
        cout << "<<EXIT>>\n";
        cout << "Pilihan : ";
        cin >> pilihan;
        switch (pilihan){
        case 1 :
            inputDatadepan();
            break;
        case 2 :
            inputDatabelakang();
            break;
        case 3 :
            hapusDatadepan();
            break;
        case 4 :
            if (baru == NULL){
                    cout << "Penginputan Inventaris Masih Kosong";
            }
            else {
                outputData();
            }
            break;
        default :
            cout << "---------EXIT---------";
            break;
        }
    }while(pilihan <= 4);
    getch ();
}
