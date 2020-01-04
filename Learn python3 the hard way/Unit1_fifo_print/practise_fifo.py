from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here is your file >: {filename}")
print(txt.readline(),end="")
print(txt.readline())
print(txt.readline())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again)
print(txt_again.read())


# from sys import argv
# script, filename = argv

# print(f"We're going to erase {filename}.")
# print("If you don't want that, hit CTRL-C (^C).")
# print("If you want to do that,hit RETURN.")

# input("?")

# print("Opening the file...")
# # "w" mode is deleting all context of file.There's no need to add target.truncate()
# target = open(filename,'w+')

# print("Truncating the file. Goodbye!")
# # target.truncate()

# print("Now I'm going to ask you for three lines.")

# line1 = input("Line1: ")
# line2 = input("Line2: ")
# line3 = input("Line3: ")

# print("I'm going to write these to the file.")
# # target.write(line1)
# # target.write("\n")
# # target.write(line2)
# # target.write("\n")
# # target.write(line3)
# # target.write("\n")

# # target.write(f"{line1}\n{line2}\n{line3}\n")

# target.write("{}\n{}\n{}\n".format(line1,line2,line3))

# print("And finally, we close it.")
# print(target.read())
# target.close()