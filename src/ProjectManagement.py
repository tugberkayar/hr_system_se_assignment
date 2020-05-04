from src.Project import Project
from src.Employee import Employee
from src.Accounting import Accounting
import numpy as np
import pandas as pd
import random


class ProjectManagement:
    def __init__(self, projects: dict, employees: dict):
        # This class has to know about everything so it holds all projects and employees
        self.projects = projects
        self.employees = employees

    @property
    def projects(self):
        return self.__projects

    @projects.setter
    def projects(self, projects: dict):
        self.__projects = projects

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, employees: dict):
        self.__employees = employees

    def get_projects_ids(self):
        return list(self.projects)

    def project_exists(self, pr_id: int):
        ids = self.get_projects_ids()
        return pr_id in ids

    def is_project_running(self, pr_id: int):
        exists = self.project_exists(pr_id)
        if not exists:
            raise Exception("Project does not exist")
        else:
            prj = self.projects.get(pr_id)
            return prj.running

    # create a project with min and max number of employee constraints
    def create_project(self, name: str, min_emp_num: int, max_emp_num: int):
        if min_emp_num <= 0 or max_emp_num <= min_emp_num:
            return False
        else:
            # if boundaries are plausible create and return a "project" object
            ids = self.get_projects_ids()
            generated_id = np.array(ids).max() + 1
            temp = Project(generated_id, name , min_emp_num, max_emp_num)
            # append newly created project to projects list
            self.projects[temp.id] = temp
            return True

    def get_emps_ids(self):
        return list(self.employees)

    def employee_exists(self, emp_id: int):
        # get current employees' ids
        ids = self.get_emps_ids()
        # if given id in current ids return True else False
        return emp_id in ids

    def hire_employee(self, name: str, domain: str, def_acc=None):
        # generate id
        ids = self.get_emps_ids()
        if len(ids) == 0:
            generated_id = 1000
        else:
            generated_id = np.array(ids).max() + 1
        # generate salary
        random_salary = 4000 + np.random.rand(1)[0] * 1000
        # decide if using webservice of default accounting
        if def_acc is None:
            accounting = Accounting(False)
        else:
            accounting = Accounting(True)
        # create employee
        emp = Employee(salary=random_salary,
                       name=name,
                       emp_id=generated_id,
                       domain=domain,
                       accounting=accounting
                       )
        # add employee to list
        self.employees[emp.id] = emp
        # override for reading from file ???
        return emp

    # this is for firing employees that not working in a project
    # to use this function remove employee from the project that s/he works on
    def fire_employee(self, employee_id: int):
        # get employee
        emp = self.employees[employee_id]
        # check if working on a project and if project is running
        if not pd.isna(emp.project_id):
            if self.projects[emp.project_id].running:
                return False
        self.employees.pop(employee_id)
        return True

    def check_if_all_projects_maxed(self):
        for p in self.projects:
            if not self.projects[p].emp_counter == self.projects[p].max_emp_num:
                return False
        return True

    def assign_to_project(self, employee_id: int, project_id: int):
        emp = self.employees[employee_id]
        if not pd.isna(emp.project_id):
            return -1
        prj = self.projects[project_id]
        return prj.add_emp(emp)

#    def random_assign_to_project(self, employee_id: int):
#        if self.check_if_all_projects_maxed():
#            return False
#        else:
#            status = False
#            while not status:
#                random_project_id = random.choice(list(self.projects))
#                status = self.assign_to_project(employee_id, random_project_id)
#            return True

    def remove_emp_from_project(self, employee_id: int, project_id: int):
        emp_exists = self.employee_exists(employee_id)
        prj_exists = self.project_exists(project_id)
        if not emp_exists:
            print("employee does not exist")
            return False
        if not prj_exists:
            print("project does not exist")
            return False
        emp = self.employees.get(employee_id)
        prj = self.projects.get(project_id)
        return prj.remove_emp(emp)

    def is_project_ready_to_run(self, pr_id: int):
        prj = self.projects.get(pr_id)
        if prj.running:
            return 2
        if prj.emp_counter < prj.min_emp_num:
            return 1
        return 0

    def start_project(self, pr_id: int):
        status = self.is_project_ready_to_run(pr_id)
        if status == 0:
            self.projects[pr_id].running = True
        return status

    def end_project(self, pr_id: int):
        prj = self.projects.get(pr_id)
        if prj.running:
            prj.running = False
            prj = self.projects.pop(pr_id)
            # for emp_id in prj.employees:
            #    status = self.random_assign_to_project(emp_id)
            #    if not status:
            #        self.employees[emp_id].project_id = None
            for emp_id in prj.employees:
                self.employees[emp_id].project_id = None
            return True
        else:
            return False

    def print_all_projects(self):
        for p in self.projects:
            print(self.projects[p])

    def print_all_employees(self):
        for e in self.employees:
            print(self.employees[e])
