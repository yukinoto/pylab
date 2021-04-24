import sys

l,r=0,1000000001
while True:
	mid=(l+r)//2
	print(mid)
	sys.stdout.flush()
	x=int(input())
	if x==-1:
		l=mid+1
	elif x==1:
		r=mid
	else:
		sys.exit(0)