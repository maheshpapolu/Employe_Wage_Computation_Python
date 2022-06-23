import random  # importing random modules

print("<------------Calculating EmployeeDailyWage Based on Working Hours------------>\n")
print("<-------Switch Case------->")


class Employee:
    """
           Defining a function name MonthlyWage and declaring variables

        """
    def __init__(self, wage_per_hour, emp_work_hour, emp_daily_wage, total_monthly_wage, employee_name):
        self.wage_per_hour = wage_per_hour
        self.emp_daily_wage = emp_daily_wage
        self.emp_work_hour = emp_work_hour
        self.total_monthly_wage = total_monthly_wage
        self.employee_name = employee_name

    # Now checking the employee is present or not
    def present_for_full_time(self):
        """
        this function is set to employee working hours as 8 hrs
        :return: emp_work_hour
        """
        self.emp_work_hour = 8
        return self.emp_work_hour

    def present_for_part_time(self):
        """
        this function is set to employee working hours as 4 hrs
        :return: emp_work_hour
        """
        self.emp_work_hour = 4
        return self.emp_work_hour

    def employee_absent(self):
        """
        this function is set to employee as absent
        :return: emp_work_hour
        """
        self.emp_work_hour = 0
        return self.emp_work_hour

    def switch_case(self, user_input):

        """
        implementing switch case in this function
        :return: emp_status
        """
        switch = {
            1: self.present_for_full_time,
            0: self.present_for_part_time
        }
        # self.present_for_full_time
        return switch.get(user_input)()

    def employee_daily_wage(self):
        result = 1
        for day in range(20):
            check = random.randint(0, 2)
            if check == 2:
                result = self.employee_absent()
            elif check == 1:
                result = self.present_for_full_time()
            else:
                result = self.present_for_part_time()

        print(result * self.wage_per_hour)
        return result * self.wage_per_hour

    def emp_monthly_total(self):
        self.total_monthly_wage += self.emp_daily_wage
        print(self.total_monthly_wage)
        return self.total_monthly_wage


if __name__ == '__main__':
    daily_total_wage = Employee(20, 0, 5, 0, 0)
    data = daily_total_wage.emp_monthly_total()
    print(data)
    # Calculate the employee daily wage using random result
