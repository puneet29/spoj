def checkPrime(num):
    if(num <= 1):
        return False
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True


T = int(input())
for _ in range(T):
    l, u = map(int, input().split())
    X = []
    S = []

    for i in range(l, u+1):
        X.append(i)
        S.append(True)

    for i in range(u-l+1):
        if(not checkPrime(X[i])):
            S[i] = False
        if(X[i] == 1):
            continue
        for i in range(i+X[i], u-l+1, X[i]):
            S[i] = False

    for i in range(u-l+1):
        if(S[i]):
            print(X[i])
    print()
