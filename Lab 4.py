#задание 1
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = my_list[::2]
print(even)

#задание 2
def greatest(list):
    my_list =[ ]
    i=0
    k = int(input("enter a number"))
    for i in range(len(my_list)):
        if my_list[i] > k:
           greatest = my_list[i]
        else:
            print("greatest does not exist")
    return greatest
    
#задание 3
def swap_min_max(a):
    max_index =a.index(max(a))
    min_index =a.index(min(a))
    ma=max(a)
    mi=min(a)
    a[max_index]=mi
    a[min_index]=ma
    a=[ ]
    print(a)
    return swap_min_max(a)
    
#задане 4
def value(dict,key):
    return dict[key]
    
#задане 5

from math import pi
default_radius = 5
def circle_area(r = default_raduis):
    return(pi*(r**2))
def circle_perimeter(r = default_radius):
    return 2*pi*r
   
default_l = 15
def square_area(l =default_l):
    return l*l 
def square_perimeter(l = default_l):
    return 4*l
    
from math import sqrt
p = 7
q = 2
r = 8
def triangle_area(p=p, q=q, r=r):
    return sqrt(4*p**2*q**2 -(p**2+q**2-r**2)*2)/4
def triangle_perimeter(p=p, q=q, r=r):
    return p+q+r
    
from figures.circle.code import *
from figures.triangle.code import *
from figures.square.code import * 
