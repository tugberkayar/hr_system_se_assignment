from abc import ABC
import src.Project as pr
import src.Accounting as ac

class Employee(ABC):

    def __init__(self, salary: float, name: str, emp_id: int, domain: str, accounting = None, project_id= None):
        self.salary = salary
        self.name = name
        self.id = emp_id
        self.domain = domain
        self.project_id = project_id
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
    def project_id(self):
        return self.__project_id

    @project_id.setter
    def project_id(self, new_project:int):
        self.__project_id = new_project

    @property
    def accounting(self):
        return self.__accounting

    @accounting.setter
    def accounting(self, accounting: ac.Accounting):
        self.__accounting = accounting

    def print_info(self):
        print('employee')
    def __str__(self):
        return r"""---------------------
ID   : {id},
Isim : {name},
Maas : {salary},
Alan : {domain},
---------------------
            
        """.format(id=self.id,
                   name=self.name,
                   salary=self.salary,
                   domain=self.domain)


class Analyst(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Analyst', accounting)

    def print_info(self):
        print(self.domain)


class Designer(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Designer', accounting)

    def print_info(self):
        print(self.domain)


class Maintainer(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Maintainer', accounting)

    def print_info(self):
        print(self.domain)


class Manager(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Manager', accounting)

    def print_info(self):
        print(self.domain)


class Programmer(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Programmer', accounting)

    def print_info(self):
        print(self.domain)


class Tester(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Tester', accounting)

    def print_info(self):
        print(self.domain)








