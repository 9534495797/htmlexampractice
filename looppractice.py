# i=0
# while i<=20:
#     i+=2
#     print(i)

# i=0
# while i<50:
#     i+=5
#     print(i)

def febonacci_series(n):
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return(febonacci_series(n-2)+febonacci_series(n-1))
n=int(input("your num: "))
for n in range(0,n):
 print(febonacci_series(n))
