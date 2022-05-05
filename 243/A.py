V, A, B, C = map(int, input().split())

x = V % (A+B+C)

if x < A:
    print('F')
elif x < A+B:
    print('M')
else:
    print('T')





