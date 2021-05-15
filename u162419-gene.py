import random
from decimal import *
bt=10000000
getcontext().prec=20100000

def rand(bits):
	c=str(random.randint(1,10))
	for i in range(1,bits):
		c+=str(random.randint(0,10))
	return c

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

def gen(fn):
	a=rand(bt)
	b=rand(bt)
	with open(fn+'.in','w') as f:
		print(a,b,sep='\n',file=f)
	with open(fn+'.out',"w") as f:
		print(rn(a,b),file=f)
	return

for i in range(0,10):
	gen('data'+str(i))
