
lis = [5,12,5,6,2,6,7,8]
lis2 = [6,4,3,8,1,2,4,6]
sub_list = []


for (i,j) in zip(lis,lis2):
    if i>j:
        k = i-j
        sub_list.append(k)
    else:
        k = j-i
        sub_list.append(k)
print(sub_list)

total = sum(sub_list)
print(total)
