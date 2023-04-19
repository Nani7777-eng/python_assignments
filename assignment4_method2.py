'''Suppose l1 = [6,10,2,13,45,67,32,1] and l2 = [8,3,9,12,54,322,98,54]
sort the first list in ascending order l1_sorted = [1,2,6,10,13,32,45,67]
and list2 should be l2_updated as = [54,9,8,3,12,98,54, 322]

Rules to update List 2:
1. List2 element order should be according to l1_sorted index.
2. First value in l1_sorted is 1, before sorting index of 1 is 7, so list2_updated first value is 54, which is 7th index before updating
3. Second value in l1_sorted is 2, before sorting index of 2 is 2,  so list2_updated second value is 9 which is second index before updating
4. Third value in l1_sorted is 6, before sorting index of 6 is 0, so list2_updated third value is 8 which is 0th index before updating.
Similarly, update All the values of list2 by corresponding index values of list1 after sorting.
'''



def rekk(g1,g2):
    if len(g1) == len(g2):

        l2.updated = []
        g1.sort()
        for i in g1:
            l2_updated.append(g2[g1.index(i)])
        print(l2_updated)



    else :
        print("len of the both the list were not equal")
rekk([6,10,2,13,45,67,32,1],[8,3,9,12,54,322,98,54])