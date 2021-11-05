def isEven(a):
    if a%2 == 0:
        return True
    else:
        return False

n = int(input("N: "))

if isEven(n):
    print("Sum of odd numbers: " + str((n/2)**2)) 
    print("Average of even numbers: " + str( (((n)/2)*(n+1))/n ))
else:
    print("Sum of odd numbers:" + str(((n+1)/2)**2))
    print("Average of even numbers: " + str( (((n)/2)*(n+1))/n ))

