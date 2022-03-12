import os
#s=open("s.txt", "w+")
#s.write("shashikant\nPhP\nPython\nSQL\nDjango\nFlutter\nRuby\nJSon\nKotline")
#print (s.name)




def file():
	s.close()
	#s.write("Hi")		#You can't write because file is closed
	#print (s. closed)
	#print (s.mode)
	i=open("s.txt","r+")
	read=i.read()
	#print (read)
	#print (type(read))
	#p=s.tell()
	#print (p)

#file()





'''		****Operation On Other File****			'''




def Xparametre():
	file=open("kk.txt","x") #if file exist same name then work This
	print ("file created")
	if file:
		print ('file created')
	else:
		print ("File does not created")
#Xparametre()




def Aparametre():
	file=open("s.txt","a")
	file.write("\nShell")
	i=open("s.txt","r+")
	reaad=i.read()
	print (reaad)

#Aparametre()




def research():
	Pi="python"
	PI="python"
	print (Pi is PI)
	x=[1,2,3,4,5,6]
	z=[1,2,3,4,5,6]
	y=x=z
	print (x is y)
	print (z is x)
	i=input()
	j=input()
	if i==j:
		print ("You Are Same")
	else:
		print ("You Are Differ")
#research()




def cd():

	os.chdir("storage/shared/git")
	file=open("info.txt","r")
	_file=file.read()
	print (_file,sep="__")
	for file in _file:
		print (file,end="_")

#cd()










from scapy.all import *
from scapy.layers.dot11 import Dot11

def packet_handler(pkt):        
    if pkt.haslayer(Dot11) and pkt.type == 2:        
        print(pkt.show())
scapy.sniff(iface="mon0", prn=packet_handler)
















