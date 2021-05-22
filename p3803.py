from decimal import *
getcontext().prec=2000010

def rn(a,b):
	e=1
	if a[0]=='-':
		e*=-1
		a=a[1:]
	if b[0]=='-':
		e*=-1
		b=b[1:]
	a,b=Decimal('0.'+a),Decimal('0.'+b)
	c=str(a*b)
	c=c[2:]
	while c[0]=='0':
		c=c[1:]
	if e==-1:
		c='-'+c
	return c

cache=input().split()
n,m=int(cache[0]),int(cache[1])
cache=input().split()
a=''
for i in cache:
	a+=i
cache=input().split()
b=''
for i in cache:
	b+=i

c=rn(a,b)
for i in range(0,len(c)):
	print(c[i],end=' ')
