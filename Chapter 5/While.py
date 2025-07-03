# while condition :
    #some work
    
#print Ganesh in 5 times
count =1
while count <= 5:
    print("Ganesh")
    count += 1
print(count)

#Print number from 1 to 100
i = 1
while i<= 100:
    print(i)
    i+=1
print("Loop end")
#Print number from 100 to 1
i=100
while i>= 1:
    print(i)
    i-=1

#Print the Multiplication table of a number n

n = int(input("Enter the number:"))
i = 1
while i<= 10:
    print(n*i)
    i += 1

# print the element  of the  following list using  a loop:
    # [1,4,9,16,25,36,49,64,81,100]

num = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(num):
    print(num[i])
    i += 1

# search for a number  x in thin tuple using loop

num = [1,4,9,16,25,36,49,64,81,100]
x = int(input("Enter the number: "))
i = 0
while i < len(num):
   if(num[i] == x):
       print("FOUND at idx",i)
   else:
       print("NOT FOUND")
   i += 1
