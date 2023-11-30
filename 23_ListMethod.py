l=[45,64,1,2,3,4,5,1]
print(l)
# l.append(7) # it will add at the end of the list
# l.sort() # it will sort the array in ascending order
print(l)
# l.sort(reverse=True) # it will sort the array in descending order
# print(l)
# l.reverse()
# print(l.index(1)) # it will give the index of value 1
print(l.count(1)) # count the number of appearance in list of a value
print(l)
m=l
m[0]=0 # it will change the original list
print(l)
# if you do not want to change the list
l=[1,2,4,5,6]
m=l.copy()
m[0]=0
print(l)
l.insert(1,899) # add 899 on index 1
print(l)
m=[900,100,800]
k= l+m
print(k) # concatenate two list without change the original list
l.extend(m) # add the value of m in l
print(l)
