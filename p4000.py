import sys

def fnth(n):
	if n==1:
		return [0,1]
	else:
		if n%2==1:
			ans=fnth(n-1)
			return [ans[1],ans[0]+ans[1]]
		else:
			ans=fnth(n//2)
			return [ans[0]**2+ans[1]**2,2*ans[0]*ans[1]+ans[1]**2]

def fi(n):
	return fnth(n)[1]
