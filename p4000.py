import sys

def fnth(n,mod=None):
	if mod==None:
		if n==1:
			return [0,1]
		else:
			if n%2==1:
				ans=fnth(n-1)
				return [ans[1],ans[0]+ans[1]]
			else:
				ans=fnth(n//2)
				return [ans[0]**2+ans[1]**2,2*ans[0]*ans[1]+ans[1]**2]
	else:
		if n==1:
			return [0,1]
		else:
			if n%2==1:
				ans=fnth(n-1,mod)
				return [ans[1],(ans[0]+ans[1])%mod]
			else:
				ans=fnth(n//2,mod)
				return [(ans[0]**2+ans[1]**2)%mod,(2*ans[0]*ans[1]+ans[1]**2)%mod]

def fi(n,mod=None):
	return fnth(n,mod)[1]

