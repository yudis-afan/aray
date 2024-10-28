# deklarasi array untuk menyimpan nilai
nilai_siswa = []
 
# meminta input nilai dari pengguna
for i in range(5):
    nilai = float (input(f"masukkan niali siswa ke-(i+1): "))
    nilai_siswa.append(nilai)
     
# menghitung total nilai
total_nilai = sum(nilai_siswa)
 
# menghitung rata rata
rata_rata = total_nilai / len(nilai_siswa)
 
# menampilkan hasil rata rata
print(f"rata rata nilai siswa adalah: (rata_rata)")