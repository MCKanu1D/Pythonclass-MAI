#Задание 1

a = True
b = False
print(a and b)
print((a and b) or b)
print((a and b) or not (a and b))
print(a and b or not (a or b) or b)
print(b and b or not a and (a or b or a) or not(a or b))
print(1<<2)
print(1 & 0 | 1 >> 1)
print(1 & 0 | 1 >0)
print(0b101 & 0b111 ^ 0b111 | 0b010)

#Задание 2

a = int(input("type a number"))
b = int(input("type another number"))
if (a < b) :
    print(a)
elif (a == b):
    print(a)
else:
    print(b)
    
    #Задание 3
    
a = float(input("enter first number: "))
b = float(input("enter second number: "))
c = float(input("enter third number: "))
if (a >= b) and (a >= c) :

    print(a)
elif(b>=a) and (b>=c) :
    print(b)
else:
    print(c)
    
    #Задание 4
    
a = int(input("enter number1: "))
b = int(input("enter number2: "))
c = int(input("enter number3: "))

if a== b and b== c:
    print("One unique number")
elif (a == b) or (b == c) or (a == c):
    print("Two unique numbers")
else:
    print("3 unique numbers")