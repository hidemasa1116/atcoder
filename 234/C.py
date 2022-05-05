K = int(input())

mul = []

while K > 1:
    if K % 2 == 1:
        mul.append('2')
    else:
        mul.append('0')
    K = K // 2

mul.append('2')
mul.reverse()


print(int(''.join(mul)))
    
# mul.reverse()
# ans = [2]

# for i in mul:
#     if i == 'r':
#         ans.append(2)
#     else:
#         ans.append(0)

# print(int(''.join([str(_) for _ in ans])))  



# 220022020000202020002022022000002020002222002200002200000000
# 220022020000202020002022022000002020002222002200002022002200


