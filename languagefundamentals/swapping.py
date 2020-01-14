print("case 1")
print("case 1 before swapping")
no1=10
no2=20
print("no1=",no1,"no2=",no2)
temp=no1+no2
no1=temp-no1
no2=temp-no2
print("case 1 after swapping")
print("no1=",no1,"no2=",no2)


print("\ncase 2")
no1=10
no2=20
print("case 2 before swapping")
print("no1=",no1,"no2=",no2)
no1=no1+no2
no2=no1-no2
no1=no1-no2
print("case 2 after swapping")
print("no1=",no1,"no2=",no2)


print("\ncase 3")
print("case 3 before swapping")
no1=10
no2=20
print("no1=",no1,"no2=",no2)
temp=no1
no1=no2
no2=temp
print("case 3 after swapping")
print("no1=",no1,"no2=",no2)