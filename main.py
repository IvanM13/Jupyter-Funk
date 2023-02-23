import numpy as np
import matplotlib.pyplot as plt

a, b, c, d, e = -12, -18, 5, 10, -30
limit = 9
step = 0.01
line_style = '-'
color = 'b'
direct_up = True

def switch_line():
    global line_style
    if line_style == '-':
        line_style = '--'
    else:
        line_style = '-'
    return line_style

# Переключатель цвета линии
def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color


def func(x):
    f = a * x ** 4 * np.sin(np.cos(x)) + b * x ** 3 + c * x ** 2 + d * x + e
    return f


x = np.arange(-limit, limit + 1, step)
x_change = [(-limit, 'limit')]

for i in range(len(x) - 1):
    if func(x[i]) > 0 and func(x[i + 1]) < 0 or func(x[i]) < 0 and func(x[i + 1]) > 0:
        x_acr = np.arange(x[i], x[i + 1], 0.000001)
        for j in range(len(x_acr) - 1):
            if func(x_acr[j]) > 0 and func(x_acr[j + 1]) < 0 or func(x_acr[j]) < 0 and func(x_acr[j + 1]) > 0:
                x_change.append((x_acr[j], 'zero'))
    if direct_up:
        if func(x[i]) > func(x[i + 1]):
            direct_up = False
            x_change.append((x[i], 'dir'))
    else:
        if func(x[i]) < func(x[i + 1]):
            direct_up = True
            x_change.append((x[i], 'dir'))

x_change.append((limit + 1, 'limit'))
for i in range(len(x_change) - 1):
    cur_x = np.arange(x_change[i][0], x_change[i + 1][0] + step, step)
    if x_change[i][1] == 'zero':
        plt.plot(x_change[i][0], func(x_change[i][0]), 'go')
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color)
    else:
        plt.plot(cur_x, func(cur_x), switch_color())

plt.plot(-7.65, func(-7.65), 'go', label='Корни функции f')
plt.plot(-9, func(-9), '', label='Убывает > 0')
plt.plot(-7.651, func(-10), 'b-.', label='Убывает < 0')
plt.plot(10, func(10), 'r--', label='Возрастает < 0')
plt.plot(10, func(10), 'r', label='Возрастает > 0')
plt.legend()
plt.grid()
plt.show()


x_roots = set()
print('Множество корней уравнения для заданного интервала: ')
for i in range(len(x_change) - 1):
    if x_change[i][1] == 'zero':
        x_roots.add(round(float(x_change[i][0]), 3))
all_roots = list(x_roots)
all_roots.sort()
print(*all_roots)

x_extr = set()
print('Экстремумы для заданного интервала: ')
for i in range(len(x_change) - 1):
    if x_change[i][1] == 'dir':
        x_extr.add(round(float(x_change[i][0]), 3))
all_extr = list(x_extr)
all_extr.sort()
print(*all_extr)
