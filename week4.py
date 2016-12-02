


anumber = int(input("Pleae enter number: "))
list = [6, 7, 27, 36, 40, 43, 61, 64, 78, 95]

def bins(bnum, array):
   
    middle = len(array)//2
    try:
        if array[middle-1] == bnum:
            return True
        else:
            if array[middle-1] > bnum:
                return bins(bnum, array[:mid-1])
            elif array[middle-1] < bnum:
                return bin(bnum, array[middle:])
            return False
    except IndexError and RecursionError: 
        return False

print("is %d in the list? Answer: %s" % (anumber, bins(anumber, list)))









