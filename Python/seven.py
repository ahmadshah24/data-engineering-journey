# file = open(r"C:\Users\sayed ahmad shah\Desktop\data-engineering-journey\Python\shah.txt","r")

# content = file.read()

# print(content)

# file.close()


# file = open(r"C:\Users\sayed ahmad shah\Desktop\data-engineering-journey\Python\sayed.txt","w")

# string = '''
# sayed is a good boy and knows python programming language.
# '''

# file.write(string)
# file.close()
# file = open(r"C:\Users\sayed ahmad shah\Desktop\data-engineering-journey\Python\sayed.txt","a")

# string = '''
# and he live in richmond
# '''

# file.write(string)
# file.close()



# try:
#     file = open(r"C:\Users\sayed ahmad shah\Desktop\data-engineering-journey\Python\shah.txt","r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found")


# try:
#     file = open(r"C:\Users\sayed ahmad shah\Desktop\data-engineering-journey\Python\shah.txt","r")
#     for line in file:
#         print(line.strip())
#     file.close()
# except FileNotFoundError:
#     print("File not found") 


# with open(r"C:\Users\sayed ahmad shah\Desktop\data-engineering-journey\Python\shah.txt","r") as file:
#     content = file.read()
#     print(content)  
#     # no need to close the file explicitly, it will be closed automatically when the block is exited


# import os

# all_files = os.listdir(r"C:\Users\sayed ahmad shah\Desktop\data-engineering-journey")

# print(all_files)

# print("Current working directory:", os.getcwd())

import shutil
# this is way powerful then os module because it can copy, move, delete files and directories


