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


# import os

# print("Current working directory:", os.getcwd())
# print("List of files in the current directory:", os.listdir(os.getcwd()))
# os.mkdir("new_directory")   

# import shutil

# shutil.copy("tasks.txt", "new_directory/tasks_copy.txt")
# os.remove("new_directory/tasks_copy.txt")



# import sys



# def count_lines(file_path):
#     try:
#         with open(r"C:\Users\sayed ahmad shah\Desktop\data-engineering-journey\Python\notes.txt","r") as file:
#             lines = file.readlines()
#             return len(lines)
#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' was not found.")
#         return None
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None

# if __name__ == "__main__":
#     file_path = sys.argv[1]
#     line_count = count_lines(file_path)
#     print(f"The number of lines in the file is: {line_count}")



# import sys

# def search_word(word, string):
#     return string.count(word)

# if __name__ == "__main__":
#     file_name = sys.argv[1]
#     word_to_search = sys.argv[2]
#     with open(file_name, "r") as file:
#         string = file.read()
#         count = search_word(word_to_search, string)
#         print(f"The word '{word_to_search}' appears {count} times in the file.")

