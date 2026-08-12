"""
🌑 NYX Android - Personal AI Assistant
v0.2 - Multi Screen UI + Action System Ready
"""

import kivy
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder

# ─── Theme ─────────────────────────────
Window.clearcolor = (0.05, 0.05, 0.08, 1)

BLUE = (0.29, 0.56, 0.85, 1)
DARK_SURFACE = (0.08, 0.08, 0.12, 1)
WHITE = (0.9, 0.9, 1, 1)
GRAY = (0.5, 0.5, 0.7, 1)

# ─── Load UI Layout ────────────────────
Builder.load_file('nyx/ui/main_screen.kv')


# ═══════════════════════════════════════
# SCREENS
# ═══════════════════════════════════════

class HomeScreen(Screen):
    """Beranda - Ringkasan + Quick Actions"""
    pass


class ChatScreen(Screen):
    """Chat dengan NYX"""
    
    def send_message(self, text):
        if not text.strip():
            return
        
        chat_area = self.ids.chat_area
        chat_input = self.ids.chat_input
        
        # Bubble user
        user_bubble = BoxLayout(
            size_hint_y=None,
            height=40,
            padding=[50, 0, 5, 0]
        )
        user_label = Label(
            text=text,
            size_hint_x=0.7,
            halign='right',
            color=WHITE,
            font_size='14sp'
        )
        user_bubble.add_widget(Label(size_hint_x=0.3))  # spacer
        user_bubble.add_widget(user_label)
        chat_area.add_widget(user_bubble)
        
        # Bubble NYX (simulasi)
        nyx_bubble = BoxLayout(
            size_hint_y=None,
            height=40,
            padding=[5, 0, 50, 0]
        )
        nyx_label = Label(
            text=f"Nyx: Aku dengar '{text}'. Fitur coming soon!",
            size_hint_x=0.7,
            halign='left',
            color=(0, 0, 0, 1),
            font_size='14sp'
        )
        nyx_bubble.add_widget(nyx_label)
        nyx_bubble.add_widget(Label(size_hint_x=0.3))  # spacer
        chat_area.add_widget(nyx_bubble)
        
        chat_input.text = ''


class HistoryScreen(Screen):
    """Riwayat aktivitas"""
    
    def on_enter(self):
        history_list = self.ids.history_list
        history_list.clear_widgets()
        
        # Data dummy
        items = [
            "✅ Alarm 07:00 - Berhasil",
            "✅ Putar musik - Berhasil",
            "✅ Buka YouTube - Berhasil",
            "✅ Timer 10 menit - Selesai",
            "✅ Alarm 05:00 - Berhasil",
        ]
        
        for item in items:
            box = BoxLayout(
                size_hint_y=None,
                height=35
            )
            box.add_widget(Label(
                text=item,
                font_size='13sp',
                color=GRAY
            ))
            history_list.add_widget(box)


class ActionScreen(Screen):
    """Grid aksi cepat"""
    
    def on_action(self, action_name):
        app = App.get_running_app()
        app.show_toast(f"⚡ {action_name} - Coming Soon")


class SettingScreen(Screen):
    """Pengaturan"""
    pass


# ═══════════════════════════════════════
# MAIN APP
# ═══════════════════════════════════════

class NyxApp(App):
    """🌑 NYX Main Application"""
    
    current_tab = StringProperty('home')
    
    def build(self):
        # Screen Manager
        self.sm = ScreenManager()
        
        # Register screens
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(ChatScreen(name='chat'))
        self.sm.add_widget(HistoryScreen(name='history'))
        self.sm.add_widget(ActionScreen(name='action'))
        self.sm.add_widget(SettingScreen(name='setting'))
        
        return self.sm
    
    def on_start(self):
        print("🌑 NYX v0.2 Ready")
        print("   📱 5 Screens loaded")
        print("   ⚡ Action system ready")
    
    # ─── Navigasi ───────────────────────
    def switch_screen(self, screen_name):
        self.sm.current = screen_name
        self.current_tab = screen_name
    
    def show_toast(self, message):
        """Tampilkan toast/notifikasi"""
        print(f"🔔 {message}")
        # Nanti pakai Android Toast / notifikasi
    
    # ─── Quick Actions ──────────────────
    def alarm(self):
        self.show_toast("⏰ Alarm - Coming Soon")
    
    def timer(self):
        self.show_toast("⏱️ Timer - Coming Soon")
    
    def buka_app(self):
        self.show_toast("📱 Buka App - Coming Soon")
    
    def musik(self):
        self.show_toast("🎵 Musik - Coming Soon")


# ═══════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════

if __name__ == '__main__':
    NyxApp().run()
