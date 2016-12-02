
num = False
while num == False:
    try:
        parameter = int(input("Enter Number: "))
        num = True
    except ValueError:
        print("Only enter positive number.")

rParameter = (parameter)**0.5 
s = (int(rParameter))**2 
print(s)

