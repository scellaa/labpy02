n = int(input("Jumlah data: "))
while n < 3:
    n = int(input('minimal 3, coba lagi'))

data = [int(input(f'data {i+1}:')) for i in range (n)]
data.sort()

print('hasil urut: ')
for i, v in enumerate(data, 1):
    print(f'{i}. {v}') 