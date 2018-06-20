print(" create a circle class and init with radius")
class circle:
	radius=5
	def get_area(self):
		print("Area of cirle is: ",3.14*self.radius*self.radius)
	def get_circumference(self):
		print("circumference of circle: ",2*self.radius*3.14)
obj=circle()
obj.get_area()
obj.get_circumference()



print("class student and init with name and rollno")
class student :
	name = "devam"
	roll_no=6316015
	def display(self):
		print("name is:",self.name)
		print("roll no :",self.roll_no)
obj=student()
obj.display()


print("create temperature class and make two methods in it")
class temperature:
	def convert_farenheit(self):
		c=int(input("enter the temp. in celcius: "))
		d=1.8*c+32
		print("temp. in farenheit: ",d)
	def convert_celcius(self):
		f=int(input("enter the temp. in farenheit: "))
		r=(f-32)/1.8
		print("temp. in celcius :",r)
obj=temperature()
obj.convert_farenheit()
obj.convert_celcius()



print(" class moviedetails  and init with it movie name,artist name,release year")
class moviedetails:
	movie_name="sanju"
	artist_name="ranveer kapoor"
	release_date="28-6-2018"
	def display(self):
		print("detail:\n","\n",self.movie_name,"\n",self.artist_name,"\n",self.release_date,"\n")
	def update(self):
		movie_name="race3"
		artist_name="paaji"
		release_date="5-7-2018"
		print("updated details:\n","\n",movie_name,"\n",artist_name,"\n",release_date)
		
obj=moviedetails()
obj.display()
obj.update()



print(" class expenditure and initialize it")
class expenditure:
	expenditure=3000000
	savings=1000000
	def display(self):
		print("expenditure and savings:",self.expenditure,self.savings)
	def total(self):
		total_salary=self.expenditure+self.savings
		return total_salary
	def salary(self,a):
		self.total_salary=a
		print("total salary: ",self.total_salary)
obj=expenditure()
obj.display()
a=obj.total()
obj.salary(a)
		