l=[2,3,5,"Ammar",True]
print(l)
print(l[0])
print(l[1])
print(l[2])
if 7 in l:
    print("yes")
else:
    print("NO")
if "Am" in "Ammar":
    print("Yes")
else:
    print("No")
print(l[:])
print(l[1:-1]) #len(l)-1=4
print(l[1:4])
print(l[1:4:2])  #Jump index it will jump 2 times

# List Comprehension
lst=[i*i for i in range(10)] # i value start from 0*0
print(lst)
lst=[i for i in range(10) if i%2==0] # it will print only even numbers
print(lst)
# Examples
names=["Ammar","Ahmad","Ali"]
name_a=[item for item in names if "m" in item]
print(name_a)
name_l=[item1 for item1 in names if len(item1)>3]
print(name_l)