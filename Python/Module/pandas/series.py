from pandas import Series

data = Series([8888, 5555555, 11111, 1234321, 1212121], index=[
              'xiaoyun', 'xiaohong', 'xiaoteng', 'xiaoyi', 'xiaoyang'])
name = input("Please input the name:")
while name not in data:
    name = input("%s is not in the Data.\nPlease input the name:" % name)
print(name, 'QQ:', data[name])
print("Who has the nice QQ number?")
i = len(data.values) - 1
while i >= 0:
    if data.values[i] < 100000:
        print(data.index[i])
    i -= 1
