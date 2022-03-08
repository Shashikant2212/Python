
def breck():
    for i in range(5):
        print('')

Name="Shashikant"

"""

class Test:
    def display(self):
        print (self.name, self.last,self.work)
sha=Test()
sha.name=input("Entre Your First Name")
sha.last=input("Entre Your Last Name")
sha.work=input("Entre Your Work Experience")
a=sha.display()

"""

breck()





"""

class Test2:
    def __init__(self,Fname,Lname,Work,Age):
      self.Fname=Fname
      self.Lname=Lname
      self.Work=Work
      self.Age=Age
    
    
    def Output(self):
        print ("Name=",self.Fname)
        
    def Change(self):
        self.Fname="Vishal"
    
    
data=Test2("Shashikant","kumar","Coding",18)
data.Output()
data.Change()
data.Output()
"""






breck()







dictionarry={
"data":
{
    "Name":"Shashikant",
    "Title":"kumar",
    "Work":"Learning",
},

"Jonh":
    {
        "Name":"Jonh",
        "Title":"Dio",
        "Prifetion":"Devloper",
        
        "Detail":{
            "ss":"Shashikant",
            "kk":"kumar",
        }
    },
    }
print(dictionarry)
print(len(dictionarry["Jonh"]))
print(dictionarry["Jonh"]["Detail"]["ss"])
count=0.999999999999
for di in dictionarry["Jonh"]:
    count+=0.9
    print (count,di)
    
    
    
    
    
breck()
    
    
    
    
    
    
#......Todo Range() Function .........#
for R in range(4):
    print (R)
    list=["list1","list2","list3","list4","list5","list6"]
    print(list[R],end="break")
    print("")
    
def xxx():
    print ("hello Worlds")
    return "You Are lol"
x=xxx()
print(x)
def foo():
    list=[]
    for i in range(len(dictionarry["Jonh"])):
        x=input("Entre Your Data")
        x=list.append(x)
    print(list)
#foo()
print (len(dictionarry["Jonh"]))

breck()
list=["sql",["LAMP","linux","apache","etc",["sublist","inner"]]]
print(list)
print(list[0])
print(list[1][0])
print(list[1][4][0],[1])
breck()
for i in list[1][4]:
    print(i)
    
breck()

list0,list1=list
Phone=[["Redmi",800],["Oppo",10000],["Realme",700],["Moto",7500]
    ]
#Mobile,Prize=Phone
'''
for Mobile,Prize in Phone:
    print (Mobile,Phone)'''
for Mobile,Prize in Phone:
    print (Mobile,"$",Prize)
Mobile=[["oppo A 5s",800],["Realme",900],["poco",1000],["vivo",4000],["Samsung",12000],["Etc","Something"]]
for mobile,prize in Mobile:
    print (mobile,prize,end='')
breck()
a=100