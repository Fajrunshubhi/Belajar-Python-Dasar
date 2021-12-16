# a = 10, a adalah variabel dengan nilai 10

# tipe data: Angka satuan yang gak ada
# koma nya (integer)
data_integer = 11
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# tipe data: angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "ucup"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# tipe data: biner true/false (boolean)
data_bool = False
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

## tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double, c_char

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))



# Tipe Data String (text)
nama = "fajrun shubhi"
kota = "cirebon"
alamat = "panguragan kulon"

nama_depan = "fajrun"
nama_belakang = "shubhi"
nama_lengkap = nama_depan + " " + nama_belakang

print(nama_lengkap)
print(kota)
print(alamat)

sapa = "haloo" + nama_lengkap + "selamat datang"
print(sapa)
# ini solusi untuk masalah diatas agar lebih muda
# String format
sapa2 = f"halloo {nama_depan} {nama_belakang} selamat datang "
print(sapa2)

# Tipe Data Angka (number)
# tanpa petik
umur = 19
tinggi_badan = 170


# Tipe Data Boolean
# hanya ada 2 nilai yaitu benar atau salah
# true or false
lulus = False
kuliah = True
print(lulus)
print(kuliah )