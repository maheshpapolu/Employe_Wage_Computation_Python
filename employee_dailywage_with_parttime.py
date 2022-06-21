import random  # importing random modules

print("<------------Calculating EmployeeDailyWage Based on Working Hours------------>\n")


class DailyWage:
    def __init__(self, wage_per_hour, emp_work_hour, emp_daily_wage):
        self.wage_per_hour = wage_per_hour
        self.emp_daily_wage = emp_daily_wage
        self.emp_work_hour = emp_work_hour

    # """
    #    Defining a function name calculate Wage and declaring variables

    # """

    # Now checking the employee is present or not

    def get_working_hours(self):
        check = random.randint(0, 2)
        if check == 1:
            result = random.randint(0, 1)
            if result == 0:
                print("Employee is present for part time")
                self.emp_work_hour = 4
            return self
        else:
            print("Employee is present for full time")
            self.emp_work_hour = 8
            return self
        print("Employee is absent")
        emp_work_hour = 0
        return self

    def employee_daily_wage(self):
        print(self.emp_work_hour * self.wage_per_hour)
        return self


if __name__ == '__main__':
    calculate_wage = DailyWage(20, 0, 0)
    calculate_wage.get_working_hours().employee_daily_wage()
    # Calculate the employee daily wage using random result
