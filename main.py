# Write a program to append a file with the contents of another file  

file1 = open("file1.txt", "w")
file1.writelines(" Its language constructs as well as its object-oriented")
file1.close()

file2 = open("file2.txt","w")
file2.writelines("Python is an interpreted high-level general-purpose programming language.")
file2.close()

file1 = open("file1.txt", "r")
file2=open("file2.txt","a")
file2.write(file1.read())
file1.close()
file2.close()