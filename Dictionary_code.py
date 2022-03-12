	#If You Want Work On any Function You Can Or Uncomment Them

def demo():
	dict={"mobile":9889773513,"dob":"07/08/2003",2:"Shashikant"}
	print (dict["mobile"])
	print (dict[2])
	dict_={
	"ram":"syam",
	"radhe":"syam",
	"shashikant":"kumar",
	"age":"07/08/2003",
	"course":"B.sc",
	"python":"sql",
	"ruby":"php"

	}
	keys=dict_.keys()
	values=dict_.values()
	#print (keys)
	#print (values)
	print (dict_["ram"])
	del dict_["ruby"]

	for key_ in dict_.keys():
		print (key_)
	for values_ in dict_.values():
		print (values_)
	ss=dict_.items()
	#print (ss)




def To_var_in_for_loop():
	#Two Variable In for Loop
	#For Only items()
	#if items is infinite Then Variable be Bacome infinites
	dictt_={
	"A":"Z",
	"B":"Y",
	"C":"X",
	"D":"W",
	"E":"V",
	"F":"U",
	}

	for dict_key,dict_value in dictt_.items():
		print ("dict_ key is",dict_key,"	dict_value is",dict_value)
#To_var_in_for_loop()




def L_in_D():
	#Creating a list that contains dictionary
	customer=[
	{
	"Shashikant":{	"id":0,
			"name":"Shashikant",
			"address":"Varanasi 22 Rd",
	}
	},
	{
		"id":2,
		"name":"Vishal",
		"address":"Varanasi 22 Rd"
	},
	{
		"id":3,
		"name":"john",
		"address":"22 varanasi Rd."
	},
	{
		"id":4,
		"name":"lumberjack",
		"address":"Unknown"
	},
	]
	print (len(customer))
	print (customer[0]["Shashikant"]["address"])

#L_in_D()





def D_in_L():
	#Creating a dictionary that contains lists

	dict___={"yt":["Thapa","Harry","Minati"]}
	for iii in dict___ ["yt"]:
		#print (dict___)
		print ('')
		print (iii)
	print (len(dict___))
	print (dict___.keys())
	print (dict___.values())
	print (dict___.items())
	print (dict___["yt"])
#D_in_L()


def update():
	#dictionary is update able
	#Given below Like "hi"
	dict33={"hi":"hello","pk":"amir","lumber":"jack","hi":"ghghello"}
	print (dict33["hi"])




def D_in_D():
	#Creating a dictionary that contains a dictionary
	database={
	"Shashikant": {
		"first name":"Shashikant",
		"last name":"Rajbhar",
		"Qualifications":"20th\n12th",
		"DoB":"07/08/2003",
		},
	"Lumber": {
		"first name":"Lumber",
		"last name":"jack",
		"Qualification":"No",
		"DoB":"01/01/2000"
		},
	       }
	print (len(database))
	print (database["Shashikant"])
	print (database["Lumber"]["last name"])

#D_in_D()

def input_database():

	username=input("Entre Your Username")
	password=input("Entre Your Password")
	name=input("Entre Your Name")
	database={
	username: {
		"username":username,
		"password":password,
		"name":name,
		     }
		  }

	print (database[username])
	for key,values in database[username].items():
		print ("Your",key+"Is",values)
#input_database()











