class Circle(object):
	pi=3.14
	
	def __init__(self,radius):
		self.radius=radius
		
	def circumference(self):
		#radius=input("Please inout your radius: ")
		return self.pi*self.radius*2
		
	def area(self):
		#radius2=input("Please inout your radius: ")
		return self.pi*self.radius**2
		
big_circle=Circle(10)
print(big_circle.circumference())
print(big_circle.area())