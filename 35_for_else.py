for i in range(5):
    print(i)
else:
    print("There is no i")
for i in range(6):
    print(i)
    if i==4:
        break
else: # it will not execute because loop is break without successfully execute
    print("NO break")
for x in range(5):
    print("x in for loop {}".format(x+1))