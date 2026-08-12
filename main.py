"""
🌑 NYX Android - v0.4 Animated UI + Swipe
"""

import kivy
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SlideTransition
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.clock import Clock

# Load UI
Builder.load_file('nyx/ui/main_screen.kv')

Window.clearcolor = (0.04, 0.04, 0.06, 1)


class HomeScreen(Screen):
    pass


class ChatScreen(Screen):
    
    def send_message(self, text):
        if not text.strip():
            return
        
        chat_area = self.ids.chat_area
        chat_input = self.ids.chat_input
        
        # Bubble user
        user_bubble = BoxLayout(
            size_hint_y=None, height=44,
            padding=[70, 0, 10, 0]
        )
        user_label = Label(
            text=text,
            size_hint_x=0.6,
            halign='right', valign='middle',
            color=(1, 1, 1, 1), font_size='14sp'
        )
        user_label.bind(size=user_label.setter('text_size'))
        user_bubble.add_widget(Label(size_hint_x=0.4))
        user_bubble.add_widget(user_label)
        
        # Animasi fade in
        user_bubble.opacity = 0
        chat_area.add_widget(user_bubble)
        Animation(opacity=1, duration=0.3).start(user_bubble)
        
        # Bubble NYX
        def add_nyx_reply(dt):
            nyx_bubble = BoxLayout(
                size_hint_y=None, height=44,
                padding=[10, 0, 70, 0]
            )
            nyx_label = Label(
                text=f"📩 '{text}' diterima!",
                size_hint_x=0.6,
                halign='left', valign='middle',
                color=(0, 0, 0, 1), font_size='14sp'
            )
            nyx_label.bind(size=nyx_label.setter('text_size'))
            nyx_bubble.add_widget(nyx_label)
            nyx_bubble.add_widget(Label(size_hint_x=0.4))
            
            nyx_bubble.opacity = 0
            chat_area.add_widget(nyx_bubble)
            Animation(opacity=1, duration=0.3).start(nyx_bubble)
        
        Clock.schedule_once(add_nyx_reply, 0.5)
        chat_input.text = ''


class HistoryScreen(Screen):
    
    def on_enter(self):
        history_list = self.ids.history_list
        history_list.clear_widgets()
        
        items = [
            ("✅", "Alarm 07:00 - Berhasil"),
            ("✅", "Musik - Diputar"),
            ("✅", "YouTube - Dibuka"),
            ("⏰", "Timer 10 menit - Selesai"),
            ("✅", "Alarm 05:00 - Berhasil"),
        ]
        
        for i, (icon, text) in enumerate(items):
            box = BoxLayout(size_hint_y=None, height=42, padding=[10, 0])
            box.opacity = 0
            box.add_widget(Label(
                text=f"{icon}  {text}",
                font_size='13sp',
                color=(0.5, 0.5, 0.7, 1)
            ))
            history_list.add_widget(box)
            
            # Animasi stagger
            Animation(opacity=1, duration=0.3).start(box)
            # delay per item tidak bisa di kv saja, jadi biar muncul bersamaan dulu


class ActionScreen(Screen):
    
    def on_action(self, action_name):
        app = App.get_running_app()
        app.show_toast(f"⚡ {action_name} - Coming Soon")


class SettingScreen(Screen):
    pass


class SwipeScreenManager(ScreenManager):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = SlideTransition(duration=0.25)
        self._touch_start = None
        self.screen_order = ['home', 'chat', 'action', 'history', 'setting']
    
    def on_touch_down(self, touch):
        self._touch_start = touch.x
        return super().on_touch_down(touch)
    
    def on_touch_up(self, touch):
        if self._touch_start is None:
            return super().on_touch_up(touch)
        
        diff = touch.x - self._touch_start
        current = self.current
        order = self.screen_order
        idx = order.index(current) if current in order else 0
        
        if diff < -100:
            self.transition.direction = 'left'
            next_idx = min(idx + 1, len(order) - 1)
            self.current = order[next_idx]
        elif diff > 100:
            self.transition.direction = 'right'
            prev_idx = max(idx - 1, 0)
            self.current = order[prev_idx]
        
        self._touch_start = None
        return super().on_touch_up(touch)


class NyxApp(App):
    
    def build(self):
        self.sm = SwipeScreenManager()
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(ChatScreen(name='chat'))
        self.sm.add_widget(HistoryScreen(name='history'))
        self.sm.add_widget(ActionScreen(name='action'))
        self.sm.add_widget(SettingScreen(name='setting'))
        return self.sm
    
    def on_start(self):
        print("🌑 NYX v0.4 Animated Ready")
    
    def switch_screen(self, screen_name):
        self.sm.transition.direction = 'left'
        self.sm.current = screen_name
    
    def show_toast(self, message):
        print(f"🔔 {message}")


if __name__ == '__main__':
    NyxApp().run()
