time_in_sec = int(input("Введите время в секундах: "))

h = time_in_sec // 3600
residue = time_in_sec % 3600
m = residue // 60
s = residue % 60

print(f"Now is {h}:{m}:{s} ")