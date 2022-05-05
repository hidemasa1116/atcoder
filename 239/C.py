x1, y1, x2, y2 = map(int, input().split(' '))

box = []

x1_1 = x1 + 1
y1_1 = y1 + 2
box.append([x1_1, y1_1])

x1_2 = x1 + 2
y1_2 = y1 + 1
box.append([x1_2, y1_2])

x1_3 = x1 + 2
y1_3 = y1 - 1
box.append([x1_3, y1_3])

x1_4 = x1 + 1
y1_4 = y1 - 2
box.append([x1_4, y1_4])

x1_5 = x1 - 1
y1_5 = y1 - 2
box.append([x1_5, y1_5])

x1_6 = x1 - 2
y1_6 = y1 - 1
box.append([x1_6, y1_6])

x1_7 = x1 - 2
y1_7 = y1 + 1
box.append([x1_7, y1_7])

x1_8 = x1 - 1
y1_8 = y1 + 2
box.append([x1_8, y1_8])




x2_1 = x2 + 1
y2_1 = y2 + 2
box.append([x2_1, y2_1])

x2_2 = x2 + 2
y2_2 = y2 + 1
box.append([x2_2, y2_2])

x2_3 = x2 + 2
y2_3 = y2 - 1
box.append([x2_3, y2_3])

x2_4 = x2 + 1
y2_4 = y2 - 2
box.append([x2_4, y2_4])

x2_5 = x2 - 1
y2_5 = y2 - 2
box.append([x2_5, y2_5])

x2_6 = x2 - 2
y2_6 = y2 - 1
box.append([x2_6, y2_6])

x2_7 = x2 - 2
y2_7 = y2 + 1
box.append([x2_7, y2_7])

x2_8 = x2 - 1
y2_8 = y2 + 2
box.append([x2_8, y2_8])

def has_duplicates2(seq):
    seen = []
    unique_list = [x for x in seq if x not in seen and not seen.append(x)]
    return len(seq) != len(unique_list)


if has_duplicates2(box) == True:
    print('Yes')
else:
    print('No')



# print(box)
# print(set(box))
# # if len(box) != len(set(box)):
# #     print('Yes')
# # else:
# #     print('no')








