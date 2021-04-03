import numpy as np

cache=input().split()
n,m=int(cache[0]),int(cache[1])
cache=input().split()
a=[]
for i in cache:
    a.append(int(i))
cache=input().split()
b=[]
for i in cache:
    b.append(int(i))
def w(k,n):
    return np.cos(2*np.pi*k/n)+np.sin(2*np.pi*k/n)*1j

def dft(f,n):
    ans=[]
    for i in range(0,n):
        x=w(i,n)
        ts=0+0j
        for j in range(0,len(f)):
            ts+=(x**j)*f[j]
        ans.append(ts)
    return ans

def antidft(f,n):
    ans=[]
    for i in range(0,n):
        x=w(-i,n)
        ts=0+0j
        for j in range(0,len(f)):
            ts+=(x**j)*f[j]
        ans.append(ts/n)
    return ans

# print(antidft(dft(a,m+n),m+n))
# print(antidft(dft(b,m+n),m+n))

a,b=dft(a,n+m+1),dft(b,n+m+1)
ans=[]
for i in range(0,len(a)):
    ans.append(a[i]*b[i])
# print(antidft(ans,n+m+1))

ans=antidft(ans,n+m+1)
for i in ans:
    print(int(abs(i+0.01)),end=' ')
print("\n")