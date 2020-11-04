"""
Zadanie 2
Napisz program, który:

Dla liczb z zakresu od 0 do 100, wyświetli te, które są podzielne przez 5.
W następnym wierszu wyświetli te liczby podniesione do potęgi 3.
"""

div_5 = []
cube_root = []

for i in range(0, 101):
  if i > 1:
    if i % 5 == 0:
      div_5.append(i)
      cube_root.append(pow(i, 3))
      
print(f"Liczby podzielne przez 5: \n{div_5}")
print(f"Potęga 3 tych liczb: \n{cube_root}")

print("nobody expects the spanish inquisition")

print("next commmit 1")
