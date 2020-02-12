# import date time for static method
import datetime


class Employee:

    raise_amnt = 1.04

    # setting attributes for our instances
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # creating methods that will be applied to our instances
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # define email as a method, but use it as an attribute
    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amnt)

    def __repr__(self):
        # method returns string containing printable representation of an object
        # instead of showing memory location of the object (in our case)
        # goal of the method is to be unambiguous
        # usually used by other developers
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        # returns a string containing nicely printable representation of an object
        # goal to be readable (by the end user)
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        # example of an add method
        # add salaries of the 2 employees to get combined salary
        # example: print(emp_1 + emp_2) ---> combined salary
        return self.pay + other.pay

    def __len__(self):
        # return the length of the fullname
        return len(self.fullname())

    # creating class methods
    @classmethod
    def set_raise_amnt(cls, amount):
        cls.raise_amnt = amount

    @classmethod
    def from_string(cls, employee_string):
        first, last, pay = employee_string.split('-')

        # creating new employee value and then returning it
        return cls(first, last, pay)

    # creating an example of the static method
    @staticmethod
    def is_work_day(day):
        # days have weekdays methods, where Monday == 0 and Sunday == 6, use weekday() method
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# create my_date variable, notice, 11 is automatically assigned to the day
my_date = datetime.date(2020, 2, 11)
# check if current day of the week is a workday or not
Employee.is_work_day(my_date)


# Developer class inherits functionality from the Employee class
class Developer(Employee):
    raise_amnt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # keep code DRY and use super() (note that in this case it is a single inheritance)
        # super() gives access to methods, attributes in a parent class,
        # which have been overridden in a sub-class that inherits from it
        # in single inheritance can also use Employee.__init__(self, first, last, pay)
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, num_of_employees=None):
        super().__init__(first, last, pay)
        # very important to use IS instead of ==
        if num_of_employees is None:
            self.num_of_employees = []
        else:
            self.num_of_employees = num_of_employees

    def add_employee(self, employee):
        # check if employee is not in the list, then add employee
        if employee not in self.num_of_employees:
            self.num_of_employees.append(employee)

    def remove_employee(self, employee):
        # check if employee is in the list, remove employee
        if employee in self.num_of_employees:
            self.num_of_employees.remove(employee)

    def print_all_employees(self):
        for employee in self.num_of_employees:
            print(employee.fullname())


emp_str = "Garry-Smith-10000"

# how we create new employee using from_string class method
new_emp3 = Employee.from_string(emp_str)

emp1 = Employee('Nickolas', 'Cage', 10000)
emp2 = Employee('Valeriya', 'Socks', 25000)

dev_1 = Developer('Artur', 'Gem', 15000, 'Python')
dev_2 = Developer('Alex', 'Green', 60000, 'Java Script')

mngr_1 = Manager('Danny', 'Golden', 76000, [dev_1])

# function that tells us if the object is an instance of the class
isinstance(mngr_1, Developer)
# tells if class is the subclass of another class
issubclass(Developer, Employee)

