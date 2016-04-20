dict_ach = {}  # More RAM and Fast
list_name = []  # Less RAM and Slow
list_score = []  # You can change value in [],but can't in ()
score = set([])  # There is no repeat
passing = set([])
while True:
    n = str(input("Input name(Enter \"e\" to exit it):"))
    if n == "e":
        print("Done")
        break
    else:
        dict_ach[n] = int(input("Score:"))
        list_name.append(n)
        list_score.append(dict_ach[n])
        score.add(dict_ach[n])  # Use remove to del set
list_name.append(list_score)
for s in range(60, 101):
    passing.add(s)
print("--------------------------------------------------------------------")
print("Dict:", dict_ach)
print("List:", list_name)
print("Achievement:")
x = len(list_name) - 2
i = -1
while i < x:
    i = i + 1
    print("    %s:%d" % (list_name[i], list_name[-1][i]))
print("All Passing score is", score & passing)  # sum is |
