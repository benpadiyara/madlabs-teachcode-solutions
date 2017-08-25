s=input()
a=int(input())
b=int(input())
d=0
print(s[a].upper())
print(s[b].lower())
for c in s:
	d+=ord(c)
print(d)
