import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
from numpy import random
from matplotlib import ticker

# Выборка

#print("---------------Выборка неупорядоченная---------------")
unordered_selection = [0.41845, 0.71643, 0.65055, 0.38581, 0.47323, 0.14957, 2.18406, 0.05286, 0.32256, 0.63544,
                       1.01714, 0.20688, 0.45530, 0.40937, 1.62548, 1.70686, 0.92240, 0.49447, 1.05269, 0.76828,
                       0.38401, 0.10967, 3.52477, 0.74893, 0.48923, 0.07528, 0.27811, 0.12089, 0.16186, 1.02256,
                       1.09086, 0.64528, 0.31991, 0.77642, 0.61488, 0.00499, 0.19858, 1.47173, 0.23458, 0.45376,
                       1.27573, 0.57924, 0.68958, 0.31635, 0.87901, 0.33194, 0.24206, 0.29928, 0.03071, 0.70932,
                       1.66484, 1.18204, 1.14566, 0.67026, 1.63866, 0.79882, 1.05804, 0.20520, 0.86944, 1.44848,
                       2.34793, 0.39431, 0.29858, 0.45197, 1.60549, 0.36667, 0.04259, 0.77542, 0.31383, 0.20832,
                       0.32197, 0.37968, 0.55976, 0.34903, 0.91271, 0.30606, 0.49038, 0.22388, 0.24288, 0.07333,
                       0.17971, 2.02101, 0.09770, 0.95316, 1.80033, 0.45786, 0.04457, 0.08133, 0.35624, 0.86457,
                       0.43624, 0.05993, 0.14605, 0.57897, 0.15769, 0.08141, 0.55088, 3.26472, 0.66626, 0.41324,
                       0.72477, 0.01635, 1.04068, 0.55387, 0.58295, 3.14358, 2.31217, 0.23249, 1.16428, 0.61118,
                       0.47879, 0.47721, 1.79980, 0.09895, 0.43836, 0.14934, 0.52932, 0.08475, 0.16084, 0.90206,
                       0.65352, 1.83597, 1.04359, 0.25747, 1.36332, 0.34323, 0.22477, 0.75758, 0.07963, 0.27110,
                       1.30298, 1.73354, 0.28871, 0.54153, 0.26354, 0.38195, 0.55144, 0.48394, 0.40359, 0.16973,
                       0.01731, 0.44381, 0.35552, 0.40327, 0.21548, 1.79116, 0.36882, 0.14138, 0.83204, 0.60887,
                       0.39017, 0.40633, 0.33532, 0.25829, 0.15697, 0.33991, 0.28902, 0.49825, 2.23780, 0.59969,
                       1.05899, 0.14500, 0.11921, 1.90545, 1.17583, 0.00383, 0.80269, 0.13318, 0.54884, 0.47719,
                       0.63372, 0.03425, 0.83827, 0.55285, 0.79963, 0.09499, 1.56434, 0.28969, 1.27997, 1.27768,
                       0.25833, 0.37345, 0.75364, 0.62652, 1.59509, 0.99132, 0.65317, 0.23618, 0.03544, 0.28107,
                       1.01945, 0.63893, 0.04639, 0.51764, 0.90996, 0.15233, 0.10842, 0.59876, 0.42228, 0.11097]
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
print("Сумма p:",sum_p)

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
print("Сумма w_k", sum_w, "Сумма p_k", sum_p, "Сумма shtuka_k", round(sum_shtuka, 5))

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
