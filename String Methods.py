#String are immutable
a = "Harry"
print(a.upper()) # It will not change the original string it will create a new string
print(a.lower())
#rstrip -> remove any trailing character
a="Harry! !!!! Harry!!!"
print(a.rstrip("!"))
b="!!!harry"
print(b.rstrip("!")) # it will not remove the leading character
print(a.replace("Harry", "Honda"))
# Who to convert a string into a list
print(a.split(" ")) # it will return a list
# Captilize
blogHeading = "inroduction to jS this is js "
print(blogHeading.capitalize()) # It will convert first letter to Upper case other laters to lower case
# Centralize Method
str1 = "Welcome to the Console!"
print(len(str1))
print(str1.center(50))
print(len((str1.center(50)))) # it will convert the string to 50 character
# Count
str1="Ammar Ammar Ammar"
print(str1.count("Ammar")) # It will count the numbers of time a word repeat
# endsWith
str= "Welcome to the console !!!"
print(str.endswith("!!!"))
print(str.endswith("to",4,10))
# find
a = "He is name is"
print(a.find("is")) # It will return the first occurrence
print(a.find("isshh")) # It will return -1
# print(a.index("isshhh")) # it will give an error
# isalnum
a = "WelocmetoConsole0"
print(a.isalnum())
print(a.isalpha())
# islower
print(a.islower()) # check if all character are in lower case
# isprintable

g = "hi i am harry\n"
print(g.isprintable())
# isspace
print(g.isspace())
# is title
t = "This Is A Title"
print(t.istitle()) # check all the words start with upper case
#start withs
r = "Python is an interprated languge"
print(r.startswith("Python"))
print(r.swapcase())
print(r.title())