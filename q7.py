
Pseudocode

if n > 1:
 
   for i = range(2,n):

      if n reminder i == 0:
out n




Implementation 

n = int(input("Please enter number to check that number is prime or not: "))

if n > 1:
 
   for i in range(2,n):

      if (n % i) == 0:
         print(n,"number you entered is not a prime number")

         break
   else:

      print(n,"number is prime number")
