import sys

def fnth(n,mod=None):
	if mod is not None:
		if n==1:
			return [0,1]
		else:
			if n%2==1:
				ans=fnth(n-1,mod)
				return [ans[1],(ans[0]+ans[1])%mod]
			else:
				ans=fnth(n//2,mod)
				return [(ans[0]**2+ans[1]**2)%mod,(2*ans[0]*ans[1]+ans[1]**2)%mod]
	else:
		if n==1:
			return [0,1]
		else:
			if n%2==1:
				ans=fnth(n-1)
				return [ans[1],ans[0]+ans[1]]
			else:
				ans=fnth(n//2)
				return [ans[0]**2+ans[1]**2,2*ans[0]*ans[1]+ans[1]**2]

def fi(n,mod=None):
	return fnth(n,mod)[1]

def pcy(p):
	if p%5==1 or p%5==4:
		return p-1
	elif p%5==2 or p%5==3:
		return 2*p+2
	else:
		return 20

def pacy(p,a):
	return pcy(p)*(p**(a-1))

def gcd(a,b=0):
	while b!=0:
		a,b=b,a%b
	return a

def lcm(a,b):
	return a//gcd(a,b)*b

def rlcm(x):
	ans=1
	for i in x:
		ans=lcm(ans,i)
	return ans

def cy(p):
	i=2
	ans=[]
	while i*i<=p:
		cnt=0
		while p%i==0:
			cnt+=1
			p//=i
		if cnt!=0:
			ans.append(pacy(i,cnt))
		i+=1
	if p!=1:
		ans.append(pacy(p,1))
	return rlcm(ans)

n,p=int(input()),int(input())
if p==1 or n==0:
	print(0)
else:
	print(fi(n%cy(p),p))
#	print(cy(p))
