N = int(input())
T = input()

x = 0
y = 0
ang = 1

for i in range(N):

    if T[i] == 'S':

        if ang == 1:
            x += 1
        elif ang == 2:
            y -= 1
        elif ang == 3:
            x -= 1
        else:
            y += 1
    
    else:

        if ang <= 3:
            ang += 1
        else:
            ang = 1


print(x, y)












