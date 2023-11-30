s={1,2,3,5}
s2={4,6,3,8}
print(s.union(s2))
print(s,s2)
s.update(s2)
print(s,s2)
print(s.intersection(s2))
s.intersection_update(s2)
print(s)
# symetric difference
set1={"Pak","Ind","Aus"}
set2={"Pak","Afg"}
set3=set1.symmetric_difference(set2) # Print all value which are not common
print(set3)
# Difference
set4 = set1.difference(set2)
print(set4)
# set1.difference_update(set2)
print(set1)
# isdisjoint
print(set1.isdisjoint(set2)) # when there is no intersection in sets
#superset
print(set1.issuperset(set2)) #  If values of second set match the first set than it will be a super set
s={1,2,3}
s1={1,2}
print(s.issuperset(s1))
print(s1.issubset(s))
#add
s.add(5)
print(s)
#remove/discard
s.remove(5) # if a elment is not present in a set remove will generat an error while discrad not
print(s)
#pop
p=s.pop() # Random value will pop from the set
print(p)
# del
# del s
print(s)
# clear
s.clear() # it will delete the all values but not the set
print(s)

s={"ab" ,2, 3, 5 ,5}
if "ab" in s:
    print("1 is present")
