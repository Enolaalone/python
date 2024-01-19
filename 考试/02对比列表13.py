ls1 = [12, 40, 10, 9, 8, -1, 21, -6]
ls2 = [12, 7, 10, 9, 88, -1, 21, -6, 10]
Same = []
Difference_1 = []
Difference_2 = []
for i in ls1:
    if i in ls2:
        Same.append(i)
    else:
        Difference_1.append(i)
for i in ls2:
    if i not in ls1:
        Difference_2.append(i)

print('两个表相同元素', Same)
print('ls1有而ls2无', Difference_1)
print('ls2有而ls1无', Difference_2)
