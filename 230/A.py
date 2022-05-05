N = int(input())

if N >= 42:
    num = N+1
else:
    num = N

if len(str(num)) == 1:
    ans = 'AGC' + '00' + str(num)
elif len(str(num)) == 2:
    ans = 'AGC' + '0' + str(num)

print(ans)




