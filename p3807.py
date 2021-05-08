cache=input().split()
n,m,p=int(cache[0]),int(cache[1]),int(cache[2])

def exeu(a,b,&x,&y):
	if b==0:
		x,y=1,0
		return
	exeu(b,a%b,y,x)
	y-=a//b*x
	return

def anti(n,mod=p):
	x,y=0,0
	exeu(n,mod,x,y)
	return x%mod

def c(u,d,mod=p):
	if u<p and d<p:
		ans=1
		for i in range(u+1,d+1):
			ans=ans*i%p
		for i in range(2,d-u+1):
			ans=ans*anti(i)%p
		return ans
	