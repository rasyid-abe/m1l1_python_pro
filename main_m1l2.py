import random

karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
panjang_karakter = input("Masukkan panjang sandi:")
password = ""

for i in range(int(panjang_karakter)):
    password += random.choice(karakter)

print(password)


acak = random.randint(1, 10)