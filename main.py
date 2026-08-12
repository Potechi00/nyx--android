"""
🌑 NYX Android - Personal AI Assistant
v0.3 - Styled UI + Swipe Navigation + Action Ready
"""

import kivy
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.behaviors import TouchRippleBehavior

# ─── Theme ─────────────────────────────
Window.clearcolor = (0.05, 0.05, 0.08, 1)

# ─── Load UI ───────────────────────────
Builder.load_file('nyx/ui/main_screen.kv')


# ═══════════════════════════════════
# SCREENS
# ═══════════════════════════════════

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
            size_hint_y=None,
            height=40,
            padding=[60, 0, 10, 0]
        )
        user_label = Label(
            text=text,
            size_hint_x=0.65,
            halign='right',
            valign='middle',
            color=(1, 1, 1, 1),
            font_size='14sp'
        )
        user_bubble.add_widget(Label(size_hint_x=0.35))
        user_bubble.add_widget(user_label)
        chat_area.add_widget(user_bubble)
        
        # Bubble NYX
        nyx_bubble = BoxLayout(
            size_hint_y=None,
            height=40,
            padding=[10, 0, 60, 0]
        )
        nyx_label = Label(
            text=f"Nyx: '{text}' diterima. Coming soon!",
            size_hint_x=0.65,
            halign='left',
            valign='middle',
            color=(0, 0, 0, 1),
            font_size='14sp'
        )
        nyx_bubble.add_widget(nyx_label)
        nyx_bubble.add_widget(Label(size_hint_x=0.35))
        chat_area.add_widget(nyx_bubble)
        
        chat_input.text = ''


class HistoryScreen(Screen):
    
    def on_enter(self):
        history_list = self.ids.history_list
        history_list.clear_widgets()
        
        items = [
            "✅ Alarm 07:00 - Berhasil",
            "✅ Putar musik - Berhasil",
            "✅ Buka YouTube - Berhasil",
            "✅ Timer 10 menit - Selesai",
            "✅ Alarm 05:00 - Berhasil",
        ]
        
        for item in items:
            box = BoxLayout(size_hint_y=None, height=40, padding=[10,0])
            box.add_widget(Label(
                text=item,
                font_size='13sp',
                color=(0.5, 0.5, 0.7, 1)
            ))
            history_list.add_widget(box)


class ActionScreen(Screen):
    
    def on_action(self, action_name):
        app = App.get_running_app()
        app.show_toast(f"⚡ {action_name} - Coming Soon")


class SettingScreen(Screen):
    pass


# ═══════════════════════════════════
# SWIPE SCREEN MANAGER
# ═══════════════════════════════════

class SwipeScreenManager(ScreenManager):
    """ScreenManager dengan gesture swipe"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
        current_idx = self.screen_order.index(current) if current in self.screen_order else 0
        
        # Swipe left → next screen
        if diff < -80:
            next_idx = min(current_idx + 1, len(self.screen_order) - 1)
            self.current = self.screen_order[next_idx]
        
        # Swipe right → previous screen
        elif diff > 80:
            prev_idx = max(current_idx - 1, 0)
            self.current = self.screen_order[prev_idx]
        
        self._touch_start = None
        return super().on_touch_up(touch)


# ═══════════════════════════════════
# MAIN APP
# ═══════════════════════════════════

class NyxApp(App):
    
    def build(self):
        self.sm = SwipeScreenManager()
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(ChatScreen(name='chat'))
        self.sm.add_widget(HistoryScreen(name='history'))
        self.sm.add_widget(ActionScreen(name='action'))
        self.sm.add_widget(SettingScreen(name='setting'))
        
        # Start di home
        self.sm.current = 'home'
        
        return self.sm
    
    def on_start(self):
        print("🌑 NYX v0.3 Ready")
        print("   🎨 Styled UI + Swipe Navigation")
    
    def switch_screen(self, screen_name):
        self.sm.current = screen_name
    
    def show_toast(self, message):
        print(f"🔔 {message}")


if __name__ == '__main__':
    NyxApp().run()
