import random
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelness)s - %(message)s')
logging.warning('This will get logged to a file')


class ComputeEmployeeWage:
    IS_FULL_TIME = 1
    IS_PART_TIME = 2
    emp_wage_per_month = 0

    def __init__(self, company, emp_rate, num_of_days, max_hours):
        self.company = company
        self.emp_rate = emp_rate
        self.num_of_days = num_of_days
        self.max_hours = max_hours
        self.dict_ = {}

    def calculate_employee_wage_for_company(self):
        """
        used to calculate employee wage for company
        :return:  employee wage per month
        """

        total_emp_hours = 0
        total_working_days = 0
        while total_emp_hours <= self.max_hours and total_working_days < self.num_of_days:
            total_working_days += total_working_days
            emp_check = int(random.randint(0, 2))
            emp_hrs_dict = {self.IS_FULL_TIME: 8, self.IS_PART_TIME: 4, 0: 0}
            emp_hrs_dict.get(emp_check)
            total_emp_hours += emp_hrs_dict.get(emp_check)
            emp_wage_per_day = emp_hrs_dict.get(emp_check) * self.emp_rate
            self.emp_wage_per_month += emp_wage_per_day

        return self.emp_wage_per_month

    def display(self):
        """
        used for display computed wage
        :return:company name
        """
        print("Company Name= {}".format(self.company))
        print("Employee Wage Per Month {}".format(self.emp_wage_per_month))
        return self.company


if __name__ == "__main__":
    try:
        company_name = input("enter the company name")
        emp_rate = int(input("Enter Employee rate"))
        num_of_days = int(input("Enter the Number of Days"))
        max_hours = int(input("Enter the Max Hours"))
        company = ComputeEmployeeWage(company_name, emp_rate, num_of_days, max_hours)
        company.calculate_employee_wage_for_company()
        company.display()

    except Exception as e:
        print(e)
        logging.error(e)
