# a = 4
# b = "4"
a = [1, 2, 4] # tuple is mutable
b = [1, 2, 4]
print(a is b)  # exact location of object in memory
print(a == b)  # value
a = 3 # it is constant so python do not another memory
b = 3 # immutable
print(a is b)  # exact location of object in memory
print(a == b)  # value
