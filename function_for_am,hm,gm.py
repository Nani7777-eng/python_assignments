def val(*hee):
    kill = list(hee)
    # print(kill)
    sum = 0
    sum_1 = 0
    pro  = 1
    har = []


    for i in range(len(kill)):

        sum+=kill[i]
        pro *= kill[i]
        n = len(kill)
        rec = 1/kill[i]
        har.append(rec)
        rec_n = 1/n
    # print(har)
    # print(n)
    # print(sum)
    # print(rec_n)
    for j in range(len(har)):
        sum_1 += har[j]
    # print(sum_1)



    arthimatic_mean = sum/n
    print("arthimatic mean of given number is :",arthimatic_mean)
    harmonic_mean = n/sum_1
    print("harmonic mean of given number is :", harmonic_mean)
    geometric_mean = pow(pro,rec_n)
    print("geometric mean of given number is :", geometric_mean)



val(12,3,4,7)