print("1. calculate area of cirle using fn")
def area(r):
	a=3.14*r*r
	print("area of circle",a)

area(int(input("enter the radius :")))


print("2. perfect or not")
def perfect(num):
	sum=0
	for x in range(1,num):
		if num%x==0:
			sum=sum+x
	if sum==num:
		print(num,":is a perfect number")
for x in range(1,1001):
	perfect(x)
	
	
print("3. print multiplication table of 12 using recursion")
def rec(x,y):
	if y<=10:
		t=x*y
		print(t)
		y+=1
		rec(x,y)
rec(12,1)


print("4. calculate power of a number raised to other(a^b) using recursion")
count=0
def power(a,b):
	if b==1:
		return a
	else:
		p=a*power(a,b-1)
		return p
a=int(input("enter base:"))					
b=int(input("enter index of base"))
print(power(a,b))

print("5. factorial of number")
def fact(x):
	if x==1 or x==0:
		return 1
	else:
		f=x*fact(x-1)
		return f
d={}
for x in range(5):
	num=int(input("enter any number: "))
	a=fact(num)
	d[num]=a
print(d)