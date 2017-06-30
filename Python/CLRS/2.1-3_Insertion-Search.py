def INSERTION_SEARCH(list, value):
    i = 0
    while i < len(list) and list[i] != value:
        i += 1
    if i > len(list) - 1:
        return "NIL"
    else:
        return i


def CREATE_LIST(list):
    while True:
        key = input("Input:")
        if key == "":
            break
        list.append(key)
A = []
CREATE_LIST(A)
v = input("Find:")
print(INSERTION_SEARCH(A, v))
