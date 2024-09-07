celsius = float(input("Masukkan suhu dalam Celsius: "))

kelvin = celsius + 273.15
reamur = celsius * 4/5
fahrenheit = celsius * 9/5 + 32

print(f"Suhu dalam Kelvin: {kelvin:.2f} K")
print(f"Suhu dalam Reamur: {reamur:.2f} °Re")
print(f"Suhu dalam Fahrenheit: {fahrenheit:.2f} °F")