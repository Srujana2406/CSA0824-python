m=int(input("enter number of vehicles"))
n=int(input("enter y=the number of children"))
x=m%n
if x==0:
    print("you are so lucky")
elif x!=0 and x%2!=0:
    print("mr.peter gets",x,"vehicles")
elif x!=0 and x%2==0:
    print("mr.peter gets",x,"vehicles.he is lucky")
