print("1.  write a program to read last n lines of a file")
f=open("test.txt","r",encoding="utf8")
content = f.readlines()
f.close()
n=int(input("enter"))
print("last lines are :")

while n > 0:
    print(content[-n])
    n-=1



print("Q.2- Write a Python program to count the frequency of words in a file")
f=open("test.txt","r",encoding="utf8")
content=f.read()
words=content.split()

uniwords=set(words)
for word in uniwords:
	print(word, words.count(word))
	
	
print("\nQ.3- Write a Python program to copy the contents of a file to another file")

with open("test.txt","r",encoding="utf8") as f1:
    with open("test1.txt",'w') as f2:
        for line in f1:
           f2.write(line)
		   
		   
print("\nQ.4- Write a Python program to combine each line from first file with the corresponding line in second file.")

with open("test.txt","r",encoding="utf8") as f1:
	content1=f1.readlines()
	n1=len(content1)

with open("abc.txt","r",encoding="utf8") as f2:
	content2=f2.readlines()
	n2=len(content2)
i=0
for x in range(min(n1,n2)):
	print(content1[i]+content2[i])
	i = i+ 1
	
	
	

print("\nQ.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.")
import os
import random
list2=[]
n=int(input('How many random numbers:'))
os.remove("random.txt")
with open("random.txt","w",encoding="utf8") as afile:	
	for i in range(n):	#insert n random number as per user
		list2.append(random.randint(1, 100))
	print(list2,"#")
	for x in range(len(list2)):		#write numbers in file
		afile.write(str(list2[x])+"\n")		#"\n"-print number line by line
	afile.seek(0)
with open("random.txt","r+",encoding="utf8") as f1:
	list1=f1.readlines()
	for i in range(len(list1)):
		list1[i]=int(list1[i])	#type casting
	list1.sort()	#sorting
	print(list1)
with open("random_sorted.txt","w",encoding="utf8") as f2:
	for x in list1:
		f2.write(str(x)+"\n")
		
