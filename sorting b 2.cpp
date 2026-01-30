#include<iostream>
using namespace std;

int data[10],data1[10];
int n;

void tukar(int *a,int *b){
	int t;
	t=*a;
	*a=*b;
	*b=t;
}
void bubble_sort(int data[]){
	for(int i=1;i<=n;i++){
		for(int j=n-1;j>=i;j--){
			if(data[j]<data[j-1])tukar(&data[j],&data[j-1]);
		}
	}
}
void bubble_sortdua( int data[]){
	for(int i=1;i<=n;i++){
		for(int j=n-1;j>=i;j--){
			if(data[j]>data[j-1])tukar(&data[j],&data[j-1]);
		}
	}
}

int main()
{ 
cout<<"masukkan banyak data :";
cin>>n;
for(int i=0;i<n;i++)
{
	cout<<"\n masukkan data ke"<<i+1<<"=";
	cin>>data[i];
	data1[i]=data[i];
	
}
cout<<"\n data diurutkan ascending:";
bubble_sort(data);
for(int i=0;i<n;i++)
{
	cout<<"\t"<<data[i];
}
cout<<endl;
cout<<"\n data diurutkan decending;";
bubble_sortdua(data);
for(int i=0;i<n;i++)
{
	cout<<"\t"<<data[i];
}
cout<<endl;
}
