a = [34, 56, 78, 34, 4, 5]
for index,a in enumerate(a,start=1): # if we not write start it will start from 0 and replace 78 
    print(a)
    if index==3:
        print("Harry is awesome")