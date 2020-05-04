from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window
import pandas as pd
import numpy as np
from src.ProjectManagement import ProjectManagement
from src.DataHandler import DataHandler
from src.Employee import Employee
from src.Accounting import Accounting
import tkinter as tk
from tkinter.messagebox import showerror, showinfo
tk.Tk().withdraw()


class HomeScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(HomeScreen, self).__init__(*args, **kwargs)

        self.__data_handler = DataHandler()
        self.__project_manager = ProjectManagement(
            self.__data_handler.load_current_projects(),
            self.__data_handler.load_current_employees()
        )
        self.__applicant_list = self.__data_handler.load_applicants()
        self.__retrieve_project_employees()
        self.reset_applicant_spinner_values()
        self.reset_employee_spinner_values()
        self.reset_project_spinner_values()

    def reset_employee_spinner_values(self):
        self.ids.employees.values = ["Name:{name}, ID:{id}".format(
            name=e.name, id=e.id) for e in self.__project_manager.employees.values()]

    def reset_project_spinner_values(self):
        self.ids.projects.values = ["Name:{name}, ID:{id}".format(
            name=p.name, id=p.id) for p in self.__project_manager.projects.values()]

    def reset_applicant_spinner_values(self):
        self.ids.applicants.values = ["Name:{name}, ID:{id}".format(
            name=a['name'], id=a['id']) for a in self.__applicant_list]

    def hire_button_on_click(self):
        if (not self.ids.applicants.text == "Choose an applicant" and
                not self.ids.accounting_type_spinner.text == "Choose an accounting type"):
            selected_id = int(self.ids.applicants.text.split(":")[-1])
            applicant = self.__applicant_list[selected_id]
            if self.ids.accounting_type_spinner.text == "Default":
                accounting = Accounting(False)
            else:
                accounting = Accounting(True)
            emp = self.__project_manager.hire_employee(name=applicant["name"],
                                                       domain=applicant["domain"],
                                                       def_acc=accounting)
            self.ids.applicants.values.remove(self.ids.applicants.text)
            self.__applicant_list.remove(applicant)
            self.reset_employee_spinner_values()
            self.ids.accounting_type_spinner.text = "Choose an accounting type"
            self.ids.applicants.text = "Choose an applicant"
            # self.accounting_popup.open()
        else:
            showerror("ERROR","Choose an applicant and an accounting type.")

    def new_project_on_click(self):
        if self.ids.text_input_name.text == "":
            showerror("ERROR", "Name field can not be empty.")
        elif (not self.ids.text_input_min.text.isdigit()
              or not self.ids.text_input_max.text.isdigit()):
            showerror("ERROR", "Min-Max values for new project must be integers")
        else:
            status = self.__project_manager.create_project(self.ids.text_input_name.text,
                                                           int(self.ids.text_input_min.text),
                                                           int(self.ids.text_input_max.text))
            if not status:
                showerror(
                    "ERROR", "Minimum employee number can not be smaller than zero and maximum employee number must be greater than minimum employee number.")
            else:
                self.ids.text_input_name.text = ""
                self.ids.text_input_min.text = ""
                self.ids.text_input_max.text = ""
            self.reset_project_spinner_values()
            self.ids.projects.text = "Choose a project"
            self.ids.project_info.text = ""

    def start_project_on_click(self):
        if not self.ids.projects.text == "Choose a project":
            selected_id = int(self.ids.projects.text.split(":")[-1])
            status = self.__project_manager.start_project(selected_id)
            if status == 0:
                self.reset_project_spinner_values()
            elif status == 1:
                showerror(
                    "ERROR", "Minimum employee requirement has not been satisfied.")
            elif status == 2:
                showerror("ERROR", "Project is already running.")
            self.ids.project_info.text = ""
            self.ids.projects.text = "Choose a project"
        else:
            showerror("ERROR", "Choose a project.")

    def end_project_on_click(self):
        if not self.ids.projects.text == "Choose a project":
            selected_id = int(self.ids.projects.text.split(":")[-1])
            prj = self.__project_manager.projects[selected_id]
            status = self.__project_manager.end_project(selected_id)
            if status:
                # self.__project_manager.projects.pop(prj.id)
                self.reset_project_spinner_values()
            else:
                showerror("ERROR", "Project is not running")
            self.ids.project_info.text = ""
            self.ids.projects.text = "Choose a project"
        else:
            showerror("ERROR", "Choose a project.")

    def fire_employee_on_click(self):
        if not self.ids.employees.text == "Choose an employee":
            print(self.ids.employees.text.split(":")[-1])
            selected_id = int(self.ids.employees.text.split(":")[-1])
            temp_emp = self.__project_manager.employees[selected_id]
            compensation = temp_emp.accounting.calc_compensation(temp_emp.salary)
            if self.__project_manager.fire_employee(employee_id=selected_id):
                self.reset_employee_spinner_values()
                showinfo("INFO", "Compensation : {}".format(compensation))
            else:
                showerror(
                    "ERROR", "This employee currently working on a project")
            self.ids.employees.text = "Choose an employee"
        else:
            showerror("ERROR", "Choose an employee")

    def assign_to_project_on_click(self):
        if (self.ids.projects.text != "Choose a project"
                and self.ids.employees.text != "Choose an employee"):
            project_id = int(self.ids.projects.text.split(":")[-1])
            emp_id = int(self.ids.employees.text.split(":")[-1])
            status = self.__project_manager.assign_to_project(
                emp_id, project_id)
            if status == -1:
                showerror(
                    "ERROR", "This employee is already working in a project.")
            elif not status:
                showerror("ERROR", "The capacity of this project is full.")
            self.reset_employee_spinner_values()
            self.reset_project_spinner_values()
            self.ids.employee_info.text = ""
            self.ids.project_info.text = ""
            self.ids.employees.text = "Choose an employee"
            self.ids.projects.text = "Choose a project"
        else:
            showerror("ERROR","Choose an employee and a project.")

    def __retrieve_project_employees(self):
        for e in self.__project_manager.employees.values():
            if not pd.isna(e.project_id):
                self.__project_manager.projects[e.project_id].employees[e.id] = e
                #counter neden artmıyor

    def employee_spinner_select(self):
        if not self.ids.employees.text == "Choose an employee":
            selected_id = int(self.ids.employees.text.split(":")[-1])
            employee = self.__project_manager.employees[selected_id]
            self.ids.employee_info.text = str(employee)
        else:
            self.ids.employee_info.text = ""

    def project_spinner_select(self):
        if not self.ids.projects.text == "Choose a project":
            selected_id = int(self.ids.projects.text.split(":")[-1])
            project = self.__project_manager.projects[selected_id]
            self.ids.project_info.text = str(project)
        else:
            self.ids.project_info.text = ""

    def applicant_spinner_select(self):
        if not self.ids.applicants.text == "Choose an applicant":
            selected_id = int(self.ids.applicants.text.split(":")[-1])
            applicant = self.__applicant_list[selected_id]
            self.ids.applicant_info.text = "Name:{name}\ndomain:{domain}".format(
                name=applicant['name'], domain=applicant['domain'])
        else:
            self.ids.applicant_info.text = ""

    def save_before_exit(self,*args):
        self.__data_handler.save_current_employees(self.__project_manager.employees.values())
        self.__data_handler.save_current_projects(self.__project_manager.projects.values())
        self.__data_handler.save_current_applicants(self.__applicant_list)


class HrSystem(App):

    def build(self):
        self.home_screen = HomeScreen()
        Window.bind(on_request_close = self.home_screen.save_before_exit)
        return self.home_screen

if __name__ == '__main__':
    HrSystem().run()
