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
                     {'text': 'etkin0'},
                     {'text': 'etkin1'},
                     {'text': 'etkin2'},
                     {'text': 'etkin3'},
                     {'text': 'etkin4'},
                     {'text': 'etkin5'},
                     {'text': 'etkin6'},
                     {'text': 'etkin7'},
                     {'text': 'etkin8'},
                     {'text': 'etkin8'},
                     {'text': 'etkin8'},
                     {'text': 'etkin8'},
                     {'text': 'etkin8'},
                     {'text': 'etkin8'}]
        self.current_projects = [{'text': 'ipek_'},
                     {'text': 'ipek0'},
                     {'text': 'ipek1'},
                     {'text': 'ipek2'},
                     {'text': 'ipek3'},
                     {'text': 'ipek4'},
                     {'text': 'ipek5'},
                     {'text': 'ipek6'},
                     {'text': 'ipek7'},
                     {'text': 'ipek8'},
                     {'text': 'ipek8'},
                     {'text': 'ipek8'},
                     {'text': 'ipek8'},
                     {'text': 'ipek8'},
                     {'text': 'ipek8'}]

class HrSystem(App):
    def build(self):
        return HomeScreen()


HrSystem().run()
