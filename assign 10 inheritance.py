print("basic inheritance- \n")
class animal:
	def show1(self):
		print("animal class call")
class tiger(animal):
	pass
		
t=tiger()
t.show1()



print("checks the output of code\n")
class A:
	def f(self):
		return self.g()
	def g(self):
		return'A'
class B(A):
	def g(self):
		return 'B'

a=A()
b=B()
print (a.f(), b.f())
print (a.g(), b.g())

class cop:
    def add(self,name,age,work_exp,designation):
        self.name=name
        self.age=age
        self.work_exp=work_exp
        self.designaation=designation
    def display(self):
        print("name : ",self.name)
        print("age : ",self.age)
        print("work experience : ",self.work_exp)
        print("designation : ",self.designaation)
    def update(self,name,age,work_exp,designation):
        self.name = name
        self.age = age
        self.work_exp = work_exp
        self.designaation = designation

class mission(cop):
    def add_mission_details(self,mission):
        self.mission=mission
        print(self.mission)

m1= mission()
m1.add_mission_details("assigned to HCL")
m1.add("Devam",18,5,"manager")
m1.display()
m1.update("dheeraj",25,12,"gateman")
m1.display()
		

		
class shape:
	def __init__(self,l,b):
		self.length=l
		self.breadth=b
	def area(self):
		self.area=self.length*self.breadth
		print(self.area)
class rectangle(shape):
	pass
class square(shape):
	pass
s=square(4,6)
r=rectangle(6,8)
s.area()
r.area()
