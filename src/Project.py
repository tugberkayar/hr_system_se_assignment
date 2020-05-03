class Project:

    def __init__(self, pr_id: int, name: str, min_emp_num: int, max_emp_num: int, emp_counter=0, employees=None, running=False):
        self.id = pr_id
        self.name = name
        self.min_emp_num = min_emp_num
        self.max_emp_num = max_emp_num
        self.emp_counter = emp_counter
        if employees is None:
            self.employees = dict()
        else:
            self.employees = employees
        self.running = running

    @property
    def min_emp_num(self):
        return self.__min_emp_num

    @min_emp_num.setter
    def min_emp_num(self, min_emp_num: int):
        self.__min_emp_num = min_emp_num

    @property
    def max_emp_num(self):
        return self.__max_emp_num

    @max_emp_num.setter
    def max_emp_num(self, max_emp_num: int):
        self.__max_emp_num = max_emp_num

    @property
    def emp_counter(self):
        return self.__emp_counter

    @emp_counter.setter
    def emp_counter(self, value: int):
        self.__emp_counter = value

    @property
    def employees(self):
        return self.__employees

    # fixes no member named __employees problem??
    @employees.setter
    def employees(self, employees):
        self.__employees = employees

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    def __str__(self):
        return "id : {}\nname:{}\nmin_emp_num : {}\nmax_emp_num : {}\nemp_counter : {}\nis_running : {}\n".format(self.id, self.name, self.__min_emp_num, self.__max_emp_num, self.__emp_counter, self.running)

    def add_emp(self, new_emp):
        if self.max_emp_num == self.emp_counter:
            return False
        elif new_emp.id in self.employees.keys():
            return False
        else:
            self.employees[new_emp.id] = new_emp
            self.emp_counter += 1
            new_emp.project_id = self.id
            return True

    def remove_emp(self, employee_id: int):
        if employee_id not in self.employees.keys():
            print('Bu kisi bu projede calismiyor')
            return False
        elif self.emp_counter == self.min_emp_num:
            print('Calisani cikaramazsiniz. Minimum sayida kisi calisiyor.')
            return False
        else:
            self.employees.pop(employee_id)
            self.emp_counter -= 1
            return True

    def print_all_employees(self):
        for e in self.employees:
            print(self.employees[e])
