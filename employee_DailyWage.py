import random  # importing random modules


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
        check = random.randint(0, 1)
        emp_work_hour = 0
        if check == 1:
            print("Employee is present")
            emp_work_hour = 8
        return emp_work_hour

    def employee_daily_wage(self, emp_work_hour, wage_per_hour):
        print(type(emp_work_hour))
        print(type(wage_per_hour))
        print(emp_work_hour * wage_per_hour)


if __name__ == '__main__':

    calculate_wage = DailyWage(20, 0, 0)
    print(calculate_wage)
    # Calculate the employee daily wage using random result
    calculate_wage.employee_daily_wage(20, 8)
