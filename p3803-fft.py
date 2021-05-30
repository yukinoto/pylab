import sys
import math

def w(n,k):
	th=math.pi*2/n*k
	return complex(math.cos(th),math.sin(th))

def fft(f):
	n=len(f)
	if n==1:
		return [(1+0j)*f[0]]
	a,b=[],[]
	for i in range(0,n):
		if i%2==0:
			a.append(f[i])
		else:
			b.append(f[i])
	a,b=fft(a),fft(b)
	ans=[]
	for i in range(0,n//2):
		ans.append(a[i]+b[i]*w(n,i))
	for i in range(0,n//2):
		ans.append(a[i]+b[i]*w(n,i+n//2))
	return ans

def atfft(f):
	n=len(f)
	if n==1:
		return [(1+0j)*f[0]]
	a,b=[],[]
	for i in range(0,n):
		if i%2==0:
			a.append(f[i])
		else:
			b.append(f[i])
	a,b=atfft(a),atfft(b)
	ans=[]
	for i in range(0,n//2):
		ans.append(a[i]+b[i]*w(n,-i))
	for i in range(0,n//2):
		ans.append(a[i]+b[i]*w(n,-i-n//2))
	return ans

def ifft(f):
	ans=atfft(f)
	for i in range(0,len(f)):
		ans[i]/=len(f)
	return ans

def times(f,g):
	n=1
	while n<len(f)+len(g)-1:
		n*=2
	for i in range(len(f),n):
		f.append(0)
	for i in range(len(g),n):
		g.append(0)
	cache1,cache2=fft(f),fft(g)
	ans=[]
	for i in range(0,n):
		ans.append(cache1[i]*cache2[i])
	ans=ifft(ans)
	for i in range(0,n):
		ans[i]=int(abs(ans[i]+0.1))
	return ans

def get():
	cache=input().split()
	for i in range(0,len(cache)):
		cache[i]=int(cache[i])
	return cache

input()
ans=times(get(),get())
flag=False
cache=''
for i in ans:
	if (not flag) and i==0:
		pass
	else:
		flag=True
		if cache!='':
			cache+=' '
		cache+=str(i)
print(cache)
