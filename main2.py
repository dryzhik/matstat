import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
from numpy import random
from matplotlib import ticker

np.random.seed(5)

# Ввод варианта
var = input("Input variant: ")
V = int(var)
_lambda = 3 + (-1)**V * 0.01 * V

# Выборка неупорядоченная
print("---------------Выборка неупорядоченная---------------")
unordered_selection = sps.expon.rvs(scale=round(1/_lambda, 5), size=200)
for i in range(len(unordered_selection)):
    if i % 10 == 0:
        print("Числа с", i+1, "по", i+10)
    unordered_selection[i] = round(unordered_selection[i], 5)
    print(unordered_selection[i])

# Выборка упорядоченная
print("---------------Выборка упорядоченная---------------")
ordered_selection = np.sort(unordered_selection)
for i in range(len(unordered_selection)):
    if i % 10 == 0:
        print("Числа с", i+1, "по", i+10)
    ordered_selection[i] = round(ordered_selection[i], 5)
    print(ordered_selection[i])

# Значения интервального ряда(группированной выборки)
# Число интервалов по формуле Стерджеса
m = 1 + int(math.log2(200))

# Шаг
step = ordered_selection[199] / m

# a_i
a = [i for i in range(m+1)]
a[0] = 0
for i in range(1, m+1):
    a[i] = round(a[i - 1] + step, 5)

# n_i
n = [0 for i in range(m)]
for i in range(m):
    for k in range(200):
        if a[i] < ordered_selection[k] <= a[i+1]:
            n[i] += 1

# w_i
w = [i for i in range(m)]
for j in range(m):
    w[j] = round(n[j]/200, 5)

print("---------------Интервальный ряд (группированная выборка)---------------")
for i in range(m):
    print(i, ".", "Интервал", "[", a[i], ",", a[i+1], "]", "n_i =", n[i], "w_i =", w[i])
print("Сумма n_i", sum(n), "Сумма w_i", round(sum(w), 5))

# Значения для ассоциированного статистического ряда
# x_i
x = [0 for i in range(m)]
for i in range(m):
    x[i] = round( (a[i] + a[i+1]) / 2, 5)

print("---------------Ассоциированный статистический ряд---------------")
for i in range(m):
    print(i, ".", "x_i =", x[i], "n_i =", n[i], "w_i =", w[i])
print("Сумма n_i", sum(n), "Сумма w_i", round(sum(w), 5))
print("------------------------------")

# Гистограмма относительных частот
fig, ox = plt.subplots()
for i in range(m):
    h = round(w[i] / step, 5)
    ox.plot([a[i], a[i]], [0, h], 'k')
    ox.plot([a[i], a[i + 1]], [h, h], 'k')
    ox.plot([a[i + 1], a[i + 1]], [h, 0], 'k')
ox.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ox.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
plt.title("Гистограмма относительных частот")
plt.grid()
plt.show()

# Эмпирическая функция распределения
fig, ax = plt.subplots()
for i in range(199):
    ax.plot([ordered_selection[i], ordered_selection[i+1]], [i/200, i/200], 'k')
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
plt.title("Эмпирическая функция распределения")
plt.grid()
plt.show()

# Выборочное среднее
vs = 0
for i in range(m):
    vs += x[i] * w[i]
a_ot = math.fabs(round(vs, 5) - round((1/_lambda), 5))
print("Выборочное среднее экспериментальное", round(vs, 5))
print("Выборочное среднее теоретическое", round((1/_lambda), 5))
print("Абсолютное отклонение", a_ot)
print("Относительное отклонение", round((a_ot/round((1/_lambda), 5))*100, 5))
print("------------------------------")

# Выборочная дисперсия с поправкой Шеппарда
vd = 0
for i in range(m):
    vd += ((x[i] - vs) ** 2) * w[i]
vd = vd - (h**2) / 12
a_ot1 = math.fabs(round(vd, 5) - round(_lambda ** (-2), 5))
print("Выборочная дисперсия эксперементальная", round(vd, 5))
print("Выборочная дисперсия теоретическая", round(_lambda ** (-2), 5))
print("Абсолютное отклонение", a_ot1)
print("Относительное отклонение", round((a_ot1/round(_lambda ** (-2), 5))*100, 5))
print("------------------------------")

# Выборочное среднеe квадратическое отклонение
sigma = vd ** 0.5
a_ot2 = math.fabs(round(sigma, 5) - round(1/_lambda, 5))
print("Выборочное средне квадратическое отклонение эксперементальное", round(sigma, 5))
print("Выборочное средне квадратическое отклонение теоретическое", round(1/_lambda, 5))
print("Абсолютное отклонение", a_ot2)
print("Относительное отклонение", round((a_ot2/round(1/_lambda, 5))*100, 5))
print("------------------------------")

# Выборочная мода
k = 0
for i in range(len(w)):
    if w[i] == max(w):
        k = i
mode = a[k] + step * (w[k] - w[k-1]) / (2*w[k] - w[k-1] - w[k+1])
print("Выборочная мода эксперементальная", round(mode, 5))
print("Выборочная мода теоретическая", 0)
print("Абсолютное отклонение", math.fabs(round(mode, 5)))
print("Относительное отклонение", "-")
print("------------------------------")

# Выборочная медиана
sum_w = 0
for i in range(len(w)):
    sum_w += w[i]
    if sum_w == 1/2:
        print("Выборочная медиана эксперементальная", round(a[i+1], 5))
        print("Выборочная медиана теоретическая", round(math.log(2)/_lambda, 5))
        a_ot3 = math.fabs(round(a[i+1], 5) - round(math.log(2)/_lambda, 5))
        print("Абсолютное отклонение", a_ot3)
        print("Относительное отклонение", round((a_ot3 / round(math.log(2)/_lambda, 5)) * 100, 5))
        print("------------------------------")
        break
    if sum_w > 1/2:
        answer = a[i]+step*(0.5-sum_w+w[i])/w[i]
        print("Выборочная медиана эксперементальная", round(answer, 5))
        print("Выборочная медиана теоретическая", round(math.log(2)/_lambda, 5))
        a_ot3_1 = math.fabs(round(answer, 5) - round(math.log(2)/_lambda, 5))
        print("Абсолютное отклонение", a_ot3_1)
        print("Относительное отклонение", round((a_ot3_1 / round(math.log(2)/_lambda, 5)) * 100, 5))
        print("------------------------------")
        break

# Выборочный коэффициент асимметрии и выборочный коэффициент эксцесса
mu1 = vs
mu2 = 0
mu3 = 0
mu4 = 0
for i in range(m):
    mu2 += ((x[i]) ** 2) * w[i]
    mu3 += ((x[i]) ** 3) * w[i]
    mu4 += ((x[i]) ** 4) * w[i]
mu3_0 = mu3 - 3 * mu2 * mu1 + 2 * (mu1 ** 3)
mu4_0 = mu4 - 4 * mu3 * mu1 + 6 * mu2 * (mu1 ** 2) - 3 * (mu1 ** 4)

vka = mu3_0 / (sigma ** 3)
vke = (mu4_0 / (sigma ** 4)) - 3
a_ot4 = math.fabs(round(vka, 6) - 2)
print("Выборочный коэффициент асимметрии эксперементальный", round(vka, 5))
print("Выборочный коэффициент асимметрии теоретический", 2)
print("Абсолютное отклонение", a_ot4)
print("Относительное отклонение", round((a_ot4 / 2) * 100, 5))
print("------------------------------")

a_ot5 = math.fabs(round(vke, 5) - 6)
print("Выборочный коэффициент эксцесса эксперементальный", round(vke, 5))
print("Выборочный коэффициент эксцесса теоретический", 6)
print("Абсолютное отклонение", a_ot5)
print("Относительное отклонение", round((a_ot5 / 6) * 100, 5))

# Таблица сравнения относительных частот и теоретических вероятностей
print("---------------Таблица сравнения относительных частот и теоретических вероятностей---------------")
prob = [i for i in range(m)]
for i in range(m):
    prob[i] = math.exp(-_lambda * a[i]) - math.exp(-_lambda * a[i + 1])
mod = [i for i in range(m)]
delta = 0
for i in range(m):
    mod[i] = round(math.fabs(w[i] - prob[i]), 5)
    if mod[i] > delta:
        delta = mod[i]
    print(i, ".", "Интервал", "[", a[i], ",", a[i+1], "]", "w_j =", w[i], "p_j = ", round(prob[i], 5), "|w_j - p_j| = ", mod[i])
print("Сумма w_i", sum(w), "Сумма p_i", round(sum(prob), 5), "Макс дельта", delta)
