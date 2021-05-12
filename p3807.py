def pe(n,p=None):
	if p is None:
		ans=1
		for i in range(2,n+1):
			ans*=i
		return ans
	else:
		if n>p:
			return 0
		else:
			ans=1
			for i in range(2,n+1):
				ans=ans*i%p
			return ans

def anti(x,p):
	return pow(x,p-2,p)

def c(n,m,p=None):
	if p is None:
		return pe(n)//pe(m)//pe(n-m)
	else:
		if n<p and m<p:
			if n<m:
				return 1
			ans=1
			for i in range(m+1,n+1):
				ans=ans*i%p
			ans*=anti(pe(n-m,p),p)
			return ans%p
		else:
			return c(n//p,m//p,p)*c(n%p,m%p,p)%p

t=int(input())
for i in range(0,t):
	cache=input().split()
	n,m,p=int(cache[0]),int(cache[1]),int(cache[2])
	print(c(n+m,n,p))
