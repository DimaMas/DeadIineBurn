#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#подключаем библиотеку math для использования функции sin
import math
#подключаем библиотеку numpy для использования функции r 
import numpy
#подключаем библиотеку matplotlib и модуль pyplot, называя ее mpp
import matplotlib.pyplot as mpp

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':
    #массив numpy, элементов от 0, с шагов 0.1 в количестве 200 
    arguments = numpy.r_[0:200:0.1]
    #mpp.plot - описание и построение графика
    mpp.plot(
        #построение графика. Переменная а принимает значение элементов массива, функция math.sin отображает
        #на графике tan(a)
        arguments,
        [math.tan(a) * math.tan(a/20.0) for a in arguments]
    )
    #вывод графика на экран
    mpp.show()