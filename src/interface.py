from kivy.app import App
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

class HomeScreen(Screen):
    current_emps = ListProperty([])
    current_projects = ListProperty([])
    def __init__(self, *args, **kwargs):
        super(HomeScreen, self).__init__(*args, **kwargs)
        self.current_emps = [{'text': 'etkin_'},
                     {'text': 'etkin0'}]
        self.current_projects = [{'text': 'ipek_'},
                     {'text': 'ipek0'}]

    def hire_button_on_click(self):
        if not self.ids.applicants.text == "Choose an applicant":
            self.ids.employees.values.append(self.ids.applicants.text)
            self.ids.applicants.values.remove(self.ids.applicants.text)
            self.ids.applicants.text = "Choose an applicant"



class HrSystem(App):
    def build(self):
        return HomeScreen()


HrSystem().run()
