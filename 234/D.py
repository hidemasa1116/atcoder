from heapq import heapify, heappush, heappop

N, K = map(int, input().split())
P = list(map(int, input().split()))

pq = P[:K]
heapify(pq)  # O(K)でリストpqをヒープ化します

print(pq[0])  # pq[0] が 先頭 K 項 で最小です。(ソートしているわけではないので、pq[1]以降は小さい順に並んでいるとは限りません)

for x in P[K:]:
    heappush(pq, x)  # pqにxを追加します
    heappop(pq)  # 長さK+1のリストpqで最小の値を捨てます
    print(pq[0])  # 長さKのリストpqの最小の値を出力します

































# import bisect
# N, K = map(int, input().split())
# P = list(map(int, input().split()))
# T = ['' for _ in range(N+1)]


# # if K == 1:
# #     T = []
# # else:
# #     T = P[:K-1]

# for i in range(K-1):
#     T[P[i]] = str(P[i])

# print(T)


# for i in range(K-1, N):
#     T[P[i]] = str(P[i])
#     ans = '.'.join(T)
#     # print(ans[-K])
#     print(ans)
    




# # T = [i for i in T if i != 0]
# # T.sort()


# # # T = int(''.join(T))

# # for 


# # for i in range(K-1, N):
# #     T.insert(bisect.bisect(T, P[i]), P[i])
# #     # print(T)
# #     print(T[-K])
    


