my_Tupal = ("apple","cherry","Oranges")
print(my_Tupal)
print(my_Tupal[1])
print(my_Tupal[-1])

for val in my_Tupal:
    print(val)
    
#my_Tupal[2] = "Kiwi"
#del my_Tupal

print(len(my_Tupal))

my_Tupal2 = ("Banana",(1,2,3),["Tokyo","New Delhi"])
print(my_Tupal2[2][1])

my_Tupal2[2][1] = "New York"
print(my_Tupal2)

print("Banana" in my_Tupal2) #true
print("Cherry" in my_Tupal2) #false