import liczenie_kapitalu.calculate_invest
wartosc_pocz = float(input("Podaj wartość początkową: "))
proc = float(input("Podaj oprocentowanie: "))
lata = float(input("Podaj czas trwania lokaty: "))
wartosc_koncowa = liczenie_kapitalu.calculate_invest.calculate_investment(wartosc_pocz, proc, lata)
print(f"Wartość końcowa: {wartosc_koncowa:.2f} zł")