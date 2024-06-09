def exercise1():
    num_list = list(map(int, input("num_list = ").split()))
    k = int(input("k = "))
    res = []
    for i in range(len(num_list)-k+1):
        res.append(max(num_list[i:i+k]))
    print(res)