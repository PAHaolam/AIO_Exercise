#Câu hỏi 1
def max_kernel(num_list, k):
    result = []

    for i in range(len(num_list)-k+1):
        result.append(max(num_list[i:i+k]))

    return result


#Câu hỏi 2
def character_count(s):
    character_statistic = {}
    for i in s:
        if i in character_statistic:
            character_statistic[i] += 1
        else:
            character_statistic[i] = 1
    return (character_statistic)


#Câu hỏi 3
def word_count(file_path):
    counter = {}

    with open(file_path, 'r') as f:
        content = f.read()
    words = content.split()
    for w in words:
        if w in counter:
            counter[w] += 1
        else:
            counter[w] = 1

    return counter


#Câu hỏi 4
def levenshtein_distance(token1, token2):
    m = len(token1)
    n = len(token2)
    res = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        res[i][0] = i
    for j in range(n+1):
        res[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            res[i][j] = min(1+res[i-1][j], res[i][j-1]+1, res[i-1][j-1]+int(token1[i-1]!=token2[j-1]))
    distance = res[m][n]

    return distance


#Câu hỏi 5
def check_the_number(N):
    list_of_numbers = []
    result = ""
    for i in range(1, 5):
        list_of_numbers.append(i)
    if N in list_of_numbers:
        results = "True"
    if N not in list_of_numbers:
        results = "False"
    return results


#Câu hỏi 6
def clip(data, max, min):
    result = []
    for i in data:
        if i<min:
            result.append(min)
        elif i>max:
            result.append(max)
        else:
            result.append(i)
    return result


#Câu hỏi 7
def concat(x, y):
    x = x.copy()
    x.extend(y)
    return x


#Câu hỏi 8
def min_element(l):
    m = l[0]
    for i in l:
        if i<m:
            m = i
    return m


#Câu hỏi 9
def max_element(l):
    m = l[0]
    for i in l:
        if i>m:
            m = i
    return m


#Câu hỏi 10
def exist(integers, number = 1):
    return any([x==number for x in integers])


#Câu hỏi 11
def mean_list(list_nums = [0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var / len(list_nums)


#Câu hỏi 12
def divisible_by_3(data):
    var = []
    for i in data:
        if i%3==0:
            var.append(i)
    return var


#Câu hỏi 13
def fact(y):
    var = 1
    while(y>1):
        var *= y
        y -= 1
    return var


#Câu hỏi 14
def reverse_string(x):
    s = ""
    for c in x:
        s = c + s
    return s


#Câu hỏi 15
def check(x):
    if x>0:
        return "T"
    else:
        return "N"
    
def eye(data):
    res = [check(x) for x in data]
    return res


#Câu hỏi 16
def non_exist(x, data):
    for i in data:
        if x==i:
            return 0
    return 1

def remove_duplicate(data):
    res = []
    for i in data:
        if non_exist(i, res):
            res.append(i)
    return res

print(remove_duplicate([9, 9, 8, 1, 1]))