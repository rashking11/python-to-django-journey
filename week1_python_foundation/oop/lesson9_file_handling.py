# File handling practice

#Write to file

with open("test.txt", "w") as file:
    file.write("Hello Rashid\n")
    file.write("Learning file handling\n")

#Append to file

with open("test.txt", "a") as file:
    file.write("This is an appended text\n")

#Read from file
with open("test.txt", "r") as file:
    content = file.read()
    print(content)

#Read line by line

with open("test.txt", "r") as file:
    for line in file:
        print("Line", line.strip())

#Error handling

try:
    with open("unknown.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exit")

