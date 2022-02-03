choice = int(input('1 - addition \n2 - subtraction \n3 - multiplication \n4 - division: \n'))
if choice == 1:
    a = int(input('first number '))
    b = int(input('second number '))
    sum = a+b
if choice == 2:
    a = int(input('first number '))
    b = int(input('second number '))
    sum = a-b
if choice == 3:
    a = int(input('first number '))
    b = int(input('second number '))
    sum = a*b
if choice == 4:
    a = int(input('first number '))
    b = int(input('second number '))
    sum = a/b

print(sum)
input('press enter to close')