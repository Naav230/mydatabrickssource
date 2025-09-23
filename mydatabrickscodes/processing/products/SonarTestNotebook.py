# Databricks notebook source
# sonar_test.py

import os  # unused import
import sys  # unused import

# Hard-coded credentials
PASSWORD = "12345"

def complex_function(a, b, c):
    # function with too many arguments and complexity
    result = 0
    for i in range(a):
        for j in range(b):
            for k in range(c):
                result += i * j * k
    return result

def duplicate_code_example(x):
    # duplicate code
    y = x * 2
    z = x * 2
    return y + z

def bad_naming_function():
    # variables with bad naming
    a = 10
    b = 20
    c = 30
    return a + b + c

def bare_except_example():
    try:
        value = int("not_a_number")
    except:
        print("Something went wrong")  # bare except

def inefficient_loop(lst):
    # inefficient loop
    result = []
    for i in range(len(lst)):
        result.append(lst[i] * 2)
    return result

# Unused function
def unused_function():
    print("I am never called")

# No main guard
print(complex_function(5, 5, 5))
print(duplicate_code_example(10))
print(bad_naming_function())
bare_except_example()
print(inefficient_loop([1,2,3,4,5]))

