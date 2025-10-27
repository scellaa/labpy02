a = input('Enter first number: ')
b = input('Enter second number: ')
c = input('Enter third number: ')
d = input('Enter fourth number: ')

a= int (a)
b= int (b)
c= int (c)
d= int (d)

if a > b and a > c and a > d:
    print('the number of a is greater')
elif b > a and b > c and b > d:
    print('the number of b is greater') 
elif c > a and c > b and c > d:
    print('the number of c is greater')
elif d > a and d > b and d > c:
    print('the number of d is greater')
else:
    print('the number is equal')
    
    