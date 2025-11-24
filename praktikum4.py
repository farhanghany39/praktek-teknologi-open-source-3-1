# segitiga_05.py
def hourglass(n):
    # bagian atas (inverted triangle) 
    for i in range(n, 0, -1):
        spaces = n - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)
    # bagian bawah (upright triangle) 
    for i in range(2, n + 1):
        spaces = n - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

def main():
    try:
        x = int(input("Masukkan angka : ").strip())
        if x <= 0:
            print("Masukkan angka positif lebih besar dari nol.")
            return
        hourglass(x)
    except ValueError:
        print("Masukkan nilai integer yang valid.")

if __name__ == "__main__":
    main()