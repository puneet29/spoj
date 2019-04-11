def decode(S, i, j, memo):
    if(j == i-1):
        return 1
    if(i in memo):
        return(memo[i])
    else:
        ans = decode(S, i+1, j, memo)
        if(j-i >= 1):
            if(int(S[i:i+2]) <= 26):
                ans += decode(S, i+2, j, memo)
        memo[i] = ans
        return (ans)


while(True):
    n = input()
    if(n == "0"):
        break
    print(decode(n, 0, len(n)-1, {}))
