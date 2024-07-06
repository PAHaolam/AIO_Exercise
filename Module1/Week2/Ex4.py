def Levenshtein_dist(source, target):
    m = len(source)
    n = len(target)
    res = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        res[i][0] = i
    for j in range(n+1):
        res[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            res[i][j] = min(1+res[i-1][j], res[i][j-1]+1, res[i-1][j-1]+int(source[i-1]!=target[j-1]))
    print(res[m][n])