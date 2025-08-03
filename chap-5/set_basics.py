# set basics

s = set()  # empty set decleration, it cannot be initilized by empty {}
print(type(s)) # set
print(len(s)) # 0

s.add(1)
s.add(2)
s.add(2) # cannot add duplicate value
s.add(3) 
print(s) # {1, 2, 3}

s.remove(1)
print(s) # {2,3}

returned1 = s.pop()
print(returned1) # 2

returned2 = s.pop()
print(returned2) # 3

# Another set concept
s1 = {1,2,3}
s2 = {2,3,4}

print(s1.intersection(s2)) #{2,3}
print(s1.union(s2)) #{1,2,3,4}

