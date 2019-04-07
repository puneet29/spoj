def checkPrime(num):
    if(num <= 1):
        return False
    if(num <= 3):
        return True
    for i in range(5, int(num**(1/2)), 6):
        if(num % i == 0 or num % i+2 == 0):
            return False
    return True


T = int(input())
for _ in range(T):
    l, u = map(int, input().split())
    X = []
    S = []

    for i in range(u+1):
        X.append(i)
        if((i % 2 == 0 or i % 3 == 0) and i > 3):
            S.append(False)
        else:
            S.append(True)

    for i in range(u+1):
        if(S[i]):
            if(not checkPrime(X[i])):
                S[i] = False
            else:
                if(i >= l):
                    print(X[i])
            if(X[i] <= 1):
                continue
            for j in range(i+X[i], u+1, X[i]):
                S[j] = False

    print()
