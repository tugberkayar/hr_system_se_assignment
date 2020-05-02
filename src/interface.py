from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
import pandas as pd
import numpy as np
from src.ProjectManagement import ProjectManagement
from src.DataHandler import DataHandler
from src.Employee import Employee
import tkinter as tk
from tkinter.messagebox import showerror
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
        self.ids.employees.values = ["Name:{name}, ID:{id}".format(name=e.name, id=e.id) for e in self.__project_manager.employees.values()]

    def reset_project_spinner_values(self):
        self.ids.projects.values = [str(p.id) for p in self.__project_manager.projects.values()]

    def reset_applicant_spinner_values(self):
        self.ids.applicants.values = ["Name:{name}, ID:{id}".format(name =a['name'], id=a['id'] ) for a in self.__applicant_list]
    
    def hire_button_on_click(self):
        if (not self.ids.applicants.text == "Choose an applicant" and
            not self.ids.accounting_type_spinner.text == "Choose an accounting type") :
            selected_id = int(self.ids.applicants.text.split(":")[-1])
            applicant = self.__applicant_list[selected_id]
            if self.ids.accounting_type_spinner.text == "Default":
                accounting = None
            else:
                accounting = "WebService"
            emp = self.__project_manager.hire_employee(name=applicant["name"],
                                                        domain=applicant["domain"],
                                                        default_accounting=accounting)
            
            self.ids.applicants.values.remove(self.ids.applicants.text)
            self.reset_employee_spinner_values()
            self.ids.accounting_type_spinner.text = "Choose an accounting type"
            self.ids.applicants.text = "Choose an applicant"
            #self.accounting_popup.open()

    def new_project_on_click(self):
        pass

    def start_project_on_click(self):
        if not self.ids.projects.text == "Choose a project":
            selected_id = int(self.ids.projects.text)
            status = self.__project_manager.start_project(selected_id)
            if status == 0:
                self.reset_project_spinner_values()
            elif status == 1:
                showerror("ERROR", "Minimum employee requirement has not been satisfied.")
            elif status == 2:
                showerror("ERROR", "Project is already running.")
            self.ids.project_info.text = ""
            self.ids.projects.text = "Choose a project"

        

    def end_project_on_click(self):
        pass

    def fire_employee_on_click(self):
        if not self.ids.employees.text == "Choose an employee":
            print(self.ids.employees.text.split(":")[-1])
            selected_id = int(self.ids.employees.text.split(":")[-1])
            if self.__project_manager.fire_employee(employee_id=selected_id):
                self.reset_employee_spinner_values()
            else:
                showerror("ERROR", "This employee currently working on a project")
            self.ids.employees.text = "Choose an employee"


    def assign_to_project_on_click(self):
        pass

    def __retrieve_project_employees(self):
        for e in self.__project_manager.employees.values():
            if not pd.isna(e.project_id):
                self.__project_manager.projects[e.project_id].employees[e.id] = e

    def employee_spinner_select(self):
        if not self.ids.employees.text == "Choose an employee":
            selected_id = int(self.ids.employees.text.split(":")[-1])
            employee = self.__project_manager.employees[selected_id]
            self.ids.employee_info.text = str(employee)
        else:
            self.ids.employee_info.text = ""

    def project_spinner_select(self):
        if not self.ids.projects.text == "Choose a project":
            selected_id = int(self.ids.projects.text)
            project = self.__project_manager.projects[selected_id]
            self.ids.project_info.text = str(project)
        else:
            self.ids.project_info.text = ""

    def applicant_spinner_select(self):
        if not self.ids.applicants.text == "Choose an applicant":
            selected_id = int(self.ids.applicants.text.split(":")[-1])
            applicant = self.__applicant_list[selected_id]
            self.ids.applicant_info.text = "Name:{name}\ndomain:{domain}".format(name =applicant['name'], domain=applicant['domain'])
        else:
            self.ids.applicant_info.text = ""

class HrSystem(App):

    def build(self):
        return HomeScreen()



if __name__ == '__main__':
    HrSystem().run()
