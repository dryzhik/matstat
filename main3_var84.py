import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
from numpy import random
from matplotlib import ticker

# Выборка

#print("---------------Выборка неупорядоченная---------------")
unordered_selection = [3.23201, 0.67900, 0.19967, 1.09873, 1.02077, 1.04180, 0.25377, 0.14239, 0.10828, 0.80772,
                       1.20218, 1.01154, 0.05482, 0.72387, 0.05598, 1.46263, 0.57104, 1.28147, 0.23291, 0.47717,
                       0.20569, 0.08186, 2.32645, 0.03115, 1.31646, 0.70285, 0.22106, 0.13163, 0.22057, 0.73863,
                       1.89297, 0.62482, 0.65762, 1.40614, 0.44728, 0.01761, 0.22406, 2.57914, 0.80272, 0.68380,
                       0.42102, 1.42840, 1.58676, 0.05499, 0.84371, 0.69110, 0.49398, 0.57027, 0.26407, 0.02431,
                       0.08085, 0.43535, 0.88986, 0.11818, 0.86491, 0.19314, 0.70400, 0.60198, 2.60474, 0.11875,
                       0.09248, 0.23322, 0.04362, 0.34554, 0.05102, 0.00880, 0.35227, 0.06641, 0.20622, 0.13897,
                       0.38703, 0.30414, 0.01549, 0.58453, 0.54077, 0.55279, 0.12175, 0.03206, 0.95111, 0.84356,
                       0.60328, 0.09629, 1.10557, 0.75244, 0.20824, 0.10094, 0.04736, 0.38621, 0.74711, 0.36249,
                       1.99138, 0.02978, 0.03823, 0.01660, 0.34371, 0.57362, 0.27359, 1.11239, 0.17732, 0.63310,
                       0.36225, 1.85315, 1.48644, 0.01938, 1.20342, 0.44673, 2.40807, 0.18693, 0.61593, 0.29642,
                       1.40869, 0.22571, 1.11339, 0.51921, 0.08535, 2.16273, 0.70707, 0.63686, 2.18274, 0.12410,
                       2.89668, 0.09122, 1.06073, 0.70243, 0.09821, 0.51451, 0.21989, 0.20114, 0.59647, 2.61627,
                       0.26727, 0.52788, 0.29553, 2.81528, 0.32689, 0.14882, 3.04225, 0.18552, 1.04285, 0.46521,
                       3.08974, 0.77434, 0.22770, 0.28996, 1.18848, 0.31939, 0.08597, 0.50945, 1.35821, 0.36861,
                       0.08882, 0.00690, 0.68387, 0.21473, 0.52555, 0.38294, 0.29968, 1.27273, 0.25679, 0.22621,
                       0.81307, 4.75185, 0.24636, 0.26237, 1.00961, 0.07560, 0.34901, 1.02019, 0.01715, 0.21853,
                       1.28088, 1.15997, 0.16998, 0.30582, 0.01089, 1.36421, 0.23308, 1.14121, 1.18444, 0.73368,
                       0.55969, 0.37517, 0.41284, 0.09101, 0.22808, 0.12312, 0.19595, 0.01990, 0.15338, 0.30599,
                       0.59008, 0.01613, 1.09722, 0.12517, 0.13476, 0.38499, 0.12417, 0.14833, 0.00937, 0.67818]
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

