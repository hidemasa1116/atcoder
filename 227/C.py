N = int(input())

def divisor_list_s(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)  
            if i**2 == num:
                continue
            divisors.append(int(num/i))
#     return divisors # 昇順にしなくてよいならソートは不要
    return sorted(divisors) # 昇順にしたいときはソートする

ans = 0
for i in range(1, N+1):
    x = divisor_list_s(i)
    if len(x) % 2 == 0:
        ans += len(x) / 2
    else:
        ans += len(x) // 2 + 1

print(int(ans))






# X = divisor_list_s(N)
# print(X)

# ans = 0
# for x in X:
#     s = divisor_list_s(N/x)
#     if len(s) % 2 == 0:
#         ans += len(s) / 2
#     else:
#         ans += len(s) // 2 + 1

# print(ans)
