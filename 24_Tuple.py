tup=(1,2,3,6,34,56,65)
print(tup)
t=(1) # it will print as integar
print(type(t),t)
t1=(1,)
# t1[0]=45 # it will generate an erro becasue tuple is unchangeable
print(type(t1),t)
if 1 in tup:
    print("yes")
print(tup[1:6:2])
tup2=tup[1:6:2]
print(tup2)
