n = int(input("Jumlah data: "))
while n < 3:
    n = int(input('minimal 3, coba lagi'))

data = [float(input(f'data {i+1}:')) for i in range (3)]
data.sort()

print('hasil urut: ')
for i, v in enumerate(data, 1):
    print(f'{i}. {v}') 