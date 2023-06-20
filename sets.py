#set methods
s1={1,2,3}
s2={3,4,5}
print(s1.union(s2))
print(s2.union(s1))

print(s1.intersection(s2))
print(s2.intersection(s1))

print(s1.difference(s2))
print(s2.difference(s1))

print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))
