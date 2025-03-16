def kalkulator (angka_1,angka_2,operator):
    if operator == "+":
        return (angka_1 + angka_2)
    elif operator == "-":
        return (angka_1 - angka_2)
    elif operator == "*":
        return (angka_1 * angka_2)
    elif operator == "/":
        if angka_2 == 0:
            return "error: pembagian dengan nol tidak diperbolehkan"
        return angka_1 / angka_2
    else:
        return "error:operator tidak valid"

angka_1 =float(input("masukan angka pertama: "))
angka_2 = float(input("masukan angka kedua: "))
operator = input("masukan operator (+ , - , * , /): ")

hasil = kalkulator (angka_1, angka_2, operator)
print (f"Hasil:{hasil}")