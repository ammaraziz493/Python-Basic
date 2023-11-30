# # map
# def cube(x):
#     return x * x * x
#
#
# print(cube(2))
# l=[1,2,3,4,5,6,7,8,9,0]
# newl=[]
# for item in l:
#     newl.append(cube(item))
# print(newl)
# newl1 = list(map(cube,l)) # it will perform same as above
# print(newl1)
#
# # Filter
# def filter_function(x):
#     return x>4
# print(filter_function(5))
# newnewl = list(filter(filter_function,l))
# print(newnewl)

from functools import reduce
number = [1,2,4,5,3]
sum = reduce(lambda x,y:x+y,number)
print(sum)


