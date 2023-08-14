m=int(input("Enter row:"))
n=int(input("Enter coulmn:"))
print("x",end="  ")
for y in range(m):

                print(y+1,end="  ")
                
print()

for  i in range(n+1):
    if i>0:
        print(i,end="  ")
    for x in range(m+1):
        
        if i>0 and x>0:
           
            print(x*i,end="  ")
    print()

