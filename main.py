from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import json
import os

# Sederhana: Kita pake Vosk buat offline voice recognition 
# (Kita panggil lewat terminal dulu biar gak berat di APK)

class NyxMain(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text="Nyx siap membantu...")
        self.add_widget(self.label)
        
        btn = Button(text="Dengar Perintah Suara (Offline)")
        btn.bind(on_press=self.dengar_suara)
        self.add_widget(btn)

    def dengar_suara(self, instance):
        self.label.text = "Mendengarkan... (Simulasi)"
        # Di sini nanti kita bakal sambungin ke Vosk atau engine STT
        # Buat sekarang, kita kasih feedback aja
        Clock.schedule_once(lambda dt: setattr(self.label, 'text', "Kata kunci 'Nyx' terdeteksi!"), 2)

class NyxApp(App):
    def build(self):
        return NyxMain()

if __name__ == "__main__":
    NyxApp().run()