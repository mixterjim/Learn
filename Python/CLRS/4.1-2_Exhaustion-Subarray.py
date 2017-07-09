A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
max = 0
left = 0
right = 0
n = 0
for i in range(0, len(A)):
    sum = A[i]
    for j in range(i, len(A)):
        if i == j:
            sum = A[j]
        else:
            sum += A[j]
        if sum > max:
            max = sum
            left = i
            right = j
print(left, right, max)
