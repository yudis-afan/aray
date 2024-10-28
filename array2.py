# deklarasi matriks
matriks = []

# meminta input pengguna untuk mengisi matiks 3x3
print("masukkan elemen untuk matriks 3x3:")
for i in range(3):
    baris = []
    for j in range(3):
        nilai = int(input(f"masukkan elemen baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matriks.append(baris)
    
# transpose matriks
transpose = []
for i in range(3):
    baris = []
    for j in range(3):
        baris.append(matriks[j][i])
    transpose.append(baris)
    
# menampilkan hasil transpose
print("\nHasil transpose matiks:")