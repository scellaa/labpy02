import random
n = int(input("Masukkan nilai n: "))
for i in range(n):
    while True:
        num = random.random()
        if num < 0.5:
            print(num)
            break 