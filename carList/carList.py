#! /usr/bin/env python3
# -*- coding: utf-8 -*-
print('Input cars name')
name = input()
k = 0
f = open('cars.txt', 'rt', encoding='utf-8')  # Opening for reading

if name in open('cars.txt').read():  # Finding word in file
    k += 1
else:
    k -= 1

if k == -1:
    print('Our list have no price of this car, please input it : ')
    price = input()
    print('Please choose a currency : 1 - USD; 2 - EUR; 3 - GBP :')
    currency = input()
    price = float(price)  # Conversion type for multiplying on float
    if int(currency) == 2:  # Conversion type for comparison
        price = price * 1.11
    if int(currency) == 3:
        price = price * 1.30
    print('Name of car : ', name, '; ', 'car price in USD : ', price)
    f = open('cars.txt', 'a+t', encoding='utf-8')  # Opening file for adding information at the end
    f.write(' ' + name + ' ' + str(int(price)) + ' ')
    print('Successfully added ! Thank you')

if k == 1:
    list = f.read().split(' ')  # Reading file in list and split it
    i = 0
    while i < len(list) - 1:  # Finding car in list
        if list[i] == name:
            print('Car price in USD : ', list[i+1])
        i += 1

f.flush()
f.close()
