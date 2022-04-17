import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
from numpy import random
from matplotlib import ticker

# Выборка

#print("---------------Выборка неупорядоченная---------------")
unordered_selection = [1.35954, 0.47840, 0.46393, 0.11958, 0.83115, 2.60564, 2.17266, 0.49164, 0.88759, 0.20836,
                       0.06560, 0.12227, 0.33931, 0.63652, 0.33278, 0.11205, 0.42802, 0.63892, 0.25608, 0.45059,
                       0.47551, 0.16617, 1.59926, 0.72013, 0.18703, 0.33757, 1.11850, 0.17897, 0.09460, 0.02146,
                       0.75309, 0.32528, 1.03323, 0.22120, 0.26794, 0.01395, 1.39915, 1.67073, 0.46861, 0.28440,
                       1.02188, 0.11869, 0.27461, 0.89458, 0.88568, 0.57466, 0.49006, 0.85111, 0.12948, 0.02570,
                       0.08499, 2.38526, 2.30742, 0.15946, 0.17925, 0.47613, 0.65670, 1.22904, 1.67191, 0.29331,
                       0.27232, 0.67687, 2.31872, 0.50897, 1.94008, 0.57631, 1.04235, 0.63856, 0.05714, 0.75485,
                       1.43004, 0.70816, 0.77485, 0.94718, 2.40019, 0.36350, 0.37674, 0.22440, 1.81796, 0.33156,
                       0.17483, 0.62176, 0.19449, 0.75822, 1.63080, 1.81375, 0.38714, 0.79241, 0.06949, 0.71861,
                       1.03160, 0.21328, 0.08305, 0.04361, 0.03271, 0.20592, 0.05126, 0.28396, 0.56294, 0.37504,
                       0.47990, 1.53473, 0.50938, 0.13332, 1.28010, 0.59808, 1.05498, 0.13108, 0.01514, 0.19091,
                       0.36970, 0.23657, 0.28056, 1.44503, 0.47737, 0.98862, 0.46547, 0.22714, 0.21543, 0.22231,
                       0.21166, 0.27903, 2.77657, 0.65588, 0.27780, 0.19836, 0.45332, 0.02288, 1.50126, 0.77050,
                       0.25031, 0.75107, 0.23896, 0.33976, 0.16067, 0.38022, 0.54117, 2.30959, 1.74996, 0.18882,
                       0.07002, 0.28317, 0.86041, 0.62519, 1.92066, 0.41751, 0.78840, 0.26679, 0.34160, 0.74275,
                       0.24823, 0.69765, 0.40801, 0.67570, 0.38294, 2.09298, 0.62476, 0.45618, 2.36116, 0.18228,
                       1.07360, 0.61670, 0.47931, 1.31063, 1.28370, 1.76481, 0.63638, 0.03016, 0.29319, 0.56404,
                       0.30829, 0.62778, 1.30437, 0.38842, 0.27366, 0.14893, 4.40124, 1.72959, 0.30151, 0.11047,
                       1.67029, 0.23950, 0.58022, 0.08652, 0.56165, 0.84309, 2.20037, 0.17814, 0.08109, 0.55871,
                       0.49725, 1.24207, 0.36179, 0.08030, 0.38566, 2.32540, 0.07332, 1.68893, 1.27952, 0.05312]
#print(unordered_selection)

#print("---------------Выборка упорядоченная---------------")
ordered_selection = np.sort(unordered_selection)
print(ordered_selection)

# Группированная выборка
# Число интервалов по формуле Стерджеса
m = 1 + int(math.log2(200))

# Шаг
h = ordered_selection[199] / m

# a_i
a = [i for i in range(m+1)]
a[0] = 0
for i in range(1, m+1):
    a[i] = a[i - 1] + h

# n_i
n = [0 for i in range(m)]
j = 1
for i in range(m):
    for k in range(200):
        if a[i] < ordered_selection[k] <= a[i+1]:
            n[i] += 1

# w_i
w = [i for i in range(m)]
for j in range(m):
    w[j] = round(n[j]/200, 5)

sum_w = 0
for j in range(m):
    sum_w += w[j]


# x_i
x = [0 for i in range(m)]
for i in range(m):
    x[i] = round( (a[i] + a[i+1]) / 2, 5)

print("---------------Группированная выборка---------------")
for i in range(m):
    print(i, ".", "Интервал", "[", round(a[i], 5), ",", round(a[i+1], 5), "]", "x_i* =", x[i], "n_i =", n[i], "w_i =", w[i])
print("Сумма n_i", sum(n), "Сумма w_i", round(sum(w), 5))

# Математическое ожидание
mu1 = 0
for i in range(m):
    mu1 += x[i] * w[i]
print("Математическое ожидание", round(mu1, 5))

# Дисперсия
mu2_0 = 0
for i in range(m):
    mu2_0 += ((x[i]) ** 2) * w[i]
print("Дисперсия", round(mu2_0, 5))

# Оценка параметра лямбда
_lambda = round(1 / mu1, 5)
print("Оценка параметра лямбда: ",_lambda)
# Значечения для таблицы 2.2
# f(a_k,_lambda)

f = [0 for i in range(m + 1)]
for i in range(m + 1):
    f[i] = round(_lambda * math.exp(-_lambda * a[i]), 5)

# F(a_k,_lambda)
bigF = [0 for i in range(m + 1)]
for i in range(m + 1):
    bigF[i] = round(1 - math.exp(-_lambda * a[i]), 5)

# p_k*
p = [0 for i in range(m + 1)]
p[m] = round(1 - bigF[m-1], 5)
for i in range(m):
    if i == 0:
        p[i] = 0
    else:
        p[i] = round(bigF[i] - bigF[i - 1], 5)
sum_p = 0
for i in range(m + 1):
    sum_p += p[i]

print("---------------Таблица 2.2---------------")
k = [i for i in range(m + 1)]

for i in range(m + 1):
    print("k = ", k[i], ";", "a_k = ", round(a[i], 5), ";", "f(a_k, _lambda) = ", f[i], ";", "F(a_k, _lambda) = ", bigF[i], ";", "p_k* = ", p[i])
print("Сумма p:", round(sum_p, 5))

print("---------------Таблица 2.3---------------")

shtuka = [0 for i in range(m)]
for i in range(1, m):
    shtuka[i] = (200 * ((w[i] - p[i]) ** 2)) / p[i]
sum_shtuka = 0
for i in range(m):
    sum_shtuka += shtuka[i]

mod = [0 for i in range(m)]
delta = 0
for i in range(m):
    mod[i] = round(math.fabs(w[i] - p[i]), 5)
    if mod[i] > delta:
        delta = mod[i]
    print("k = ", k[i], "Интервал", "[", round(a[i], 5), ",", round(a[i+1], 5), "]", "w_k =", w[i], "p_k* = ", p[i], "|w_k-p_k|", mod[i], "shtuka", round(shtuka[i], 5))
print("Сумма w_k", sum_w, "Сумма p_k", round(sum_p, 5), "Сумма shtuka_k", round(sum_shtuka, 5))

step = h
# Гистограмма относительных частот
fig, ox = plt.subplots()
for i in range(m):
    h1 = round(w[i] / step, 5)
    ox.plot([a[i], a[i]], [0, h1], 'k')
    ox.plot([a[i], a[i + 1]], [h1, h1], 'k')
    ox.plot([a[i + 1], a[i + 1]], [h1, 0], 'k')
for i in range(199):
    ox.plot([ordered_selection[i], ordered_selection[i+1]], [_lambda * math.exp(-_lambda * ordered_selection[i]), _lambda * math.exp(-_lambda * ordered_selection[i+1])], 'b')
ox.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ox.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
plt.title("График")
plt.grid()
plt.show()

