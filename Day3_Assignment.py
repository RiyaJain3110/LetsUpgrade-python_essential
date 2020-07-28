#First program
#Sum of first n numbers
n=int(input("Enter the number"))
i=0
sum=0
while (i<n):
  i=i+1
  sum=sum+i
  print(sum)
print("Sum of first n numbers is", sum)

"""
Output
Enter the number 10
sum of first n numbers is 55
"""


#Second Program
# Program to check whether the given number a is prime or not 
a = int(input("Enter a number: "))

# prime numbers are always greater than 1 

if a >=2: 
   for i in range(2,a): 
       if (a % i) == 0: 
          print(a,"is not a prime number")                 
          print("Beacuse",i,"times",a//i,"is",a)
          break 
   else: 
       print(a,"is a prime number") 
else: 
   print(a,"is not a prime number")

"""
Output
Enter a number: 6
Because 2 times 3 is 6
"""
