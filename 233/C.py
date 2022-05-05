N, X = map(int, input().split())
nums = [1]

for i in range(N):
    L, *A = map(int, input().split())
    # for x in nums:
    #     for y in A:
    #         if x * y <= X:
                
    nums = [x * y for x in nums for y in A if x * y <= X]
    

# print(nums)
print(nums.count(X))

# print(L, *A)
