print ("Welcome to Shopop Rite")

groceries=input("Please name your grocery list:")

groceries={}


def create_list():
	groceries={}
	choice=input("Would you like to add an item? Type Y or N:")
	if choice == "Y":
		add_item()
	else: 
		print_list()
	

def add_item():
	item=input("What item would you like to add?")
	quantity=input("How many " +item+ "s would you like to add?")
	groceries[item]=quantity
	choice=input("Would you like to update the quantity of the item? Type Y or N:")
	if choice=="Y":
		update_item()
	else:
		print_list()

def update_item():
	item=input("Please type the item you would like to update:")
	if item in groceries:
		quantity= input("What would you like the new quantity to be?")
		groceries[item]=quantity
		create_list
	else:
		print("Item not found. ")
		new_item=input("Would you like to add "+item+"? Y or N: ")
		if new_item=="Y":
			add_item()
		
def delete_item():
	choice=input("Would like to delete an item?Y or N: ")
	if choice=="Y":
		item=input("Which item? ")
		del groceries[item]
	else:
		create_list()

def print_list():
	print(groceries)
	

create_list()

