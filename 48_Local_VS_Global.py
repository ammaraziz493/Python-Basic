x = 4
print(x)
def Hello():
    x=5
    print(f"The local x is {x}")
    print("Hello Harry")
print(f"The global x is {x}")
Hello()
print(f"The global x is {x}")

a = 10
def my_function():
    global a
    a = 4 # it will change the global x value
    y = 10 # Local variable
    print(y)
my_function() # if we not call the function it will not change the value of x
print(a)
# print(y)