my_set = {"Apple","Oranges","Cherry","Banana","Kiwi"}
print(my_set)

for x in my_set:
    print(x)
    
print("Kiwi" in my_set)

my_set.add("Grapes")
print(my_set)

my_set.update(["Bringle","Potatos"])
print(my_set)

print(len(my_set))

my_set.remove("Cherry")
print(my_set)
my_set.discard("Kiwi")
print(my_set)

#my_set.remove("Cherry")
my_set.discard("Kiwi")

my_set.pop()

my_set2 = {"Pen",1,2, (3,4,5)}
print(my_set2)

my_list = [11,22,33]
print(my_list)

my_set3 = set(my_list)
print(my_set3)

A = {'A','B','C',1,2,3}
B = {'B','C','D',2,3,4}

print(A.union(B))
print(A | B)

print(A.intersection(B))
print(A & B)

print(A.difference(B))
print(A - B)

print(B - A)

print(A.symmetric_difference(B))
print(A ^ B)

