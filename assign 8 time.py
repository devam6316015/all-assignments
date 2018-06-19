# print("1. what is time tuple")
# We represent time in a way that's easy for us to understand. However, python stores it in tuples.
# These python tuples are made of 9 numbers.

# Index   Field            Domain of values
# 0       Year             (4 digit) ex-1995
# 1       Month            1 to 12
# 2       Day              1 to 31
# 3       Hour             0 to 23
# 4       Minute           0 to 59
# 5       Second           0 to 61(60/61 are leap seconds)          
# 6       Day of week      0 to 6(mon to sun)
# 7       Day of year      0 to 366(julian day)
# 8       DST              -1,0,1

# this tuple has an equivalent struct_time structure.


print("2. program to get formatted time.")
import time
format=time.asctime(time.localtime(time.time()))
print("formated time: ",format)


print("3. extract month from the time")
from datetime import datetime 
p=datetime.now()
print(p)
print(p.strftime("%B"))


print("4. extract day from the time")
p=datetime.now()
print(p)
print(p.strftime("%A"))


print("5. extract date from the time")
import datetime
p=datetime.date.today()
print(p)
print(p.day)


print("6. print time using loactime method")
import time
print(time.localtime())


print("7. factorial using math package fn")
import math
a=math.factorial(int(input("enter any number: ")))
print("factorial =",a) 



print("8. GCD of a number input by user using math package fn")
import math
a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
print("GCd: ",math.gcd(a,b))



print("use OS package")
import os
print(os.getcwd())
print(os.environ)