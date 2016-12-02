num = False
trl = 0


while num == False:
    try:
        factorial = int(input("Enter Number: "))
        num = True
    except ValueError:
        print("Enter integer (do not write anything else such as words!)")


while factorial >= 1 :
    factorial = factorial/5
    trl = trl + int(factorial) 

print(trl)





