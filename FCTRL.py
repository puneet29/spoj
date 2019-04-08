T = int(input())
for _ in range(T):
    N = int(input())
    fact = 1
    ans = 0
    for i in range(2, N+1):
        fact *= i
    while(fact > 0):
        rem = fact % 10
        if(rem == 0):
            ans += 1
        else:
            break
        fact = fact // 10
    print(ans)
