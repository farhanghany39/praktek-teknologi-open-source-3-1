def verify_input(prompt="Masukkan data: "):
    s = input(prompt).strip()

    try:
        v_int = int(s)
        print("Tipe data: integer")
        print("Nilai:", v_int)
        return "int", v_int
    except ValueError:
        pass
    
    try:
        v_float = float(s)
        print("Tipe data: float")
        print("Nilai:", v_float)
        return "float", v_float
    except ValueError:
        print("Salah. Input bukan integer maupun float.")
        return "invalid", s

if __name__ == "__main__":
    verify_input("Masukkan data: ")