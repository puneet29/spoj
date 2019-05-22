import sys


def palindrome(A, low, up):
    # base cases
    if(low > up):
        return(sys.maxsize)
    if(low == up):
        return(0)
    if(low == up - 1):
        return 0 if (A[low] == A[up]) else 1

    # Check if first and last char are equal
    if(A[low] == A[up]):
        return(palindrome(A, low + 1, up - 1))
    else:
        return(min(palindrome(A, low, up - 1), palindrome(A, low + 1, up)) + 1)


for _ in range(int(input())):
    S = str(input())
    print(palindrome(S, 0, len(S)-1))
