import random

def randoms(a):
    alen = len(a) 
    if alen >2: 
        for x in range(alen): 
            change = random.randrange(alen - 1) 
            
            change += change >= x 
            
            a[x], a[change] = a[change], a[x]
        return a
    else:
        print("Array too short")
a = [1,3,4,5,6,7,19,20,78,9837,87633]
print (randoms(a) )

#Big O is O(n *n)  

