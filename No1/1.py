A = list(map(int, input().split('.')))

X = A[0]
Y = A[1]

if 0 <= Y <= 2:
    print('{}-'.format(X))
if 3 <= Y <= 6:
    print('{}'.format(X))
if 7 <= Y <= 9:
    print('{}+'.format(X))


