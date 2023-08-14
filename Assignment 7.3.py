x=int(input("Enter number:"))
L=[]
H=[];o=0
for i in range(x):
    n=int(input(":"))
    L.append(n)

for i in range(x-1):
    q=i+1
    while q<x:
        r=L[q]
        j=L[i]
        k=j<r
        q=q+1
        H.append(k)
        # print(H[0])
for w in H:
    
    if w==True:
        o=o+1
if len(H)==o:
    print("YES")
else:
    print("NO")