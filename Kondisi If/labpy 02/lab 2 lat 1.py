a = input('Enter first number: ')
b = input('Enter second number: ')
c = input('Enter third number: ')
d = input('Enter fourth number: ')

a= int (a)
b= int (b)
c= int (c)
d= int (d)

if a > b and a > c and a > d:
    print((a), 'is greater')
elif b > a and b > c and b > d:
    print((b), 'is greater') 
elif c > a and c > b and c > d:
    print((c), 'is greater')
elif d > a and d > b and d > c:
    print((d), 'is greater')
else:
    print('the number is equal')
    
    