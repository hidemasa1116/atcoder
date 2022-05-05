K = int(input())
n = list(map(int, input().split()))
A = str(n[0])
B = str(n[1])

def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out


new_A = Base_n_to_10(A, K)
new_B = Base_n_to_10(B, K)
print(new_A*new_B)

