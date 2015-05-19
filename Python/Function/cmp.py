print cmp(1,2),cmp(2,1),cmp(1,1)
def fake_cmp(x,y):
    if x - y < 0:
        return -1
    elif x > y:
        return 1
    return 0
print fake_cmp(1,2),fake_cmp(2,1),fake_cmp(1,1)
