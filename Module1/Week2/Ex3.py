def word_count(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    words = content.split()
    d = {}
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    print(d)