import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
from numpy import random
from matplotlib import ticker

# Выборка

#print("---------------Выборка неупорядоченная---------------")
unordered_selection = [0.67486, 0.58972, 0.42444, 0.06823, 0.11778, 0.18586, 0.18357, 2.49922, 0.18878, 0.45634,
                       0.80937, 0.07319, 1.49651, 0.53857, 1.30771, 0.54178, 1.21150, 0.38258, 0.01169, 0.37383,
                       0.71046, 1.20890, 0.04709, 0.50424, 1.50991, 0.54345, 0.24455, 0.66169, 1.83122, 0.58858,
                       0.57363, 0.55926, 0.81493, 0.98391, 1.13958, 0.13580, 3.33892, 0.53162, 0.35072, 0.19910,
                       1.78341, 0.55258, 0.14564, 0.62451, 0.38862, 2.66748, 0.33053, 0.83705, 0.33227, 0.66308,
                       0.12847, 0.47610, 0.26448, 0.71886, 0.99054, 0.52672, 0.75556, 0.39791, 0.03681, 0.36343,
                       0.11577, 0.20792, 0.26228, 1.07269, 0.20332, 0.08316, 0.47462, 0.11318, 0.56992, 1.07910,
                       0.31558, 0.82021, 0.50002, 0.33578, 0.23458, 0.41349, 0.06195, 0.75617, 0.55174, 0.20672,
                       0.38189, 0.11691, 0.10369, 0.25239, 0.23137, 0.58782, 0.21581, 0.17625, 0.29990, 1.16720,
                       0.12525, 0.17521, 1.13607, 0.82693, 0.09101, 0.41179, 0.59224, 0.99515, 0.26060, 0.99077,
                       1.55399, 0.95164, 0.16004, 0.39549, 0.62864, 0.26967, 0.75291, 0.19498, 0.19778, 0.33829,
                       0.85239, 0.66812, 1.11608, 1.65791, 0.62790, 0.61316, 0.25369, 0.19571, 1.17809, 0.17082,
                       0.39416, 0.25963, 1.15813, 0.09776, 0.40405, 1.11863, 0.21029, 0.43711, 0.53725, 0.15284,
                       0.93225, 0.23490, 0.23579, 0.65594, 0.28493, 0.02950, 0.41549, 1.78093, 0.12208, 0.11472,
                       0.71844, 1.48150, 0.61143, 1.91472, 0.54069, 0.01410, 0.90508, 2.06678, 2.08465, 0.55302,
                       0.48608, 0.17963, 0.07180, 0.98053, 0.83383, 0.51073, 0.80725, 1.09497, 0.43639, 0.40107,
                       0.54261, 0.15485, 0.01212, 0.11518, 1.05892, 0.66462, 2.81125, 0.81818, 0.79514, 0.71702,
                       0.97400, 0.95765, 2.00727, 1.23089, 1.80813, 0.16180, 0.21684, 0.42768, 1.93100, 0.13934,
                       0.11167, 0.09714, 2.81874, 0.62420, 1.22136, 0.45841, 1.75925, 0.51679, 0.26634, 0.43943,
                       2.69062, 1.39625, 0.58909, 0.62913, 0.23529, 0.39029, 0.45254, 0.34009, 0.09857, 0.27038]
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
    if(i == 0):
        print(i + 1, ".", "Интервал", "[", round(a[i], 5), "      ,", round(a[i+1], 5), "]", f"x_{i+1}* =", x[i], f"n_{i+1} =", n[i], f"w_{i+1} =", w[i])
    else:
        print(i + 1, ".", "Интервал", "[", round(a[i], 5), ",", round(a[i+1], 5), "]", f"x_{i+1}* =", x[i], f"n_{i+1} =", n[i], f"w_{i+1} =", w[i])
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
p[m] = round(1 - bigF[m - 1], 5)
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
    if(i == 0):
        print("k = ", k[i], ";", "0             ", ";", "f(0, _lambda) = ", f[i], ";","F(0, _lambda) =", "0", ";", "p_0* = ","-")
    else:
        print("k = ", k[i], ";", f"a_{i} = ", round(a[i], 5), ";", f"f(a_{i}, _lambda) = ", f[i], ";", f"F(a_{i}, _lambda) = ", bigF[i], ";", f"p_{i}* = ", p[i])
print("Сумма p:", sum_p)

print("---------------Таблица 2.3---------------")

shtuka = [0 for i in range(m)]
for i in range(m):
    shtuka[i] = (200 * ((w[i] - p[i + 1]) ** 2)) / p[i + 1]
sum_shtuka = 0
for i in range(m):
    sum_shtuka += shtuka[i]

mod = [0 for i in range(m)]
delta = 0
for i in range(m):
    mod[i] = round(math.fabs(w[i] - p[i + 1]), 5)
    if mod[i] > delta:
        delta = mod[i]
    print("k = ", k[i] + 1, "Интервал", "[", round(a[i], 5), ",", round(a[i+1], 5), "]", f"w_{i+1} =", w[i], f"p_{i+1}* =", p[i + 1], f"|w_{i+1}-p_{i+1}|", mod[i], "shtuka =", round(shtuka[i], 5))
print("Сумма w_k = ", sum_w, "Сумма p_k = ", sum_p, "Сумма shuka_k (КРИТЕРИЙ ХИ^2_В) = ", round(sum_shtuka, 5))

# Число степеней свободы
l1 = m - 2
print(f"Число степеней свободы l = {l1}")

# Проверка гипотезы
criteria = round(sum_shtuka, 5)

if(criteria <= 12.6):
    print(f"{criteria} <= 12,6 Гипотеза НЕ ПРОТИВОРЕЧИТ экспериментальным данным")
else:
    print(f"{criteria} > 12,6 Гипотеза ПРОТИВОРЕЧИТ экспериментальным данным")

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
ox.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
plt.title("График")
plt.grid()
plt.show()
