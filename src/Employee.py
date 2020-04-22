from abc import ABC
import src.Project as pr
import src.Accounting as ac

class Employee(ABC):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 domain: str,
                 project = None,
                 accounting = None):

        self.salary = salary
        self.name = name
        self.id = id
        self.domain = domain

        if project is not None:
            self.project = project


        if accounting is not None:
            self.accounting = accounting

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary: float):
        self.__salary = new_salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, new_project: pr.Project):
        self.__project = new_project

    @property
    def accounting(self):
        return self.__accounting

    @accounting.setter
    def accounting(self, accounting: ac.Accounting):
        self.__accounting = accounting

    def print_info(self):
        print('employee')


class Analyst(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Analyst', project, accounting)

    def print_info(self):
        print(self.domain)


class Designer(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Designer', project, accounting)

    def print_info(self):
        print(self.domain)


class Maintainer(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Maintainer', project, accounting)

    def print_info(self):
        print(self.domain)


class Manager(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Manager', project, accounting)

    def print_info(self):
        print(self.domain)


class Programmer(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Programmer', project, accounting)

    def print_info(self):
        print(self.domain)


class Tester(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Tester', project, accounting)

    def print_info(self):
        print(self.domain)








