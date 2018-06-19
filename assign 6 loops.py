# print("1) Take 10 integers and print")
# x=[]
# for i in range (10):
	# x.append(int(input("enter 1-10 numbers"))) 
# for i in x:
	# print(i)
	

# print("2) An infinite loop")
# a=5
# while a<10:
	# print("lol")


# print("3) list of integer thn square and print")
# a=[]
# sqr=[]
# for i in range(5):
	# z=int(input("enter 1-5 numbers"))
	# a.append(z)
	# x=z*z
	# sqr.append(x)
# print(a)
# print(sqr)


# print("4) Three list of different types")
# li=[3,5,'a','b',3.2,'c',2,2.9]
# l1=[]
# l2=[]
# l3=[]
# for x in li:
	# if(type(x)==int):
		# l1.append(x)
	# elif(type(x)==float):
		# l2.append(x)
	# else:
		# l3.append(x)
# print(li)
# print(l1)
# print(l2)
# print(l3)


# print("5) range 1-100 even an odd")
# p=[]
# q=[]
# for i in range(1,101):
	# if(i%2==0):
		# c=i
		# p.append(c)
	# else:
		# d=i
		# q.append(d)
# print(p)
# print(q)


# print("6) print * in patterns")
# for i in range(0,4):
	# for a in range(0,i+1):
		# print('*',end='')
	# print('\n')
	
 #print("7) create a user defined dictionary and gets keys corresponding to the value using loops")
 
# r={}
# for x in range(10):
	# a=input("Enter a key: ")
	# b=input("enter a value: ")
	# r[a]=b
# print(r)




print("8)  take input thn search and delete that element")
l=[]
flag=0
for x in range(9):
	l.append(int(input("enter the no:")))
print(l)

s=int(input("enter no. you want to search and delete:"))

for x in l:
	if x==s:
		l.remove(x)
		flag=1
print(l)
if flag==0:
	print("no. not found")


	
	
	


