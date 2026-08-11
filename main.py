"""
🌑 NYX Android - Personal AI Assistant
"""

import kivy
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.05, 0.08, 1)

class NyxUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 15
        
        self.add_widget(Label(
            text='🌑 NYX',
            font_size='40sp',
            color=(0.8, 0.8, 1, 1),
            size_hint=(1, 0.15)
        ))
        
        self.status = Label(
            text='Mendengarkan...',
            font_size='18sp',
            color=(0.6, 0.6, 0.9, 1),
            size_hint=(1, 0.1)
        )
        self.add_widget(self.status)
        
        self.orb = Label(
            text='🌑',
            font_size='80sp',
            size_hint=(1, 0.3)
        )
        self.add_widget(self.orb)
        
        self.add_widget(Label(
            text='Ucapkan "Nyx" diikuti perintah\n\nContoh:\n"Nyx, timer 5 menit"\n"Nyx, 100 + 200"',
            font_size='14sp',
            color=(0.5, 0.5, 0.7, 1),
            size_hint=(1, 0.3),
            halign='center'
        ))
        
        btn = Button(
            text='🎤 Ketuk untuk bicara',
            size_hint=(1, 0.1),
            background_color=(0.15, 0.15, 0.35, 1)
        )
        btn.bind(on_press=self.on_tap)
        self.add_widget(btn)
    
    def on_tap(self, instance):
        self.status.text = '🎤 Mendengarkan...'
        self.orb.text = '🟣'

class NyxApp(App):
    def build(self):
        return NyxUI()

if __name__ == '__main__':
    NyxApp().run()
