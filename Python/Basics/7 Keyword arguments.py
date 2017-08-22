def sum(*number):
    sum = 0
    for n in number:
        sum = sum + n
    return sum
print(sum(), sum(1), sum(1, 2))  # You can input any parameters
l = [1, 2, 3]
print(sum(*l))  # sum(l[0], l[1], l[2])


def student(name, age, **other):
    print('Name:', name, 'Age:', age, 'Other:', other)
student('Jim', 18, City='New York', Job='Student')
