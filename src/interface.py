from kivy.app import App
import pandas as pd
from kivy.uix.screenmanager import Screen
from src.DataHandler import DataHandler
from src.Employee import Employee
from src.ProjectManagement import ProjectManagement


class HomeScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(HomeScreen, self).__init__(*args, **kwargs)

        self.__data_handler = DataHandler()
        self.__project_manager = ProjectManagement(
            self.__data_handler.load_current_employees(),
            self.__data_handler.load_applicants()
        )

        self.__employees_dict = self.__data_handler.load_current_employees()
        self.__applicant_list = self.__data_handler.load_applicants()
        self.__projects_dict = self.__data_handler.load_current_projects()
        self.__retrieve_project_employees()
        self.ids.employees.values = ["Name:{name}, ID:{id}".format(name=e.name, id=e.id) for e in self.__employees_dict.values()]
        self.ids.applicants.values = ["Name:{name}, ID:{id}".format(name =a['name'], id=a['id'] ) for a in self.__applicant_list]
        self.ids.projects.values = [str(p.id) for p in self.__projects_dict.values()]

    def hire_button_on_click(self):
        if not self.ids.applicants.text == "Choose an applicant":
            selected_id = int(self.ids.applicants.text.split(":")[-1])
            applicant = self.__applicant_list[selected_id]
            random_salary = 4000 + np.random.rand(1)[0] * 1000
            employee = Employee(salary=random_salary, name=applicant['name'], emp_id=)

    def new_project_on_click(self):
        pass

    def start_project_on_click(self):
        pass

    def end_project_on_click(self):
        pass

    def fire_employee_on_click(self):
        pass

    def assign_to_project_on_click(self):
        pass

    def __retrieve_project_employees(self):
        for e in self.__employees_dict.values():
            if not pd.isna(e.project_id):
                self.__projects_dict[e.project_id].employees[e.id] = e

    def employee_spinner_select(self):
        selected_id = int(self.ids.employees.text.split(":")[-1])
        employee = self.__employees_dict[selected_id]
        self.ids.employee_info.text = str(employee)
    
    def project_spinner_select(self):
        selected_id = int(self.ids.projects.text)
        project = self.__projects_dict[selected_id]
        self.ids.project_info.text = str(project)

    def applicant_spinner_select(self):
        selected_id = int(self.ids.applicants.text.split(":")[-1])
        applicant = self.__applicant_list[selected_id]
        self.ids.applicant_info.text = "Name:{name}\ndomain:{domain}".format(name =applicant['name'], domain=applicant['domain'])


class HrSystem(App):

    def build(self):
        return HomeScreen()



if __name__ == '__main__':
    HrSystem().run()
