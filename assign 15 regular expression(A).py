#Q.1- Extract the user id, domain name and suffix from the following email addresses. 
#emails = "zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"

import re

#method-1
emails = "zuck26@facebook.com page33@google.com jeff42@amazon.com"
p=re.compile(r"([a-zA-Z0-9]+)@([A-Za-z0-9]+).([a-z]+)")
result=p.findall(emails)
print(result)

p=re.compile(r"($@.\\b)")
result=p.find(emails)

print(result.group())




#method-2
emails = "zuck26@facebook.com page33@google.com jeff42@amazon.com"
p=re.compile(r"(.*)@(.*).(...) (.*)@(.*).(...) (.*)@(.*).(...)")
result=p.match(emails)


# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
# print(result.group(4))
# print(result.group(5))
# print(result.group(6))
# print(result.group(7))
# print(result.group(8))
# print(result.group(9))

t1=(result.group(1),result.group(2),result.group(3))
t2=(result.group(4),result.group(5),result.group(6))
t3=(result.group(7),result.group(8),result.group(9))

l=[t1,t2,t3]
print(l)
