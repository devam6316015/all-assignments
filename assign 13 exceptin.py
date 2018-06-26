print("1) name and handle the exception\n")
# a=3
# if a<4:
	# a=a/(a-3)
	# print(a)
try:
	a=3
	if a<4:
		a=a/(a-3)
except Exception as e:
	print(e)

	
	
print("\n2)name and handle the exception")
# l=[1,2,3]
# print(l[3])
try:
	l=[1,2,3]
	print(l[3])
except Exception as e:
	print(e)
	
	
print("\n3) what will be the output of code")
try:
	raise NameError("heyy broo")
except NameError as e:
	print("An exception")
	print(e)
	
	
print("\n4) what will be the output of code")
def AbyB(a,b):
	try:
		c=((a+b)/(a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

AbyB(2.0,3.0)
AbyB(3.0,3.0)


print("\nwrite program to show -\n 1)Import error \n 2)Value Error \n 3) IndexError")
try:
	print("\n 1) Import error")
	from Devam import *
except Exception:
	print("import error")

	
	
try:
	print("\n2 value error")
	x=int(input("enter any int number: "))
	print(x)
except Exception as e:
	print(e)


	
try:
	print("\n 3)index error")
	li=[2,4,7,9]
	print(li[10])
except Exception as e:
	print(e)


	
	
print("6) create a user defined exceptiom code")
class AgeTooSmallError(Exception):
	pass
while True:
	try:
		x=int(input("enter your age: "))
		if x<18:
			raise AgeTooSmallError
		break
	except AgeTooSmallError:
		print("age is short!!!")
print("entered the correct age")
		