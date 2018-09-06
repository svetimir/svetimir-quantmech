# -*- coding: utf-8 -*-

# РЕШЕНИЕ УРАВНЕНИЯ ШРЁДИНГЕРА
# ДЛЯ ЧАСТИЦЫ В ПОТЕНЦИАЛЬНОЙ ЯМЕ
# КОНЕЧНОЙ ВЫСОТЫ (ТУННЕЛЬНЫЙ ЭФФЕКТ)
# AUTHOR: fluxoid, ifi@yandex.ru
# STARTED: 06.09.2018
# VERSION: 0.1
# LATEST FILE REVISION: 06.09.2018

from scipy import integrate
import numpy as np
import math
import matplotlib.pyplot as plt

e=1.3
h=0.5
A=1.5
omega=1
phi=0


def u(x):
    if x>5.0:
        return A*1e1
    else:
        return A


def se_solve(Y,x):
    return [Y[1],(e-u(x))/h*Y[0]]


def main():
    a=0.0
    b=10.0
    step=0.005
    N=int((b-a)/step)
    a_x=np.arange(a,b,step)
    y=np.arange(a,b,step)
    asol=integrate.odeint(se_solve,[0,1],a_x)
    print(asol)
    for i in range(0,len(asol)):
        y[i]=asol[i][0]**2
    plt.plot(y)
    plt.show()


if __name__ == '__main__':
    main()
