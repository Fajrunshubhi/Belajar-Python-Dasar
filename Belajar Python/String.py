# membandingkan STRING
s1 = "fajrun"
s2 = "shubhi"
print("s1: " + s1)
print("s2: " + s2)

if s1 == s2:
    print("s1 sama dengan s2")
else:
    print("s1 tidak sama dengan s2")

# mengambil nilai pada STRING (substring)

cek1 = s1[0] # output = f
cek2 = s1[1] # output = a
print(cek1)
print(cek2)

cek3 = s1[-4] # dihitung dari kanan
cek4 = s1[:2] # 2 karakter pertama String atau dibaca karakater pertama (index 0) sampai index 2
cek5 = s1[2:] # ambil karakter dimulai dari index ke 2 sampai akhir
cek6 = s1[1:4] # ambil karakter dari index ke 1 sampai index ke 4
print(cek3)
print(cek4)
print(cek5)
print(cek6)