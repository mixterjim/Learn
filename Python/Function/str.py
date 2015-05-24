l = str(1),str(2)
print l
def fake_str(s):
    return {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}[s]    #int:{'0':0,...,'9':9}[s]
l_new = fake_str(1),fake_str(2)
print l_new
