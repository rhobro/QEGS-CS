#  Copyright © 2020 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: PythonProject
#  File Name: quad_calc.py
#  Last Modified: 29/01/2020, 17:43
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: PythonProject
#  File Name: quad_calc.py
#  Last Modified: 29/01/2020, 17:23

import math
import os
import platform


def clear_screen():
    if platform.platform() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


quit = False

while not quit:
    # Get quadratic calculator values for ax^2 + bx + c = 0
    print("If a quadratic equation is in the format ax^2 + bx + c = 0, enter a, b and c below.")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    solutions = list()

    if (b * b - 4 * a * c) > 0:
        solutions.append((-b + math.sqrt(b * b - 4 * a * c)) / 2 * a)
        solutions.append((-b - math.sqrt(b * b - 4 * a * c)) / 2 * a)

    elif (b * b - 4 * a * c) < 0:
        print("This equation has no solution which is a real number.")

    else:
        solutions.append((-b + math.sqrt(b * b - 4 * a * c)) / 2 * a)

    for i, sol in enumerate(solutions):
        print("Solution {} = {}".format(i + 1, sol))

    if input("Do you want to quit? (Y/n): ").upper() == "Y":
        quit = True
    clear_screen()
