n=0
while n<100:
    n+=1
    a=n/7#7倍数
    b=n%7#个位7
    c=n//10#十位7
    if a in range(1,16) or b==7 or c==7:
        continue
    print(n)

n=0
while n<100:
    n+=1
    a=n%7#7倍数
    b=n%10#个位7
    c=n//10#十位7
    if a ==0 or b==7 or c==7:
        continue
    print(n)
