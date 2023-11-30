# Reading a file
# f = open("myfile.txt", "r")
# text = f.read()
# print(text)
# f.close()
# writing a file
f = open("myfile.txt","a")
text = f.write("This is a new line")
f.close()
with open("myfile.txt", "a") as f:
    f.write("Hi i am open")