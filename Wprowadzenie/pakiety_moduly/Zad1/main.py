import predkosc
distance = float(input("Podaj dystans: "))
time = float(input("Podaj czas: "))
V = predkosc.speed(time, distance)
print(f"Poruszałeś się z prędkością: {V} km/h")