#can vote & apply for licence
age = int(input("Enter age: "))
if(age >= 18):
    print("can vote & apply for licence")
else:
    print("can not vote & apply for licence")    

#signals
light = input("Enter the colour : ")
if(light == "red"):
    print("STOP")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("No Found ")
    
#Grade student based on marks
marks = int(input("Enter Student Marks : "))
if(marks >= 90 ):
   grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks <80 ):
    grade = "C"
else:
    grade = "D"
print("Grade of the student is :",grade)


#nesting
age = int(input("Enter age : "))
if (age >= 18):
    if(age >= 80):
        print("can not drive")
    else:
        print("can drive")
else:
    print("can not drive")