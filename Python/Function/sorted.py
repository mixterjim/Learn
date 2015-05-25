l = [81,48,5,897,65,-5,8,0,48,64,84,28,84,-1]
def desc(x,y):
    if x < y:
        return 1
    if x > y:
        return -1
    else:
        return 0
print sorted(l,desc)
def fake_sorted_insert(list,function):
    list_len = len(list)
    for i in range(1,list_len):
        value = list[i]
        h = i - 1
        while desc(list[h],value) == 1 and h >= 0:
            list[h + 1] = list[h]
            h = h - 1
        list[h + 1] = value
    return list
print fake_sorted_insert(l,desc)
def fake_sorted_sequence(list,function):
    list_len = len(list)
    for i in range(list_len):
        flag = i
        for h in range(i+1,list_len):
            if function(list[i],list[h]) == 1:
                flag = h
        if flag != i:
            temp = list[i]
            list[i] = list[flag]
            list[flag] = temp
    return list
print fake_sorted_sequence(l,desc)
def fake_sorted_head (list,function):
    list_len = len(list)
    i = 0
    for i in range(list_len - 1):
        for h in range(i, list_len-i-1):
            if function(list[h+1],list[h]) == -1:
                temp = list[h]
                list[h] = list[h+1]
                list[h+1] = temp
    return list
print fake_sorted_head(l,desc)
