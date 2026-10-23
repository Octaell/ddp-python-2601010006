panjang = float(input("masukkan panjang: "))
lebar = float(input("masukkan lebar: "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print(f"Luas: {luas} m2")
print(f"Keliling: {keliling} m")

# Trace Table contoh data(panjang =5 lebar= 3)
# | Baris | Panjang | Lebar | Luas | Keliling | Output               |
# |-------|---------|-------|------|----------|----------------------|
# | 1     | 5.0     | -     | -    | -        | masukkan panjang : 5 |
# | 2     | 5.0     | 3.0   | -    | -        | masukkan lebar : 3   |
# | 4     | 5.0     | 3.0   | 15.0 | -        | -                    |
# | 5     | 5.0     | 3.0   | 15.0 | 16.0     | -                    |
# | 7     | 5.0     | 3.0   | 15.0 | 16.0     | Luas: 15.0 m2        |
# | 8     | 5.0     | 3.0   | 15.0 | 16.0     | Keliling: 16.0 m     |
