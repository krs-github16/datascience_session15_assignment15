# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 19:26:05 2018

@author: disiz
"""
import math

### Mean Example:
def mean(x):
    return sum(x) / len(x)

### Variances:
def variance(x):
    n = len(x)
    x_bar = mean(x)
    return(round(sum((x_i - x_bar)**2 for x_i in x) / (n), 2))

### Standard deviation:
def standard_deviation(x):
    return(math.sqrt(variance(x)))

test_ex = [5, 5, 9, 12, 2, 4, 18, 11]

"""Problem Statement 1:
You survey households in your area to find the average rent they are paying. Find the
standard deviation from the following data:
$1550, $1700, $900, $850, $1000, $950."""

avg_rent=[1550,1700,900,850,1000,950]
print(avg_rent)
print("*/ assignment 15 output 1/*")
print("\nStandard Deviation for the above data is: ", round(standard_deviation(avg_rent), 2))
print("-"*100)
"""Problem Statement 2:
Find the variance for the following set of data representing trees in California (heights in
feet):
3, 21, 98, 203, 17, 9"""


height_cal=[3, 21, 98, 203, 17, 9]
print(height_cal)
print("*/ assignment 15 output 2/*")
print("\nVariance for the above data is: : ", variance(height_cal))
print("-"*100)
"""Problem Statement 3:
In a class on 100 students, 80 students passed in all subjects, 10 failed in one subject, 7
failed in two subjects and 3 failed in three subjects. Find the probability distribution of
the variable for number of subjects a student from the given class has failed in."""
# Variables from given data
total=100
pass_all=80
fail_one=10
fail_two=7
fail_three=3
print("*/ assignment 15 output 3/*")
print("\nprobability distribution of the variable for ZERO subjects a student from the given class has failed in is (P(X=0)):",pass_all/total)
print("-"*10)
print("probability distribution of the variable for ONE subject a student from the given class has failed in is (P(X=1)):",fail_one/total)
print("-"*10)
print("probability distribution of the variable for TWO subjects a student from the given class has failed in is (P(X=2)):",fail_two/total)
print("-"*10)
print("probability distribution of the variable for THREE subjects a student from the given class has failed in is (P(X=3)):",fail_three/total)
print("-"*100)
print("\nEnd of assignment")



