for i in range(12):
    # print("5 x",i+1,"=",5*(i+1))
    if(i==9):
        break

for i in range(12):
    if (i == 9):
        print("Skip the iteratiion")
        continue
    print("5 x",i+1,"=",5*(i+1))

# Emulate do while loop
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break
