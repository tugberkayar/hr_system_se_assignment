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
    data = ListProperty([])

    def __init__(self, *args, **kwargs):
        super(HomeScreen, self).__init__(*args, **kwargs)
        self.data = [{'text': 'etkin_'},
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
                     {'text': 'etkin8'},]


class HrSystem(App):
    def build(self):
        return HomeScreen()


HrSystem().run()
