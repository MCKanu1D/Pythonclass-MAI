#Задание 1

A = [1, 2, 0, 4, 5, 1, 10, 20, 0, 2]

def summand(A):
    list = A
    sum = 0
    
    for i in range(len(A)):       
        sum += A[i]
        
    print(f'суммa равнa {sum}')
         
       
summand(A)

print("")



#Задание 2

def zeroesin(A):
    zeroes = A.count(0)
    print(f'в массиве есть {zeroes} нуля')
    
zeroesin(A)
    
    
print()    




#Задание 3

def ladder(n):
        for i in range(n):
            for j in range(i+1):
                print(j + 1, end=' ')
            print()
        

ladder(5)

print()

#Задание 4

def pyramid(n):
    
    for i in range(1, n + 1):
        for j in range(1, n + 1 - i):
            print(' ', end = ' ')
            
        for j in range(1, i + 1):
            print(j, end=' ')
            
        for j in range(i - 1, 0, -1):
            print(j, end=' ')
        print()
            
pyramid(5)                
