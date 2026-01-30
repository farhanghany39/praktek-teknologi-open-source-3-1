#include <iostream>
using namespace std;
int main()
{
	char nama[20], tambahan, membayar;
	int harga, jumlah, total, bayar, menu, kode, berat;
	cout<<"|============== SELAMAT DATANG DI AFFILIA LAUNDRY================|"<<endl;
	cout<<endl;
	cout<<"MASUKKAN NAMA CUSTOMER :";
	cin>>nama;
	cout<<endl;
		cout<<"     |=========DAFTAR PAKET JENIS LAYANAN LAUNDRY===========| "<<endl;
	 		cout<<"kode |         jenis layanan        |         harga         | "<<endl;
	 		cout<<"  1  |   Paket Expres(1 hari)       |      Rp.12.000/kg     | "<<endl;
	 		cout<<"  2  |   Paket reguler(2 hari)      |      Rp.8.000/kg      | "<<endl;
	 		cout<<"  3  |   Paket cuci kering expres   |      Rp.7.000/kg      | "<<endl;
	 		cout<<"  4  |   Paket cuci kering biasa    |      Rp.5.000/kg      | "<<endl;
	 		cout<<"  5  |   bedcover expres            |      Rp.40.000/kg     | "<<endl;
	 		cout<<"  6  |   bedcover biasa             |      Rp.30.000/kg     | "<<endl;
	 		cout<<"  7  |   helm                       |      Rp.25.000/kg     | "<<endl;
	 		cout<<endl;
	 		atas :
	 		cout<<" pilih kode jenis layanan (1-7): ";
			cin>>kode;
			switch(kode)
			{
				case 1:
					harga=12000;
					cout<<"anda memilih kode 1 paket express(1 hari) dengan harga ="<<harga<<endl;
					cout<<"masukan berat pakaian: ";
					cin>>berat;
					break;
				case 2:
					harga=8000;
					cout<<"anda memilih kode 2 paket reguler(2 hari) dengan harga ="<<harga<<endl;
					cout<<"masukan berat pakaian: ";
					cin>>berat;
					break;
				case 3:
					harga=7000;
					cout<<"anda memilih kode 3 paket cuci kering expres dengan harga ="<<harga<<endl;
					cout<<"masukan berat pakaian: ";
					cin>>berat;
					break;
				case 4:
					harga=5000;
					cout<<"anda memilih kode 4 paket cuci kering biasa dengan harga ="<<harga<<endl;
					cout<<"masukan berat pakaian: ";
					cin>>berat;
					break;
				case 5:
					harga=40000;
					cout<<"anda memilih kode 5 paket cuci bed cover expres dengan harga ="<<harga<<endl;
					cout<<"masukan berat pakaian: ";
					cin>>berat;
					break;
				case 6:
					harga=30000;
					cout<<"anda memilih kode 3 paket cuci bed cover biasa dengan harga ="<<harga<<endl;
					cout<<"masukan berat pakaian: ";
					cin>>berat;
					break;
				case 7:
					harga=25000;
					cout<<"anda memilih kode 3 paket cuci helm dengan harga ="<<harga<<endl;
					cout<<"masukan berat pakaian: ";
					cin>>berat;
					break;
				default : cout<<"maaf code tidak ada";
			}
		cout<<endl;
	cout<<" Total Bayar           = Rp. "            <<berat*harga<<endl;
	total=berat*harga;                        
	cout<<" Bayar                 = Rp. ";                 
	cin>>bayar;
	cout<<" Anda Membayar Sebesar = Rp. "            <<bayar<<endl; 
	cout<<" Kembalian Anda        = Rp. "            <<bayar-total<<endl;
	cout<<endl;
	bawah:
	cout<<" Apakah Anda Sudah Membayar  = ";
	cin>>membayar;
	cout<<endl;
	if(membayar=='Y' || membayar=='y')
	{
			cout<<"========================================="<<endl;
		cout<<"|           STRUK PEMBAYARAN            |"<<endl;
		cout<<"========================================="<<endl;
		cout<<"|Nama Pembeli          = "                <<nama;         cout<<"		|"<<endl;
		cout<<"|Total Barang          = "                <<berat;       cout<<"   unit	|"<<endl;
 		cout<<"|Total Harga           = Rp. "            <<berat*harga; cout<<"	|"<<endl;
		total=berat*harga;                        
		cout<<"|Bayar                 = Rp. "            <<bayar;        cout<<"	|"<<endl;                 
		cout<<"|Kembalian Anda        = Rp. "            <<bayar-total;  cout<<"	|"<<endl;
		cout<<"|========================================="<<endl;
		
		cout<<"Apakah Ada Tambahan : ";
		cin>>tambahan;
		if(tambahan=='Y' || tambahan=='y')
	{
			goto atas;
		}
		if(tambahan=='T' || tambahan=='t')
		{
			cout<<endl;
			cout<<"===>TERIMA KASIH SUDAH BERBELANJA<===="<<endl;
		}
		else
		{
			cout<<"Maaf Pilihan Anda Tidak Ada";
		}
	}
	else
	{
		cout<<"======>SILAHKAN SELESAIKAN DAHULU PEMBAYARAN ANDA<======"<<endl;
		cout<<endl;
		goto bawah;
	}
	
	return 0;
}
