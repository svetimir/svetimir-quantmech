# -*- coding: utf-8 -*-

# РЕШЕНИЕ УРАВНЕНИЯ ШРЁДИНГЕРА
# ДЛЯ ЧАСТИЦЫ В ПОТЕНЦИАЛЬНОЙ ЯМЕ
# КОНЕЧНОЙ ВЫСОТЫ (ТУННЕЛЬНЫЙ ЭФФЕКТ)
# AUTHOR: fluxoid, ifi@yandex.ru
# STARTED: 06.09.2018
# VERSION: 0.1
# LATEST FILE REVISION: 07.09.2018

from scipy import integrate
import numpy as np
# на будущее
import math
# ...
import matplotlib.pyplot as plt

# энергия частицы
e=1.3
# константа частицы
h=0.5
# фактор потенциальной ямы
A=1.5
# константы интегрирования
a = 0.0
b = 10.0
step = 0.005
# начальные условия
alpha=0
beta=1
# неиспользуемые дополнительные переменные
omega=1
phi=0


def u(x):
    """
    Функция потенциала,
    прямоугольная потенциальная яма
    """
    if x>5.0:
        return A*1e1
    else:
        return A


def se_solve(Y,x):
    """
    Функция, задающая систему дифференциальных уравнений
    """
    return [Y[1],(e-u(x))/h*Y[0]]


def main():
    # массивы для решения задачи
    a_x=np.arange(a,b,step)
    y=np.arange(a,b,step)
    # интегрируем систему уравнений
    asol=integrate.odeint(se_solve,[alpha,beta],a_x)
    # на графике будем изображать квадрат модуля волновой функции
    # несущий физический смысл плотности вероятности
    for i in range(0,len(asol)):
        y[i]=asol[i][0]**2
    plt.plot(y)
    plt.show()


if __name__ == '__main__':
    main()
