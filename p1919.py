from decimal import *
getcontext().prec=10100000
a,b=input(),input()
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
print(c)
