#   Checking employee is present or not using random module

import random
print("<--------Checking Employee is Present or Absent-------->\n")


def attendence():
    check = random.randint(0, 1)  # output 0 or 1
    if check == 1:  # using if statement to print the result
        print("Employee is Present")
    else:
        print("Employee is Absent")


if __name__ == '__main__':
    attendence()
