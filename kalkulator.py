def tambah(a,b):
  return a + b
def kurang(a,b) :
  return a - b
def perkalian(a,b) :
  return a * b
  
print("Pilih operasi :")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")

pilihan = input("Masukkan pilihan (1/2/3) : ")

if pilihan in ('1', '2', '3'):
  angka1 = int(input("Masukkan bilangan pertama : "))
  angka2 = int(input("Masukkan bilangab kedua : "))

  if pilihan == '1':
    print(angka1, "+", angka2, "=", tambah(angka1, angka2))
  elif pilihan == '2':
    print(angka1, "-", angka2, "=", tambah(angka1, angka2))
   elif pilihan == '3':
    print(angka1, "*", angka2, "=", tambah(angka1, angka2))
  else
    print("Pilihan tidak valid")
 
    
