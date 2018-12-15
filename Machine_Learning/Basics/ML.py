import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# Data
# 2017:139008
# P_X = 139008
# years = np.array([1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016])
# numbers = np.array([124761, 125786, 126743, 127627, 128453, 129227, 129988, 130756, 131448, 132129, 132802, 133450, 134091, 134735, 135404, 136072, 136782, 137462, 138271])
years = np.arange(20)
numbers = 999 + years * 1234
# np.mat(years)  # define to matrix
# np.mat(numbers)  # define to matrix OR np.dot(A, B)
# Data for plotting
fig, ax = plt.subplots(figsize=(15, 6))
ax.scatter(years, numbers)  # Input Data
ax.set(xlabel='Year (S)', ylabel='Numbers (W)', title='People of China')  # Set label
ax.set_xticks(list(years) + [2017])  # Axis_X value
# Represent


def Feature_Scaling(data):
    data = (data - np.mean(data)) / np.std(data, ddof=1)
    # data = (data-np.mean(data))/(max(data)-min(data))
    return data
# Feature Scaling


def Linear(Theta_0, Theta_1, x):
    H_Theta_X = []
    for i in range(len(x)):
        H_Theta_X.append(Theta_0 + Theta_1 * x[i])
    return np.asarray(H_Theta_X)
# Linear Regression Model


def loss(H_Theta_X):
    loss = np.mean((H_Theta_X - numbers).astype(np.int64)**2)
    return loss
# Loss

Theta_0, Theta_1 = 0, 0
H_Theta_X = Linear(Theta_0, Theta_1, years)
i = 0
while loss(H_Theta_X) != 0:
    if i >= 10000:
        break
    Alpha = 0.1  # Learning rate
    temp0 = Theta_0 - Alpha * np.mean(H_Theta_X - numbers)
    temp1 = Theta_1 - Alpha * np.mean((H_Theta_X - numbers).astype(np.int64) * Feature_Scaling(years))
    Theta_0 = temp0
    Theta_1 = temp1
    H_Theta_X = Linear(Theta_0, Theta_1, years)
    i += 1
# Gradient Descent Algonthm

print("loss:", loss(H_Theta_X))
print("Theta_0:", Theta_0, "Theta_1:", Theta_1)
print(i)
# H_X = Theta_0 + Theta_1 * 2017
# print("2017:%.d" % H_X, "%.2f%%" % (100 - abs((H_X - P_X) / P_X) * 100))
ax.plot(years, H_Theta_X)
plt.show()
