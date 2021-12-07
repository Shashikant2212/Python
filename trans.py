'''x = int(input("Hello shashikant"))
y = int(input("hello pk"))
print (x,y)
print (".%2f X =.%2f Y" %(x,y))
'''
dict = {"shashikant": "kumar","kumar": "rajbhar","hi":"नमस्ते"}
print (dict)
print (dict["shashikant"])
L = input("Entre Your World ")
if  (L not in dict):
	print (dict[L])
else:
	print ("Opps! You Are Not registered In My Database")
