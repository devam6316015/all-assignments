print("1) leap year or not")
year=int(input("enter any year"))
if (year%4!=0):
	print("year is not leap year")
else:
	print("year is  leap year")
	

print("2) dimensions are of square or rectangle")
l=int(input("enter length:"))
b=int(input("enter breadth:"))
if l==b:
	print("square ")
else:
	print("rectangle")
	

print("3) determine oldest and youngest")
a=input("enter the age of 1st person:")
b=input("enter the age of 2nd person:")
c=input("enter the age of 3rd person:")
if ((a>b)and(a>c)):
	print("1st person oldest")
elif((b>c)and(b>a)):
	print("2nd person oldest")
else:
	print("3rd person oldest")
#for youngest
if((a<b)and(a<c)):
	print("1st is youngest")
elif((b<c)and(b<a)):
	print("2nd is youngest")
else:
	print("3rd is youngest")
	

print("4) prize contest:")
n=int(input("enter the no. of student (1-200):"))
if((n>=1)and(n<=50)):
	print("no price")
elif((n>=51)and(n<=150)):
	print("wooden dog")
elif((n>=151)and(n<=180)):
	print("Book")
elif((n>=181)and(n<=200)):
	print("chocolates")
else:
	print("enter correct number")
	

print("5) Discount of 10%")
q=int(input("enter the units: "))
q1=q*100
if (q1>1000):
	dis=((10/q)*100)
	q1=q1-dis
	print("total bill cost after discount is: %d"%(q1))
else:
	print("no discount")
	
	


	
