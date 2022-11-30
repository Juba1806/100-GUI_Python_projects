#!/usr/bin/env python3
from cowsay import cow

print("guess a number from 0 to 10 ")

x = 1 
y = 7 
z = 9 

q = 0 


a = 0 
while a  < 3:
    number_1 = int(input("enter the number\n"))
    if number_1 == x or number_1 == y or number_1 == z:
        print("kayna")
        q += 1 

    else:
        print("iwa nn")
    a  += 1 

print("\n\n\n")
if q == 3:
    print("rak nadi Bro")
else:
    print(cow("nn rak hmar"))
