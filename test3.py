with open("classes.txt", 'r') as f:
    # l = [int(item) for item in f.readline().split(',')]
    s = f.readlines()
    # l = []
    # for i in s:
    #     l.append(int(i))
    # l = [item.strip().split(',') for item in s]
    l = [[int(item) for item in i.strip().split(',')] for i in s]
    print(l)
