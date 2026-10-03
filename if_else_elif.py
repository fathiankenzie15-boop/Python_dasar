    elif nilai >= 80:
            predikat = "B"
        elif nilai >= 70:
            predikat = "C"nilai = 85
if nilai >=75:
  print('Selamat Anda Lulus')

#if else
tabungan = 150000000
if tabungan >= 150000000:
  print('Tabungan Sudah Tercapai')

grade = 30
if grade >= 90:
  print('Nilai Anda A')
elif grade >= 80:
  print('Nilai Anda B')
elif grade  >= 70:
  print('Nilai Anda C')
else:
  print('Nilai Anda D')

#nested if 
usia = 18
punya_ktp = True

if punya_ktp:
  print('Anda sudah memiliki KTP')
else: # jika punya_ktp adalah False
  if usia >= 17: # Asumsi usia minimal untuk KTP adalah 17
    print('Anda sudah boleh membuat KTP')
  else:
    print('Usia anda belum tercapai')
nilai_input = input('Masukkan Nilai Anda(0-100): ')
try:
    nilai = int(nilai_input)
    if nilai < 0 or nilai > 100:
        print("Peringatan: Angka yang dimasukkan berada di luar rentang 0 sampai 100!")
    else:
        if nilai >= 90:
            predikat = "A"

        elif nilai >= 60:
            predikat = "D"
        else:
            predikat = "E"
        print(f"Predikat Anda: {predikat}")
except ValueError:
    print("Input tidak valid. Harap masukkan angka bulat.")

# Meminta input nilai dari pengguna
input_user = input("Masukkan nilai ujian (0 - 100): ")

# Validasi jika input kosong
if not input_user:
    print("peringatan: Input tidak boleh kosong!)
else:
    nilai = float(input_user)

    # 1. Pernyataan If-Else untuk memeriksa rentang nilai valid (0 - 100)
    if nilai < 0 or nilai > 100:
        print("Peringatan: Angka yang dimasukkan berada di luar rentang 0 sampai 100!")

    else:
        # 2. Percabangan Bersarang (Nested If-Elif-Else) untuk menentukan predikat
        if nilai >= 85:
            predikat = "A"
        elif nilai >= 75:
            predikat = "B’’
        elif nilai >= 60:
            predikat = "C"
        elif nilai >= 45:
            predikat = "D"
        else:
            predikat = "E"

        # Menampilkan hasil
        print(f"Nilai: {nilai} -> Predikat: {predikat}")

