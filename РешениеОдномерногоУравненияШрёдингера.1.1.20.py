# Проект: Решение одномерного уравнения Шрёдингера
# Автор: Георгий Яшин, ifi@yandex.ru, 2022
# Лицензия: GNU General Public License v2
# Дата последнего изменения файла: 27.11.2022
# Версия 1.1.20
# Расшифровка индекса версий: Номер выпуска программы. Количество рабочих функций. Номер редактуры

# Copyright (C) 2022 Георгий Яшин

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

from scipy import integrate as Integrator
import numpy as FunkciiChisel
# на будущее
import math as Matematichka
# ...
import matplotlib.pyplot as RisovaljshchikGrafikov

# энергия частицы
EnergiyaChastitsy=1.3
# константа частицы
KonstantaChastitsy=0.5
# фактор потенциальной ямы
FactorPotantsialjnoiYamy=1.5
# константы интегрирования
AbscissaSleva = 0.0
AbscissaSprava = 10.0
ShagPoAbscisse = 0.005
# начальные условия дифференциального уравнения
NachaljnoeUslovieOdin=0
NachaljnoeUslovieDva=1
# неиспользуемые дополнительные переменные
omega=1
phi=0

def FunkciyaPotentsiala(x):
    """
    Функция потенциала,
    прямоугольная потенциальная яма
    """
    if x>5.0:
        return FactorPotantsialjnoiYamy*1e1
    else:
        return FactorPotantsialjnoiYamy

def FunkciyaSistemyUravneniy(MassivOrdinatResheniyDifferentsialjnogoUravneniya,Abscissa):
    """
    Функция, задающая систему дифференциальных уравнений
    """
    return [MassivOrdinatResheniyDifferentsialjnogoUravneniya[1], \
            (EnergiyaChastitsy-FunkciyaPotentsiala(Abscissa))/KonstantaChastitsy* \
            MassivOrdinatResheniyDifferentsialjnogoUravneniya[0]]

def main():
    # массивы для решения задачи
    a_x=FunkciiChisel.arange(AbscissaSleva,AbscissaSprava,ShagPoAbscisse)
    MassivOrdinat=FunkciiChisel.arange(AbscissaSleva,AbscissaSprava,ShagPoAbscisse)
    # интегрируем систему уравнений
    asol=Integrator.odeint(FunkciyaSistemyUravneniy,[NachaljnoeUslovieOdin,NachaljnoeUslovieDva],a_x)
    # коэффициент туннельного эффекта
    KoefficientTunneljnogoEffekta=1e3
    # на графике будем изображать квадрат модуля волновой функции
    # несущий физический смысл плотности вероятности
    Abscissa=0
    for i in range(0,len(asol)):
        MassivOrdinat[i]=asol[i][0]**2
        if Abscissa==5.0:
            MassivOrdinat[i]==0
        if Abscissa>5.0:
            MassivOrdinat[i]=KoefficientTunneljnogoEffekta*Matematichka.exp(-Abscissa)*asol[i][0]**2
        Abscissa+=ShagPoAbscisse
    RisovaljshchikGrafikov.plot(MassivOrdinat)
    RisovaljshchikGrafikov.show()


if __name__ == '__main__':
    main()
