N = int(input())
list_ST = []

for i in range(N):
    list_i = list(input().split())
    list_ST.append(list_i)

def has_duplicates2(seq):
    seen = []
    unique_list = [x for x in seq if x not in seen and not seen.append(x)]
    return len(seq) != len(unique_list)

if has_duplicates2(list_ST) == True:
    print('Yes')
else:
    print('No')