N = int(input())
X = [list(map(int, input().split())) for i in range(N)]

task = []
time = 0

time += X[N-1][0]
task = task + X[N-1][2:]


while len(task) > 0:

    a = max(task)
    task.remove(a)
    
    time += X[a-1][0]
    task = task + X[a-1][2:]
            
print(time)










# for i in reversed(range(N)):




# skill = []
# time = 0
# for i in reversed(range(N)):
#     time += X[i][0]
#     if X[1] > 0:
#         a = X[2:]



# def pra(now):
#     time += X[now][0]
#     if X[now][1] > 0:
#         a = X[now][2:]
#         for i in a:
#             now = i
#             pra(now)
#         return time

# time = 0
# print(pra(N-1))









