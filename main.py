import random
from tkinter import Button 
import kivymd
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.clipboard import Clipboard


class Password_Style(Screen):
    def mmm(self):
        self.password = ''
        dictionary = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        length = 10
        for i in range(1):
            password = ''
            for j in range(length):
                self.password += random.choice(dictionary)
        return self.password
    def press_button(self):
        self.ids.lable_text_vm.text = self.mmm()
class MyApp(MDApp):
    def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            Builder.load_file('style.kv')
            sm = ScreenManager()
            sm.add_widget(Password_Style(name='start'))
            return sm
    
if __name__ == '__main__':
    MyApp().run()