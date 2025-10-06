2
num1 = float(input("Masukkan bilangan pertama: "))
num2 = float(input("Masukkan bilangan kedua: "))
num3 = float(input("Masukkan bilangan ketiga: "))

# Menentukan bilangan terbesar
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Menampilkan hasil
print("Bilangan terbesar adalah:", largest)