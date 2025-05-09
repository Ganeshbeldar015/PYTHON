#WAP to check if a number entered by the user is odd or even 
num = int(input("Enter number : "))
if(num % 2== 0):
    print("Even")
else:
    print("odd")
 
#  WAP to find greatest of 3 number entered by the user.

a = int(input("Enter  first number : "))
b = int(input("Enter  second number : "))
c = int(input("Enter third number : "))

if(a >= b and a>=c):
    print("First number is largest : ",a)
elif(b>=c):
    print("Second number is largest : ",b)
else:
    print("third number is largest : ",c)
    
# WAP TO CHECK ia number is multiple of 7 or not .
num1 = int(input("Enter the number :"))
if(num1 % 7 == 0):
    print("Number is multiple of 7")
else:
    print("Number is not multiple of 7")