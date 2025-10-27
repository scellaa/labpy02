import random
# Meminta input n dari pengguna pada saat runtime
n = int(input("Masukkan nilai n: "))
# Menggunakan kombinasi for dan while untuk menghasilkan n bilangan acak yang kurang dari 0.5
for i in range(n):
    while True:
        # Menghasilkan bilangan acak antara 0 dan 1
        num = random.random()
        # Memeriksa apakah kurang dari 0.5
        if num < 0.5:
            print(num)
            break 