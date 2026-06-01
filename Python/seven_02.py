# file  = open(r"C:\Users\sayed ahmad shah\Desktop\data-engineering-journey\Python\notes.txt","w")

# file.write("This is a test file for notes.\n")

# file.close()

# file  = open(r"C:\Users\sayed ahmad shah\Desktop\data-engineering-journey\Python\notes.txt","r")

# content = file.read()
# print(content)


# file  = open(r"C:\Users\sayed ahmad shah\Desktop\data-engineering-journey\Python\tasks.txt","w")

# file.write("This is a test file for notes.\n this is a new line of text.\n and this is another line of text.")


# file.close()
# file  = open(r"C:\Users\sayed ahmad shah\Desktop\data-engineering-journey\Python\tasks.txt","a")

# file.write("\nThis is an appended line of text.")
# file.close()
# file  = open(r"C:\Users\sayed ahmad shah\Desktop\data-engineering-journey\Python\tasks.txt","r")

# # content = file.read()
# # print(content)

# for line in file:
#     print(line.strip())

# file.close()


import os

print("Current working directory:", os.getcwd())
print("List of files in the current directory:", os.listdir(os.getcwd()))
os.mkdir("new_directory")   

