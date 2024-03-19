a=set(input("enter elements in set a:"))
b=set(input("enter elements in set b:"))
c={(x,y) for x in a for y in b}
print(c)
