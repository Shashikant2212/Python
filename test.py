shashikant=('''	|========================================================|
	|                    SHASHIKANT                          |
	|========================================================|
''')
#print(shashikant)
'''
I=float(input("Entre Your Marks"))
Num=100
if Num<I:
	print ("Please Entre Number Less Than,",I)
elif I==Num:
	print ("It Can Be Not Possible")
elif I<Num and I>=80:
	print ("Grade A Hounor")
elif I<=79 and I>=60:
	print ("Grade A")
elif I<=59 and I>=50:
	print ("Grade B")
elif I<=49 and I>=40:
	print ("Grade C")
else:
	print ("Opps! You Are Fail")
'''
'''
g=10
m=20
Yes="Y"
No="N"
if I==Yes:
	print (2+2)
elif I==No:
	print (10-7)
else:
	print ("Opps! entre Y or N")

'''


'''
print("			12th marks calculator")
p=int(input("Entre Your Physics Marks     "))
c=int(input("Entre Your Chemistry Marks   "))
m=int(input("Entre Your Math Marks        "))
h=int(input("Entre Your Himdi Marks       "))
e=int(input("Entre Your English           "))
total=(p+c+m+h+e)
print (" 	Marks Obtained / Maximum Marks,total" ,total,"/" "500")
print ("		In persentage",total/5,"%")

'''

'''
passs=input("Set You Password")
msg=input("Entre is your password?")
while passs!=msg:
	print ("wrong")
	msg=input("what is your password?")
print ("correct")
'''



'''
#var="python"
#for s in var:
#	print (list(s))
lar=["python","jQuery","C++"]
for s in lar:
	print ((s))

#list=[1,2,3,4,5,6,78,9,10,11,12,13,14,15,161,17,18,19,20]
list=[1,3,5,7]
for s in list:
	if s%2==0:
		print ("evn nt avl")
else:
 print ("does not content even")
'''






'''


n=int(input("Entre the number of row"))
for i in range(0,n):
	for j in range(0,i+1):
		print ("*",end='')
	print ()
'''

'''

for i in range(0,5):
	for j in range(0,i**3):
		print ("*",end='')
	print ()

'''
'''
for i in range(-10,5):
 print (i)
usr=int(input("Entre your number for checking Even or Odd "))
if usr%2==0:
 print ("Even")
else:
 print ("Odd")
for i in range(1,usr):
 print (i,"!",end='')
print (type(usr))

'''
#emp={"name":"Shashikant","age":"18+ Year","salary":25000}
'''
print ("name: %s" %emp["name"])
print (emp)
print (emp["name"])
print ("name: %s" %emp["age"])
'''
'''
row=int(input("enter your row\n"))
if row+1>4:
	print("hi")'''


'''

inp=input()
a="a"
while inp!=a:
	print ("Wrong")
	inp=input()
print("                 12th marks calculator")
p=int(input("Entre Your Physics Marks     "))
c=int(input("Entre Your Chemistry Marks   "))
m=int(input("Entre Your Math Marks        "))
h=int(input("Entre Your Himdi Marks       "))
e=int(input("Entre Your English           "))
total=(p+c+m+h+e)

passs=input("Set Your Passworld")
inp=input()
while inp!=passs:
        print ("Wrong")
        inp=input()

print ("        Marks Obtained / Maximum Marks,total" ,total,"/" "500")
print ("                In persentage",total/5,"%")
'''

'''		break  Example		'''
'''
for latter in "Python":
	print (latter)
	if latter=="h":
		break

i=int(input("Entre Any Number"))
list=[11,22,33,44,55,66,77,88,99,00]
for l in list:
	print (l)
	if i==33:
		print ("Number found in list")
		break
	else:
		print ("Number not found in list")
		break

''' '''		iter and next function 		'''
'''it=iter(list)
print (it)
if i==(next(it)):
	print ("Ooo!")
for t in it:
	print (t)
def s(n):
	print ("shashikant")
s("g")

import math
p=(math.fabs(math.pi))
n=int(input("ip"))
print (p/n)
'''

'''
i="python"
j="Shashikant python SQL"
print (i.capitalize())
print (i.upper())
print (j.lower())
print (i.isupper())
print (i.islower())
print (i.lstrip())
print (len(i),len(j))
print (min(i))
print (min(j))
print (max(j))
print (i.replace("python","PYTHON"))
print (j.title())
'''
'''

import base64
usr=input("Entre The Text For Encrypt")
print (usr)
print (base64.b64encode(usr.encode('utf-8',errors='strict')))
j="b'aGlpaWk='"
print (base64.b64decode(j.decode('utf-8',errors='strict')))
'''



'''
	#one line calculator

while True: print (eval(input(">>>")))
'''




'''
Name=input("Entre Your Full Name ")
Father=input("Entre Your Father Name ")
age=float(input("Entre Your Ange In Yea r"))
dist=input("Entre Your district ")
sal=int(input("Entre Your Salary "))
file=open("s.txt","w")
file.write(Name,Father,age,dist,sal)
'''



'''
s="Hi"
g="hi"
print (s==g.title())
'''
'''
t=open('demo.txt','r+')
s=t.read()
for i in s:
	print (s+1)

'''


class Shashikant:
	name="Shashikant__"
	age="18+"
S=Shashikant()
S.name
S.lastname="Kumar"

def pk(Shashikant):
	print (Shashikant.name,Shashikant.lastname)
pk(S)




