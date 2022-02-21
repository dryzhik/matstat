import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import random
from matplotlib import ticker

random.seed(5)

# Ввод варианта
var = input("Input variant: ")
V = int(var)
p = 0.25 + 0.005 * V
q = 1 - p

# Выборка неупорядоченная
unordered_selection = np.random.geometric(p, 200)
for i in range(len(unordered_selection)):
    unordered_selection[i] = unordered_selection[i] - 1
print(unordered_selection)

# Выборка упорядоченная
ordered_selection = np.sort(unordered_selection)
print(ordered_selection)

# Значения для статистического ряда
# x_i
x = np.unique(ordered_selection)
print("x_i", x)

# n_i
n = np.unique(ordered_selection, return_counts=True)
print("n_i", n[1])

# w_i
arr_size = n[1].size
w = [i for i in range(arr_size)]

for j in range(arr_size):
    w[j] = n[1][j]/200
print("w_i", np.around(w, decimals=5))

# s_i
s = [i for i in range(arr_size)]
s[0] = w[0]
for j in range(1, arr_size):
    s[j] = s[j - 1] + w[j]
print("s_i", np.around(s, decimals=5))

# Полигон относительных частот
fig, ox = plt.subplots()
ox.plot(x, w)
ox.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ox.xaxis.set_major_locator(ticker.MultipleLocator(1))

prob = [i for i in range(arr_size)]
for i in range(arr_size):
    prob[i] = (q ** (x[i])) * p
ox.plot(x, prob, 'r')
plt.title("Полигон относительных частот")
plt.grid()
plt.show()

# Эмпирическая функция распределения
fig, ax = plt.subplots()

for i in range(arr_size - 1):
    ax.plot([x[i], x[i+1]], [s[i], s[i]])
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.title("Эмпирическая функция распределения")
plt.grid()
plt.show()

# Выборочное среднее
vs = 0
for i in range(arr_size):
    vs += x[i] * w[i]
print("Выборочное среднее экспериментальное", round(vs, 6))
print("Выборочное среднее теоретическое", round((q / p), 6))

# Выборочная дисперсия
vd = 0
for i in range(arr_size):
    vd += ((x[i] - vs) ** 2) * w[i]
print("Выборочная дисперсия эксперементальная", round(vd, 6))
print("Выборочная дисперсия теоретическая", round((q / (p ** 2)), 6))

# Выборочное средне квадратическое отклонение
sigma = vd ** 0.5
print("Выборочное средне квадратическое отклонение эксперементальное", round(sigma, 6))
print("Выборочное средне квадратическое отклонение теоретическое", round(((q ** 0.5) / p), 6))

# Выборочная мода
max_w = max(w)
sum_x = 0
num_x = 0
mode = 0

for i in range(arr_size):
    if w[i] == max_w:
        if sum_x > 0 and w[i] != w[i-1]:
            print("Моды не существует")
        sum_x += x[i]
        num_x += 1
    mode = sum_x/num_x
print("Выборочная мода эксперементальная", round(mode, 6))
print("Выборочная мода теоретическая", 0)

# Выборочная медиана
for i in range(arr_size):
    if i == 0:
        if s[i] > 0.5:
            print("Выборочная медиана эксперементальная", x[i])
            break
        if s[i] == 0.5:
            print("Выборочная медиана эксперементальная", (x[i]+x[i+1])/2)
            break
    if (s[i] > 0.5) and (s[i-1] < 0.5):
        print("Выборочная медиана эксперементальная", x[i])
    if s[i] == 0.5:
        print("Выборочная медиана эксперементальная", (x[i] + x[i + 1]) / 2)
        break
val = math.log(2) / math.log(q)
if int(val) == float(val):
    print("Выборочная медиана теоретическая", round(-val - 0.5, 6))
else:
    print("Выборочная медиана теоретическая", round(-val, 6))

# Выборочный коэффициент асимметрии и выборочный коэффициент эксцесса
mu1 = vs
mu2 = 0
mu3 = 0
mu4 = 0
for i in range(arr_size):
    mu2 += ((x[i]) ** 2) * w[i]
    mu3 += ((x[i]) ** 3) * w[i]
    mu4 += ((x[i]) ** 4) * w[i]
mu3_0 = mu3 - 3 * mu2 * mu1 + 2 * (mu1 ** 3)
mu4_0 = mu4 - 4 * mu3 * mu1 + 6 * mu2 * (mu1 ** 2) - 3 * (mu1 ** 4)

vka = mu3_0 / (sigma ** 3)
vke = (mu4_0 / (sigma ** 4)) - 3
print("Выборочный коэффициент асимметрии эксперементальный", round(vka, 6))
print("Выборочный коэффициент асимметрии теоретический", round(((2 - p) / (q ** 0.5)), 6))

print("Выборочный коэффициент эксцесса эксперементальный", round(vke, 6))
print("Выборочный коэффициент эксцесса теоретический", round((6 + ((p ** 2) / q)), 6))

# Таблица сравнения относительных частот и теоретических вероятностей
mod = [i for i in range(arr_size)]
for i in range(arr_size):
    mod[i] = math.fabs(w[i] - prob[i])
    print("Разница w и prob j =", x[i], "w_j =", w[i], "p_j = ", prob[i], "|w_j - p_j| = ", mod[i])
