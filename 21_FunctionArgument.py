# Default Argument
def average(a=3,b=9):
    print("The averge of two number is ",(a+b)/2)
average() # It will take default argumets
average(3,4) # while it will take other arguments than default arguments
average(4) # it will also take only one argument while other is default
#Keyword Argument
average(b=3,a=4) # we will change the position of argument
#Required Argument
def average1(a,b,c=1):
    print("The averge of two number is ",(a+b+c)/2)

average1(1,3)
# Variable lengthVariable
def average2(*numbers):
    print(type(numbers)) # it will take numbers as tuple
    sum=0
    for i in numbers:
        sum =sum +i
    print("Average is :",sum/len(numbers))

average2(1,2)
