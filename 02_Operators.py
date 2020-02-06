#Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

#Input Format
#The first line has a double, mealCost (the cost of the meal before tax and tip).
#The second line has an integer, tipPercent (the percentage of  being added as tip).
#The third line has an integer,  taxPercent(the percentage of  being added as tax).


import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    cal_tip = meal_cost * tip_percent / 100
    cal_tax = meal_cost * tax_percent / 100
    totalCost = meal_cost + cal_tip + cal_tax
    print(str(round(totalCost)))
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())
    
    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
