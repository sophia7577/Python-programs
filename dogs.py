class Dog(object):
  #attributes
  #class object attribute
  species = "mammal"
  
  def __init__(self,breed,size,color,name):
    self.breed = breed
    self.size = size
    self.color = color
    self.name = name
    
    #methods
  def bark(self):
    if self.size < 20:
	    print("woof")
    else:
        print("WOOF WOOF WOOF")
  

 
ellie = Dog("lab",60, "golden", "ellie")
nala = Dog("Yorkie", 10, "brown", "nala")
print(ellie.name)
print(ellie.species)
# print(ellie)
# print( type(ellie))
ellie.bark()  #methods always need parenthesis
 
print(nala.color)
nala.bark()
  
  

 