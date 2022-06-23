# Importing random modules
import random


# Declaring variables
class EmployeeDetails:
    def __init__(self, wage_per_hour, emp_work_hour, emp_daily_wage, total_month_wage, emp_total_hour,
                 emp_total_work_days):
        self.wage_per_hour = wage_per_hour
        self.emp_work_hour = emp_work_hour
        self.emp_daily_wage = emp_daily_wage
        self.total_month_wage = total_month_wage
        self.emp_total_hour = emp_total_hour
        self.emp_total_work_days = emp_total_work_days

    # Checking that employee is present for full time , part-time or absent
    def present_for_full_time(self):
        # """
        #     Description:
        #         This function is set employee work hours as 8 for full time presence of employee
        #     Parameter:
        #         None
        #     Return:
        #         Employee Work hours
        # """
        self.emp_work_hour = 8
        return self.emp_work_hour

    def present_for_part_time(self):
        """
            Description:
                This function is set employee work hours as 4 for part time presence of employee
            Parameter:
                None
            Return:
                Employee Work hours
        """
        self.emp_work_hour = 4
        return self.emp_work_hour

    def absent(self):
        """
            Description:
                This function is set employee work hours as 0 for absence of employee
            Parameter:
                None
            Return:
                Employee Work hours
        """
        self.emp_work_hour = 0
        return self.emp_work_hour

    def switch_case(check):
        """
            Description:
                This function is used for implementing switch case for employee attendance
            Parameter:
                This function takes one integer parameter
            Return:
                It returns function value based on choice
        """
        switch = {
            1: check.present_for_full_time(),
            0: check.present_for_part_time(),
        }
        return switch.get(check, "")

        while check.emp_total_hour <= 100 and check.emp_total_work_days < 20:
            check = random.randint(0, 1)
            if not check:
                result = check.absent()
            else:
                check = random.randint(0, 1)
                result = check.switch_case(check)  # Calling function for cases
            print(result)
            if result == 8 or result == 4:
                check.emp_total_work_days += 1
            emp_daily_wage = result * check.wage_per_hour  # Calculating employee daily wage based on work hours
            check.total_month_wage += emp_daily_wage  # Adding daily wage to total wages
            check.emp_total_hour += result

            if check.emp_total_hour > 100:  # Checking that hours are more than 100 or not
                a = check.emp_total_hour - 100
                check.emp_total_hour -= a
                wage = a * check.wage_per_hour  # Calculate extra hours wage
                check.total_month_wage -= wage  # Minus extra hours wage from emp total wage
                return check.total_month_wage


if __name__ == '__main__':
    employee_wage = EmployeeDetails(20, 8, 160, 3200, 160, 20)
    employee_wage.switch_case()

