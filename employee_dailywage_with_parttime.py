import logging
import random

IS_ABSENT = 0
IS_PRESENT_FULL_DAY = 1
IS_PRESENT_PART_TIME = 2
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4


class Employee:

    def __init__(self, emp_name, emp_working_hour, emp_wage_per_hour):
        """
        creates employee named class using init method or constructor  and passing parameters
        :param emp_name:
        :param emp_working_hour:
        :param emp_wage_per_hour:
        """
        self.emp_name = emp_name
        self.emp_working_hour = emp_working_hour
        self.emp_wage_per_hour = emp_wage_per_hour

    @staticmethod
    def check_emp_working_hours(check_emp):
        """
        define a function name called check_emp_working_hours
        :param check_emp:
        :return: emp_attendance.get(check_emp)
        """
        emp_attendance = {
            IS_PRESENT_FULL_DAY: FULL_DAY_HOURS,
            IS_PRESENT_PART_TIME: PART_TIME_HOURS,
            IS_ABSENT: 0
        }
        return emp_attendance.get(check_emp)

    def calculate_wage(self):
        """
        define a function named calculate_wage for calculate the employee wage based on the employee working hour
        using while loop to return the total wage
        :return: total_wage
        """
        global daily_wage
        working_days = 0
        working_hours = 0
        total_wage = 0
        while working_days <= comp_max_working_day and working_hours <= comp_max_working_hrs:

            employee_working_hours = self.check_emp_working_hours(check_emp)
            daily_wage = self.emp_wage_per_hour * employee_working_hours
            working_days += 1
            working_hours += employee_working_hours
            total_wage = total_wage + daily_wage
        return total_wage


class Company:

    def __init__(self, company_name, maximum_working_hour, maximum_monthly_working_days):
        """
        create a class named as company and used init method or
        constructor to passing the parameters to instance attributes
        :param company_name:
        :param maximum_working_hour:
        :param maximum_monthly_working_days:
        """
        # self.emp_name = None
        self.company_name = company_name
        self.maximum_working_hour = maximum_working_hour
        self.maximum_monthly_working_days = maximum_monthly_working_days
        self.emp_dict = {}

    def display_employee(self):
        print(self.emp_dict)

    def add_employee(self, emp_obj):
        """
        create a function named as addd_employee for adding the new employee to the company_obj
        :param emp_obj:
        :return:
        """
        self.emp_dict.update({emp_obj.emp_name: emp_obj})

    def get_employee(self, emp_name):
        """
        create a function named as get_employee in tne company class to get the employee in the company dist
        :param emp_name:
        :return:
        """
        return self.emp_dict.get(emp_name)

    def remove_employee(self, employee_name):
        """
        create a function called remove employee in the class of company
        :param employee_name:
        :return:
        """
        if self.get_employee(emp_name=employee_name) is None:
            print("employee not exist")
        else:
            self.emp_dict.pop(employee_name)

    # def add_company(self, com_name):
    #     company_dict[com_name] = company_obj


if __name__ == '__main__':
    try:

        # employee_dict = {}
        company_dict = {}

        while True:
            check_emp = random.randrange(0, 2)
            emp_hour = Employee.check_emp_working_hours(check_emp)
            print("Choose operation you want to perform :- ")
            print("1 -> Add Employee")
            print("2 -> get Employee")
            print("3 -> remove Employee")
            print()
            print("4 -> Quit")

            options = int(input("Enter your choice :- "))
            if options == 1:
                comp_name = input("Enter company name :- ")
                comp_max_working_hrs = int(input("Enter maximum working hour set by the company:- "))
                comp_max_working_day = int(input("Enter maximum no. of days a employee have to work:- "))
                wage_per_hour = int(input("Enter wage per hour of employee:- "))
                employee_name = input("Enter employee name:- ")
                employee_obj = Employee(employee_name, emp_hour, wage_per_hour)
                company_obj = Company(comp_name, comp_max_working_hrs, comp_max_working_day)
                company_obj.add_employee(employee_obj)
                company_dict.update({comp_name: company_obj})
                # print(employee_dict)
                company_obj.display_employee()
                print("company object is ", company_obj)
                print(company_dict)
                print(
                    f" Total wage of the employee is : {company_obj.emp_dict.get(employee_name).emp_name}"
                    f"{company_obj.emp_dict.get(employee_name).calculate_wage()}")
            elif options == 2:

                # company_dict={comp_name:comp_obj}
                comp_name = input("Enter company name :- ")
                company_obj = company_dict.get(comp_name)
                if company_obj:
                    employee_name = input("Enter employee name:- ")
                    employee = company_obj.get_employee(employee_name)
                    if employee:
                        print(employee.emp_name, employee.emp_working_hour, employee.emp_wage_per_hour)
                    else:
                        print("employee not exist")
                else:
                    print("company not exist")
            elif options == 3:
                comp_name = input("Enter company name :- ")
                company_obj = company_dict.get(comp_name)
                if company_obj:
                    employee_name = input("Enter employee name:- ")
                    company_obj.remove_employee(employee_name)
                else:
                    print("employee or company doesn't exist >>> pls try again")
            else:
                break
    except Exception as e:
        print(e)
        logging.error(e)
