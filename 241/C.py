N = int(input())
S = [input() for i in range(N)]

def Yes():
    print('Yes')
    exit(0)


for i in range(N):
    for j in range(N):
        
        if j <= N-6: #右方向
            count = 0
            for k in range(6):
                if S[i][j+k] == '.':
                    count += 1
            if count <= 2:
                Yes()
                        
        if i <= N-6: #下方向
            count = 0
            for k in range(6):
                if S[i+k][j] == '.':
                    count += 1
            if count <= 2:
                Yes()            

        if j <= N-6 and i <= N-6: #右下方向
            count = 0
            for k in range(6):
                if S[i+k][j+k] == '.':
                    count += 1
            if count <= 2:
                Yes()

        if j <= N-6 and i >= 5: #右上方向
            count = 0
            for k in range(6):
                if S[i-k][j+k] == '.':
                    count += 1
            if count <= 2:
                Yes()                           

print('No')









