'''list=["varanasi","delhi","newYork","noida","etc"]


print (list[2].title())
inp=input('Entre Your City')
sha="Shashikant"


def delhi():
	data={'name':'Shashikant','dob':'07/08/2003'}
	da='Shashikant'
	print ("hello" +da)
	print (list[0]=='varanasi')
	list.insert(0,"hello")
	print (list)
	list.pop(0)
	print (list)
	list.append(da)
	print (list)



#delhi()

if inp not in list:
	list.append(inp)
	print ("Your Request Has Been Submitted")
else:
	#print ("you are already exist in my database")
	delhi()






 #print (list)
#for city in list:
#	print (city.title())
#



if inp==sha.upper() or inp==sha.lower() or inp==sha.title():
	print ("Your Date Of Birth Is 07/08/2003")
'''



input_1=input("Entre Your Name ")
input_2=input("Entre Your Mobile Number ")
input_3=input("Entre Your Passworld ")
data=[input_1,input_2,input_3]
#print (data)
print ("Succusessfully resister")

def log_in():
        login_M=input("Entre Your Mobile Number ")
        login_P=input("Entre Your Mobile Password ")
        if login_M == data[1]:
                if login_P == data[2]:
                        print ("Login Success")
                else:
                        print ("Wrong Password")
        else:
                print ("Mobile Number Is Wrong")


def change():
	old=input("Entre Your Old Password")
	if old != data[2]:
		print ("Please Enter Correct Password")
	else:
		print ("Verified")
		new=input("Entre Your New Password")
		data.pop(2)
		data.insert(2,new)
		print ("Your Password is",data[2])
		#print (data)


def forgot():
	mobile=input("Entre Your Mobile Number")
	if mobile != data[1]:
		print ("Please Enter Correct Mobile Number")
	else:
		print ("Verified")
		New=input("Entre Your New Password")
		del data[2]
		data.insert(2,New)
		print ("Your New Password is",data[2])
		#print (data)


print ('''For Login Press 1\n
For Change Password Press 2\n
For Forgot Password 3''')


Choice=int(input())
if Choice == 1:
	log_in()
if Choice == 2:
	change()
if Choice ==3:
	forgot()








