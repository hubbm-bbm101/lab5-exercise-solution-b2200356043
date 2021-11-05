import random


n = random.randint(0,10)
v = int(input("Number: ")) 
while n != v:
    if n < v:
        print("decrease your number")
    else:
        print("increase your number")
    v = int(input("Number: ")) 

