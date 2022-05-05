N = int(input())
H = list(map(int, input().split()))


pos = 0
while pos < N-1:
    if H[pos+1] > H[pos]:
        pos += 1
        if pos == N-1:
            print(H[pos])
            break
    else:
        print(H[pos])
        break










