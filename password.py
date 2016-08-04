from hashlib import*

loginDict={}

def makehash(password1):
	return sha256(password1. encode('utf-8')).hexdigest()
	
	
	
def login(username1,hash):
	loginDict[username1]=hash
	print("Thank you! You are signed up.")

def prompt():
	username=input ("Enter username: ")
	password=input("Enter password: ")
	if username in loginDict:
		if loginDict[username]==password:
			print("Username and password are correct, you are in.")
	else:
		choice=input("Username and/or password are not found. Would you like to sign up? Y or N: ")
		if choice=="Y":
			username1=input("Please enter a username: ")
			password1= input("Please enter a password: ")
			hash=makehash(password1)
			login(username1,hash)
		else:
			print("Please try again")
			prompt()
		
prompt()