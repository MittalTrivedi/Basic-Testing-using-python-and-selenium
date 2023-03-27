mylist = ["Tokyo","New York","India"]
print(mylist)

print(mylist[1])

for val in mylist:
    print(val)
    
mylist[1] = "USA"

print(mylist)

mylist.append("Canada")
print(mylist)

mylist.insert(4,"UK")
print(mylist)

mylist.remove("Tokyo")
print(mylist)

mylist.clear()
print(mylist)

fruits = ["apple","Oranges","Peaches"]
print(fruits)
fruits.reverse()
print(fruits)

mylist1 = ["apple",1,2,3.0]
print(mylist1)
mylist2 = ["apple",[1,2,3,4.5],['a','b','c']]
print(mylist2[1][3])
print(mylist2[2][2])