import requests
n=int(input())
for i in range(0,n):
    res=requests.get("https://api.ixiaowai.cn/api/api.php")
    with open(str(i)+".jpg") as f:
        f.write(res.content)
