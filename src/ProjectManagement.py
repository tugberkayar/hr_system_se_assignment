from Project import Project
from Employee import Employee


class ProjectManagement:
    def __init__(self):
        # This class has to know about everything so it holds all projects and employees
        self.projects = dict()
        self.employees = dict()

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
    def create_project(self, pr_id: int, min_emp_num: int, max_emp_num: int):
        exists = self.project_exists(pr_id)
        if exists:
            raise Exception("project already exists")
        if min_emp_num <= 0 or max_emp_num <= min_emp_num:
            raise Exception("Boundaries are not plausible")
        else:
            # if boundaries are plausible create and return a "project" object
            temp = Project(pr_id, min_emp_num, max_emp_num)
            return temp

    def get_emps_ids(self):
        return list(self.employees)

    def employee_exists(self, emp_id: int):
        # get current employees' ids
        ids = self.get_emps_ids()
        # if given id in current ids return True else False
        return emp_id in ids

    def hire_employee(self):
        pass

    # this is for firing employees that not working in a project
    # to use this function remove employee from the project that s/he works on
    def fire_employee(self, employee_id: int):
        # check if id exists
        exists = self.employee_exists(employee_id)
        if not exists:
            raise Exception("Given id could not found in employees list")
        self.employees.pop(employee_id)

    def add_emp_to_project(self, employee_id: int, project_id: int):
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
        return prj.add_emp(emp)

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
        prj_exists = self.project_exists(pr_id)
        if not prj_exists:
            raise Exception("Project does not exist")
        prj = self.projects.get(pr_id)
        if prj.running:
            print("project is already running")
            return False
        if prj.employee_counter <= prj.max_emp_num and prj.employee_counter >= prj.min_emp_num:
            return True
        else:
            return False

    def start_project(self, pr_id: int):
        prj_exists = self.project_exists(pr_id)
        if not prj_exists:
            raise Exception("Project does not exist")
        if self.is_project_ready_to_run(pr_id):
            prj = self.projects.get(pr_id)
            prj.running = True

    def end_project(self, pr_id: int):
        prj_exists = self.project_exists(pr_id)
        if not prj_exists:
            raise Exception("Project does not exist")
        prj = self.projects.get(pr_id)
        if not prj.running:
            raise Exception("Project is not running")
        prj.running = False

