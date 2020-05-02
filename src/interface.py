from kivy.app import App
import pandas as pd
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleview import RecycleView
from kivy.properties import ListProperty
from kivy.uix.textinput import TextInput
from src.DataHandler import DataHandler


class HomeScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(HomeScreen, self).__init__(*args, **kwargs)
        self.__data_handler = DataHandler()
        self.__employees_dict = self.__data_handler.load_current_employees()
        self.__applicant_list = self.__data_handler.load_applicants()
        self.__projects_dict = self.__data_handler.load_current_projects()
        self.__retrieve_project_employees()
        self.ids.employees.values = ["Name:{name}, ID:{id}".format(name=e.name, id=e.id) for e in self.__employees_dict.values()]
        self.ids.applicants.values = [a['name'] for a in self.__applicant_list]
        self.ids.projects.values = [str(p.id) for p in self.__projects_dict.values()]

    def hire_button_on_click(self):
        if not self.ids.applicants.text == "Choose an applicant":
            self.ids.employees.values.append(self.ids.applicants.text)
            self.ids.applicants.values.remove(self.ids.applicants.text)
            self.ids.applicants.text = "Choose an applicant"

    def __retrieve_project_employees(self):
        for e in self.__employees_dict.values():
            if not pd.isna(e.project_id):
                self.__projects_dict[e.project_id].employees[e.id] = e



class HrSystem(App):

    def build(self):
        return HomeScreen()



if __name__ == '__main__':
    HrSystem().run()
