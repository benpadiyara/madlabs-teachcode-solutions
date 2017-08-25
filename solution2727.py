l=[]
a=[]
n=int(input())
for i in range(n):
	in1=input()
	a=in1.split(" ")
	if(a[0]=="append"):
		b=int(a[1])
		l.append(b)
	elif(a[0]=="insert"):
		b=int(a[1])
		d=int(a[2])
		l.insert(b,d)
	elif(a[0]=="pop"):
		l.pop()
	elif(a[0]=="print"):
		print(l)
	elif(a[0]=="remove"):
		b=int(a[1])
		l.remove(b)
	elif(a[0]=="reverse"):
		l.reverse()
	elif(a[0]=="sort"):
		l.sort()
	elif(a[0]=="extend"):
		l.extend(a[1])
	elif(a[0]=="count"):
		b=int(a[1])
		l.count(b)
	elif(a[0]=="index"):
		b=int(a[1])
		l.index(b)

