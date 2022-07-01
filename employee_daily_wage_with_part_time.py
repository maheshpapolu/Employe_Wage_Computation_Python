import random
import logging
logging.basicConfig(filename="employee_daily_wage_with_part_time.log", filemode="w", level=logging.DEBUG)

IS_ABSENT = 0
IS_PRESENT_FULL_DAY = 1
IS_PRESENT_PART_TIME = 2
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4


class Employee:
    try:
        def __init__(self, emp_name,  emp_wage_per_hour):
            """
            creates employee named class using init method or constructor  and passing parameters
            :param emp_name:
            :param emp_wage_per_hour:
            """
            self.emp_name = emp_name
            self.emp_wage_per_hour = emp_wage_per_hour
            self.comp_max_working_day = 26
            self.comp_max_working_hrs = 8

    except Exception as e:
        print(e.message)

    @staticmethod
    def check_emp_working_hours(check_emp):
        try:
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
        except Exception as t:
            print(t.message)

    def calculate_wage(self):
        try:
            """
            define a function named calculate_wage for calculate the employee wage based on the employee working hour
            using while loop to return the total wage
            :return: total_wage
            """
            working_days = 0
            working_hours = 0
            total_wage = 0
            while working_days <= self.comp_max_working_day and working_hours <= self.comp_max_working_hrs:
                check_emp = random.randrange(0, 2)
                employee_working_hours = self.check_emp_working_hours(check_emp)
                daily_wage = self.emp_wage_per_hour * employee_working_hours
                working_days += 1
                working_hours += employee_working_hours
                total_wage = total_wage + daily_wage
            return total_wage

        except ValueError as w:
            print(w)


class Company:
    try:

        def __init__(self, company_name, maximum_working_hour, maximum_monthly_working_days):
            """
            create a class named as company and used init method or
            constructor to passing the parameters to instance attributes
            :param company_name:
            :param maximum_working_hour:
            :param maximum_monthly_working_days:
            """
            self.company_name = company_name
            self.maximum_working_hour = maximum_working_hour
            self.maximum_monthly_working_days = maximum_monthly_working_days
            self.emp_dict = {}

    except Exception as e:
        print(e.message)

    def total_salary(self):
        return self.maximum_working_hour * self.maximum_monthly_working_days

    def add_employee(self, emp_obj):
        """
        create a function named as add_employee for adding the new employee to the company_obj
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
        try:
            """
            create a function called remove employee in the class of company
            :param employee_name:
            :return:
            """
            if self.get_employee(emp_name=employee_name) is None:
                print("employee not exist")
            else:
                self.emp_dict.pop(employee_name)
        except Exception as r:
            print(r.message)


def add_employee():
    try:
        """
        add a function by the name of add_employee
        :return:
        """
        comp_name = input("Enter company name :- ")
        company_object = company_dict.get(comp_name)
        if company_object is None:
            comp_max_working_hrs = int(input("Enter maximum working hour set by the company:- "))
            comp_max_working_day = int(input("Enter maximum no. of days a employee have to work:- "))
            company_object = Company(comp_name, comp_max_working_hrs, comp_max_working_day)

        wage_per_hour = int(input("Enter wage per hour of employee:- "))
        emp_name = input("Enter employee name:- ")
        employee_obj = Employee(emp_name, wage_per_hour)

        company_object.add_employee(employee_obj)
        company_dict.update({comp_name: company_object})
    except Exception as a:
        print(a.message)


def get_employee():
    try:
        """
        function get_employee
        :return:
        """
        company_name = input("Enter company name :- ")
        comp_obj = company_dict.get(company_name)
        if comp_obj:
            emp_name = input("Enter employee name:- ")
            employee = comp_obj.get_employee(emp_name)
            if employee:
                print(employee.emp_name, employee.emp_working_hour, employee.emp_wage_per_hour)
            else:
                print("employee not exist")
        else:
            print("company not exist")
    except Exception as u:
        print(u.message)


def remove_employee():
    try:
        """
        function remove_employee
        :return:
        """
        comp_name = input("Enter company name :- ")
        company_obj = company_dict.get(comp_name)
        if company_obj:
            employee_name = input("Enter employee name:- ")
            company_obj.remove_employee(employee_name)
        else:
            print("employee or company doesn't exist >>> pls try again")
    except Exception as i:
        print(i.message)


def display_company():
    """
    display_company named function
    :return:
    """
    for key, value in company_dict.items():
        print(key, value.maximum_working_hour, value.maximum_monthly_working_days, value.total_salary())


def display_employee():
    try:
        comp_name = input("please enter the company name:- ")
        company_object = company_dict.get(comp_name)
        if company_object is not None:
            for k, v in company_object.emp_dict.items():
                print(k, v.emp_working_hour, v.emp_wage_per_hour)
        else:
            print("company not exist")
    except Exception as p:
        print(p.message)


if __name__ == '__main__':
    company_dict = {}
    try:
        while True:
            print("1: add_employee,\n2: get_employee,\n3: remove_employee,\n4: display_company,\n5: display_employee\n"
                  "0: quit")
            options = int(input("Enter your choice :- "))
            switcher = {
                1: add_employee,
                2: get_employee,
                3: remove_employee,
                4: display_company,
                5: display_employee
            }
            if options == 0:
                print("quit the program")
                break

            switcher.get(options)()
    except Exception as e:
        print(e.message)
