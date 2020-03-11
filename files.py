myFile = open('myfile.txt', 'w')

# get some info
print("Name: ", myFile.name)
print("Is closed: ", myFile.closed)
print("Opening Mode: ", myFile.mode)

# write to file
myFile.write("I love python")
myFile.write("I love Django")
myFile.close()

# append to file
myFile = open("myfile.txt", 'a')
myFile.write(" I also like PHP")
myFile.close()

# Read from a file
myFile = open('myfile.txt', 'r+')
text = myFile.read(20)
print(text)
