x=input()
d={}
for i in range(26):
  d[x[i]]=i
ans=[]
n=int(input())
for i in range(n):
  t=[]
  s=input()
  for i in s:
    t.append(d[i])
  ans.append(tuple(t))
ans.sort()
for i in ans:
  t=[]
  for j in i:
    t.append(x[j])
  print(''.join(t))




# X = input()
# X_dict = {}
# N = int(input())
# S_list = []

# for i in range(N):
#     S_list.append(input())

# for i in range(len(X)):
#     X_dict[X[i]] = i


# for i in range(N):
#     mini = i
#     for j in range(i+1, N):
#         if X_dict[S_list[mini][0]] > X_dict[S_list[j][0]]:
#             mini = j
#         elif X_dict[S_list[mini][0]] == X_dict[S_list[j][0]]:
#             k = 1
#             while True:
#                 if (len(S_list[mini]) == k) or (len(S_list[j]) == k):
#                     if len(S_list[mini]) > len(S_list[j]):
#                         mini = j
#                         break
#                     elif len(S_list[mini]) < len(S_list[j]):
#                         break
#                     elif len(S_list[j]) == len(S_list[mini]):
#                         if X_dict[S_list[mini][k]] > X_dict[S_list[j][k]]:
#                             mini = j
#                             break
#                         elif X_dict[S_list[mini][k]] < X_dict[S_list[j][k]]:
#                             break
                        
#                 else:
#                     if X_dict[S_list[mini][k]] > X_dict[S_list[j][k]]:
#                         mini = j
#                         break
#                     elif X_dict[S_list[mini][k]] < X_dict[S_list[j][k]]:
#                         break
#                     else:
#                         k += 1

#     S_list[i], S_list[mini] = S_list[mini], S_list[i]

# for i in S_list:
#     print(i)


