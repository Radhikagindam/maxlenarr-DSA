arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
maxlen=0
right=0
left=0
sum=0
while right<k:
    sum+=arr[right]
    while sum>k:
        sum-=arr[left]
        left+=1
    maxlen=max(maxlen,right-left+1)
    right+=1
print(maxlen)
