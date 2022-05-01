import scipy.stats as sps


def choose_var():
    v = input("Input variant: ")
    var = int(v)
    if var == 80:
        x = [6.30334, 8.02645, 12.16487, 5.83584, 7.83086, 8.83664, 11.40085, 9.56617,
             5.73439, 8.50632, 10.53921, 8.79242, 10.09223, 8.11867, 7.41681, 10.03095]

        y = [2.07593, 13.02856, 8.29968, 6.49767, 8.40741, 6.84572, 9.48804, 8.26982,
             9.23229, 10.77608, 6.78528, 9.83676, 9.58789, 8.86324, 9.15862, 6.99994]

        z = [5.05028, 5.62454, 14.79647, 9.90348, 9.11461, 9.17246, 3.82668, 9.40738,
             8.85070, 4.16049, 9.01353, 13.81358, 8.98545, 8.55382, 5.77914, 9.02385]
    elif var == 84:
        x = [11.62084, 6.84302, 8.25088, 12.45885, 9.24030, 8.52812, 5.51490, 10.08981,
             9.23398, 5.64812, 8.40212, 8.85134, 8.85888, 11.69726, 5.71799, 10.58310]

        y = [7.54233, 9.63132, 13.30971, 6.04009, 9.54650, 5.19554, 9.30450, 12.93261,
             5.08283, 10.35184, 9.17455, 6.73624, 8.15137, 10.53550, 10.49489, 10.24960]

        z = [7.72909, 9.64423, 8.08131, 10.19118, 3.30469, 4.25265, 9.58360, 7.41564,
             10.78318, 8.79014, 8.51658, 7.88441, 10.68688, 7.17759, 9.30146, 10.11943]
    elif var == 86:
        x = [8.98916, 12.74455, 7.54412, 7.14413, 5.67097, 11.95328, 8.65550, 7.89505,
             12.72736, 13.46213, 8.66133, 6.77688, 9.73556, 15.18698, 4.38339, 11.76695]

        y = [12.11567, 9.91673, 7.23929, 12.86704, 7.02257, 9.00369, 4.69718, 12.07695,
             7.30159, 4.80794, 12.67437, 8.61648, 6.82806, 11.53224, 11.06643, 12.19140]

        z = [1.62073, 6.44220, 6.21874, 11.27553, 9.41593, 12.11049, 12.98772, 7.60639,
             10.80071, 10.35897, 9.74924, 11.85632, 11.94754, 8.48395, 7.89188, 6.74048]
    elif var == 90:
        x = [12.17702, 14.01000, 12.09198, 11.18424, 11.82169, 12.18678, 9.17935, 10.65043,
             7.17028, 10.84520, 8.46016, 8.84723, 9.28104, 8.58507, 8.56640, 7.99559]

        y = [5.93275, 9.89971, 9.91496, 6.28285, 10.52099, 12.62202, 12.55684, 7.37434,
             6.93578, 15.83671, 12.01177, 9.66646, 4.43970, 11.35868, 8.32329, 10.09010]

        z = [9.84826, 5.14551, 12.46817, 11.83668, 11.19952, 5.17841, 10.08253, 14.44858,
             10.13184, 6.25333, 11.63221, 5.40682, 9.21548, 12.85413, 9.21191, 7.85235]
    else:
        print("Проверь номер варианта:"
              "80 - Дзера"
              "84 - Саша"
              "86 - Ира"
              "90 - Даша")
    arr = [x, y, z]
    return arr


u = choose_var()
# Массив
print("---------------Массив---------------")
print(f"X = {u[0]}")
print(f"Y = {u[1]}")
print(f"Z = {u[2]}")

# Количество строк
N = 16

# Задание 4.1
print("---------------Задание 4.1---------------")
# Выборочное среднее
def sample_average(array):
    samp_avg = round(sum(array) / N, 5)
    return samp_avg

# Выборочная несмещенная дисперсия
def sample_variance(array):
    sum_x_2 = 0
    for i in range(N):
        sum_x_2 += array[i]**2
    samp_var = round(sum_x_2 / N, 5)
    return samp_var

# S_2
def s_2(array):
    s_v = sample_variance(array)
    s_a = sample_average(array)
    s2 = (N / (N - 1)) * (s_v - s_a ** 2)
    return round(s2, 5)

# Критерий Tn,m
#Число стпеней свободы для критерия Стьюдента
l = 2 * N - 2

def T(arr_1, arr_2):
    s_x = s_2(arr_1)
    s_y = s_2(arr_2)
    s_a_x = sample_average(arr_1)
    s_a_y = sample_average(arr_2)
    t_n_m = ((s_a_x - s_a_y) / pow(((N - 1) * (s_x + s_y)), 0.5)) * pow((N * N * l) / (2 * N), 0.5)
    return round(t_n_m, 5)

T_arr = [T(u[0], u[1]), T(u[0], u[2]), T(u[1], u[2])]

print("Столбцы  ","_x      "," _y     ","   _x^2        ","_y^2        ","s^2_x    ","s_2_y    ", "Tn,n")
print("(1, 2)   ", sample_average(u[0]), "  ", sample_average(u[1]), "  ", sample_variance(u[0]), "  ", sample_variance(u[1]), "  ", s_2(u[0]), "  ", s_2(u[1]), "  ", T_arr[0])
print("(1, 3)   ", sample_average(u[0]), "  ", sample_average(u[2]), "  ", sample_variance(u[0]), "  ", sample_variance(u[2]), "  ", s_2(u[0]), "  ", s_2(u[2]), "  ", T_arr[1])
print("(2, 3)   ", sample_average(u[1]), "  ", sample_average(u[2]), "  ", sample_variance(u[1]), "  ", sample_variance(u[2]), "  ", s_2(u[1]), "  ", s_2(u[2]), "  ", T_arr[2])

t_critical = round(sps.t.ppf(0.975, l), 5)

conclusion1 = [0 for i in range(3)]
for i in range(3):
    if abs(T_arr[i]) <= t_critical:
        conclusion1[i] = "ВЕРНА"
    else:
        conclusion1[i] = "НЕВЕРНА"
print("Столбцы  ","|Tn,n|  ","t_critical ","Вывод")
print("(1, 2)   ", abs(T_arr[0]), f" {t_critical}    ", conclusion1[0])
print("(1, 3)   ", abs(T_arr[1]), f" {t_critical}    ", conclusion1[1])
print("(2, 3)   ", abs(T_arr[2]), f" {t_critical}    ", conclusion1[2])

# Задание 4.2
print("---------------Задание 4.2---------------")

#  Общее среднее
u_sum = 0
for i in range(3):
    for j in range(N):
        u_sum += u[i][j]
u_avg = round(1/(N*3)*u_sum, 5)

# Групповое среднее
group_avg = [0 for i in range(3)]
group_sum = [0 for i in range(3)]
for i in range(N):
    group_sum[0] += u[0][i]
    group_sum[1] += u[1][i]
    group_sum[2] += u[2][i]
for i in range(3):
    group_avg[i] = round(group_sum[i] / N, 5)

#Общая сумма квадратов отклонений
s_common1 = 0
for i in range(3):
    for j in range(N):
        s_common1 += (u[i][j] - u_avg) ** 2
s_common = round(s_common1, 5)

# Факторная сумма квадратов отклонений
s_fact = 0
s_fact_sum = 0
for i in range(3):
    s_fact_sum += (group_avg[i] - u_avg) ** 2
s_fact = round(N * s_fact_sum, 5)

#Остаточная сумма квадратов отклонений
s_residual = s_common - s_fact

# Значение критерия F_N,m
s_fact_2 = round(s_fact / 2, 5)
s_residual_2 = round(s_residual / (3 * (N-1)), 5)
F_Nm = round(s_fact_2 / s_residual_2, 5)

print("S_общ  ","  S_факт     ","S_ост     ","  s^2_факт   ","s^2_ост   ","k1     ", "k2     ","F_N,m")
print(s_common, s_fact, "   ",s_residual, "  ",s_fact_2, "   ",s_residual_2,"  ", 2,"    ", 3*(N-1), "    ",F_Nm)

#Критическое значение
z_alfa1 = round(sps.f.ppf(0.95, 2, 3*(N-1)), 5)
if F_Nm <= z_alfa1:
    res = "ВЕРНА"
else:
    res = "НЕВЕРНА"

print("Fn,m    ","alfa  ","z_alfa   ","Вывод")
print(F_Nm, " 0,05  ", z_alfa1," ", res)

# Задание 4.3
print("---------------Задание 4.3---------------")
pval_43_arr = [0 for i in range(3)]
pval_43_arr[0] = round(sps.ttest_ind(u[0], u[1], equal_var=True).pvalue, 5)
pval_43_arr[1] = round(sps.ttest_ind(u[0], u[2], equal_var=True).pvalue, 5)
pval_43_arr[2] = round(sps.ttest_ind(u[1], u[2], equal_var=True).pvalue, 5)

print("Столбцы  ","pval    ","альфа   ","Вывод")
conclusion1 = [0 for i in range(3)]
for i in range(3):
    if float(pval_43_arr[i]) >= 0.05:
        conclusion1[i] = "ВЕРНА"
    else:
        conclusion1[i] = "НЕВЕРНА"

print("(1, 2)   ", pval_43_arr[0], " 0,05    ", conclusion1[0])
print("(1, 3)   ", pval_43_arr[1], " 0,05    ", conclusion1[1])
print("(2, 3)   ", pval_43_arr[2], " 0,05    ", conclusion1[2])


# Задание 4.4
pval_44_arr = [0 for i in range(3)]
pval_44_arr[0] = round(sps.ttest_ind(u[0], u[1], equal_var=False).pvalue, 5)
pval_44_arr[1] = round(sps.ttest_ind(u[0], u[2], equal_var=False).pvalue, 5)
pval_44_arr[2] = round(sps.ttest_ind(u[1], u[2], equal_var=False).pvalue, 5)

print("---------------Задание 4.4---------------")
print("Столбцы  ","pval    ","альфа   ","Вывод")
conclusion = [0 for i in range(3)]
for i in range(3):
    if float(pval_44_arr[i]) >= 0.05:
        conclusion[i] = "ВЕРНА"
    else:
        conclusion[i] = "НЕВЕРНА"

print("(1, 2)   ", pval_44_arr[0], " 0,05    ", conclusion[0])
print("(1, 3)   ", pval_44_arr[1], " 0,05    ", conclusion[1])
print("(2, 3)   ", pval_44_arr[2], " 0,05    ", conclusion[2])


# Задание 4.5
print("---------------Задание 4.5---------------")
pval_45 = round(sps.f_oneway(u[0], u[1], u[2]).pvalue, 5)

print("pval    ","альфа   ","Вывод")
if pval_45 >= 0.05:
    print(pval_45, " 0,05", "    ВЕРНА")
else:
    print(pval_45, " 0,05", "    НЕВЕРНА")

# Задание 4.6
print("---------------Задание 4.6---------------")

# Критерий Fn,m
def F(arr_1, arr_2):
    s1 = s_2(arr_1)
    s2 = s_2(arr_2)
    f = max(s1, s2) / min(s1, s2)
    return round(f, 5)

# Число степеней свободы
k = N - 1
F_arr = [F(u[0], u[1]), F(u[0], u[2]), F(u[1], u[2])]

print("Столбцы  ","S1      "," S2     ","   k1   ","k2   ","Fn,m")
print("(1, 2)   ", s_2(u[0]), "  ", s_2(u[1]), "  ", k, "  ", k, "  ", F_arr[0])
print("(1, 3)   ", s_2(u[0]), "  ", s_2(u[2]), "  ", k, "  ", k, "  ",  F_arr[1])
print("(2, 3)   ", s_2(u[1]), "  ", s_2(u[2]), "  ", k, "  ", k, "  ",  F_arr[2])

# z_alfa
z_alfa = round(sps.f.ppf(0.975, k, k), 5)

print("Столбцы  ","Fn,m    ","z_alfa   ","Вывод")
conclusion2 = [0 for i in range(3)]
for i in range(3):
    if F_arr[i] <= z_alfa:
        conclusion2[i] = "ВЕРНА"
    else:
        conclusion2[i] = "НЕВЕРНА"
print("(1, 2)   ", F_arr[0], f" {z_alfa}    ", conclusion2[0])
print("(1, 3)   ", F_arr[1], f" {z_alfa}    ", conclusion2[1])
print("(2, 3)   ", F_arr[2], f" {z_alfa}    ", conclusion2[2])

# Задание 4.7
print("---------------Задание 4.7---------------")
pval_47 = round(sps.bartlett (u[0], u[1], u[2]).pvalue, 5)
print("pval    ","альфа   ","Вывод")

if pval_47 >= 0.05:
    print(pval_47, " 0,05", "    ВЕРНА")
else:
    print(pval_47, " 0,05", "    НЕВЕРНА")

