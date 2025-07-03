# Opening a File
with open(r'python.txt', 'r') as file:
    content = file.read()
    print(content)
    
# Reading a File
file = open(r'python.txt', 'r')
content = file.read()
print(content)
file.close()

# Writing to a File
file = open("python2.txt", "w")
file.write("Hello, World!")
file.close()

# Writing to a File in Append Mode
file = open('python append.txt', 'a')
file.write("This will add this line")
file.close()