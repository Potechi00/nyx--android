"""
🌑 NYX - Personal AI Assistant
Cosmic Edition v1.2 (Fix Tofu Icons & Added Starfield Background)
Pure Kivy Canvas — No External Assets
"""

import kivy
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, RoundedRectangle, Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation
import math
import random

Window.clearcolor = (0.02, 0.01, 0.05, 1)

WHITE_SOFT  = (0.92, 0.92, 0.98, 1)
PURPLE_GLOW = (0.60, 0.25, 0.98, 1)
GRAY_DIM    = (0.50, 0.50, 0.65, 1)


# ═══════════════════════════════════════════════════════════════════════════
# 🌌 STARFIELD & NEBULA BACKGROUND (Canvas Pure)
# ═══════════════════════════════════════════════════════════════════════════

class StarfieldBackground(Widget):
    """Latar belakang ruang angkasa dengan bintang dan nebula"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stars = []
        self._generate_stars()
        self.bind(pos=self._draw, size=self._draw)
        Clock.schedule_interval(self._twinkle, 1 / 15)

    def _generate_stars(self):
        # Generate 120 bintang acak
        for _ in range(120):
            self.stars.append({
                'x': random.random(),
                'y': random.random(),
                'size': random.uniform(1.0, 2.8),
                'alpha': random.uniform(0.2, 0.9),
                'speed': random.uniform(-0.03, 0.03)
            })

    def _twinkle(self, dt):
        for s in self.stars:
            s['alpha'] = max(0.1, min(1.0, s['alpha'] + s['speed']))
            if s['alpha'] >= 1.0 or s['alpha'] <= 0.1:
                s['speed'] = -s['speed']
        self._draw()

    def _draw(self, *args):
        self.canvas.clear()
        w, h = self.width, self.height

        with self.canvas:
            # 1. Base Dark Background
            Color(0.02, 0.01, 0.05, 1)
            Rectangle(pos=self.pos, size=self.size)

            # 2. Glowing Nebula Soft Gradients
            Color(0.25, 0.08, 0.38, 0.18)
            Ellipse(pos=(w * 0.1, h * 0.4), size=(w * 0.8, h * 0.5))
            Color(0.08, 0.12, 0.35, 0.15)
            Ellipse(pos=(w * 0.2, h * 0.1), size=(w * 0.7, h * 0.4))

            # 3. Draw Stars
            for s in self.stars:
                Color(0.9, 0.9, 1.0, s['alpha'])
                Ellipse(pos=(self.x + s['x'] * w, self.y + s['y'] * h),
                        size=(s['size'], s['size']))


# ═══════════════════════════════════════════════════════════════════════════
# 🌀 COSMIC VORTEX (BLACK HOLE)
# ═══════════════════════════════════════════════════════════════════════════

class CosmicVortex(Widget):
    """Pusaran black hole animasi"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle = 0
        self.bind(pos=self.draw_vortex, size=self.draw_vortex)
        Clock.schedule_interval(self.animate, 1 / 30)

    def animate(self, dt):
        self.angle = (self.angle + 1.8) % 360
        self.draw_vortex()

    def draw_vortex(self, *args):
        self.canvas.clear()
        cx, cy = self.center_x, self.center_y
        max_r = min(self.width, self.height) / 2

        with self.canvas:
            # Glow Aura Luar
            for i in range(10, 0, -1):
                r = max_r * (i / 10.0)
                if i > 6:
                    Color(0.25, 0.08, 0.45, 0.08)
                elif i > 3:
                    Color(0.65, 0.18, 0.75, 0.12)
                else:
                    Color(0.45, 0.25, 0.95, 0.22)
                Ellipse(pos=(cx - r, cy - r), size=(r * 2, r * 2))

            # Cincin Spiral Berputar
            Color(0.85, 0.35, 1.0, 0.45)
            for ring in range(4):
                r_ring = (max_r * 0.32) + (ring * 12)
                Line(
                    ellipse=(cx - r_ring, cy - r_ring, r_ring * 2, r_ring * 2),
                    width=1.6,
                    angle_start=self.angle + (ring * 45),
                    angle_end=self.angle + 270 + (ring * 45)
                )

            # Inti Black Hole (Hitam Pekat)
            core_r = max_r * 0.32
            Color(0.01, 0.01, 0.03, 1)
            Ellipse(pos=(cx - core_r, cy - core_r), size=(core_r * 2, core_r * 2))

            # Cincin Terang Inti
            Color(0.95, 0.25, 0.85, 0.85)
            Line(ellipse=(cx - core_r, cy - core_r, core_r * 2, core_r * 2), width=2.2)


# ═══════════════════════════════════════════════════════════════════════════
# 🎨 CANVAS DRAWN ICONS (Bebas Tofu 100%)
# ═══════════════════════════════════════════════════════════════════════════

class CanvasIcon(Widget):
    """Widget Khusus untuk menggambar ikon pakai Canvas agar tidak pernah Tofu"""
    def __init__(self, icon_type="menu", **kwargs):
        super().__init__(**kwargs)
        self.icon_type = icon_type
        self.size_hint = (None, None)
        self.size = (24, 24)
        self.bind(pos=self._draw, size=self._draw)

    def _draw(self, *args):
        self.canvas.clear()
        x, y = self.x, self.y
        w, h = self.width, self.height
        cx, cy = self.center_x, self.center_y

        with self.canvas:
            Color(0.8, 0.8, 0.95, 1)
            
            if self.icon_type == "menu":
                # 3 Garis Hamburger
                Line(points=[x, y + h*0.75, x + w, y + h*0.75], width=1.8)
                Line(points=[x, y + h*0.50, x + w, y + h*0.50], width=1.8)
                Line(points=[x, y + h*0.25, x + w, y + h*0.25], width=1.8)

            elif self.icon_type == "settings":
                # Gear / Pengaturan
                Line(ellipse=(cx - 7, cy - 7, 14, 14), width=1.8)
                Line(ellipse=(cx - 2, cy - 2, 4, 4), width=1.5)

            elif self.icon_type == "home":
                # Atap & Rumah
                Line(points=[x + 2, y + h*0.45, cx, y + h*0.85, x + w - 2, y + h*0.45], width=1.6)
                Line(rectangle=(x + 5, y + 2, w - 10, h*0.45), width=1.6)

            elif self.icon_type == "chat":
                # Gelembung Pesan
                Line(rounded_rectangle=(x + 2, y + 4, w - 4, h - 8, 5), width=1.6)
                Line(points=[x + 6, y + 4, x + 2, y], width=1.6)

            elif self.icon_type == "action":
                # Grid 4 Kotak
                Line(rectangle=(x + 2, y + h/2 + 1, w/2 - 3, h/2 - 3), width=1.5)
                Line(rectangle=(x + w/2 + 1, y + h/2 + 1, w/2 - 3, h/2 - 3), width=1.5)
                Line(rectangle=(x + 2, y + 2, w/2 - 3, h/2 - 3), width=1.5)
                Line(rectangle=(x + w/2 + 1, y + 2, w/2 - 3, h/2 - 3), width=1.5)

            elif self.icon_type == "history":
                # Jam / Riwayat
                Line(ellipse=(cx - 8, cy - 8, 16, 16), width=1.6)
                Line(points=[cx, cy, cx, cy + 5], width=1.5)
                Line(points=[cx, cy, cx + 4, cy], width=1.5)


# ═══════════════════════════════════════════════════════════════════════════
# 🏷️ SUGGESTION CHIP & FAB
# ═══════════════════════════════════════════════════════════════════════════

class SuggestionChip(Label):
    """Chip kapsul perintah"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = '13sp'
        self.color = WHITE_SOFT
        self.size_hint = (1, None)
        self.height = 42
        self.padding = (16, 0)
        self.halign = 'left'
        self.valign = 'middle'
        self.bind(size=self._draw_bg, pos=self._draw_bg)

    def _draw_bg(self, *args):
        self.text_size = (self.width - 32, None)
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.10, 0.08, 0.18, 0.85)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[21])
            Color(0.30, 0.25, 0.45, 0.5)
            Line(rounded_rectangle=(self.x, self.y, self.width, self.height, 21), width=1)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            anim = (Animation(color=PURPLE_GLOW, duration=0.15) + Animation(color=WHITE_SOFT, duration=0.15))
            anim.start(self)
            app = App.get_running_app()
            app.root.handle_command(self.text.replace('"', ''))
            return True
        return super().on_touch_down(touch)


class VoiceFAB(Widget):
    """Tombol suara dengan waveform"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (64, 64)
        self.is_active = False
        self.bind(pos=self._draw, size=self._draw)

    def _draw(self, *args):
        self.canvas.clear()
        cx, cy = self.center_x, self.center_y

        with self.canvas:
            if self.is_active:
                Color(0.3, 0.9, 0.4, 0.3)
                Ellipse(pos=(self.x - 6, self.y - 6), size=(self.width + 12, self.height + 12))

            Color(*PURPLE_GLOW)
            Ellipse(pos=(self.x, self.y), size=self.size)

            Color(1, 1, 1, 0.95)
            heights = [10, 20, 14, 24, 12]
            spacing = 6
            start_x = cx - (len(heights) * spacing) / 2 + 3

            for i, h in enumerate(heights):
                x = start_x + (i * spacing)
                Line(points=[x, cy - h / 2, x, cy + h / 2], width=2.2)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.is_active = not self.is_active
            self._draw()
            app = App.get_running_app()
            if self.is_active:
                app.root.handle_voice_start()
            else:
                app.root.handle_voice_stop()
            return True
        return super().on_touch_down(touch)


# ═══════════════════════════════════════════════════════════════════════════
# 📱 LAYAR UTAMA (NYX UI)
# ═══════════════════════════════════════════════════════════════════════════

class NyxMainScreen(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._build_ui()

    def _build_ui(self):
        # 1. Starfield Background
        self.bg = StarfieldBackground(size_hint=(1, 1), pos_hint={'x': 0, 'y': 0})
        self.add_widget(self.bg)

        # 2. Header
        header = FloatLayout(size_hint=(1, 0.08), pos_hint={'x': 0, 'top': 0.98})
        
        icon_menu = CanvasIcon(icon_type="menu", pos_hint={'x': 0.05, 'center_y': 0.5})
        title = Label(text="N Y X", font_size='18sp', color=(1, 1, 1, 1), bold=True,
                      pos_hint={'center_x': 0.5, 'center_y': 0.5})
        icon_settings = CanvasIcon(icon_type="settings", pos_hint={'right': 0.95, 'center_y': 0.5})

        header.add_widget(icon_menu)
        header.add_widget(title)
        header.add_widget(icon_settings)
        self.add_widget(header)

        # 3. Status Label
        self.status_label = Label(text="Siap mendengarkan...", font_size='18sp', color=WHITE_SOFT,
                                  pos_hint={'center_x': 0.5, 'center_y': 0.83})
        self.add_widget(self.status_label)

        # 4. Vortex Black Hole
        vortex = CosmicVortex(size_hint=(0.75, 0.38), pos_hint={'center_x': 0.5, 'center_y': 0.55})
        self.add_widget(vortex)

        # 5. Subtitle
        sub_label = Label(text='Ucapkan "Nyx" diikuti perintah', font_size='13sp', color=GRAY_DIM,
                          pos_hint={'center_x': 0.5, 'center_y': 0.33})
        self.add_widget(sub_label)

        # 6. Suggestion Chips Container
        chips_box = BoxLayout(orientation='vertical', spacing=10, size_hint=(0.62, 0.15),
                              pos_hint={'x': 0.05, 'center_y': 0.21})
        chips_box.add_widget(SuggestionChip(text='"Nyx, timer 10 menit"'))
        chips_box.add_widget(SuggestionChip(text='"Nyx, buka YouTube"'))
        self.add_widget(chips_box)

        # 7. Voice FAB
        fab = VoiceFAB(pos_hint={'right': 0.93, 'center_y': 0.21})
        self.add_widget(fab)

        # 8. Navigation Bar Bawah (Canvas Icons)
        nav_bar = FloatLayout(size_hint=(1, 0.09), pos_hint={'x': 0, 'y': 0})
        
        with nav_bar.canvas.before:
            Color(0.03, 0.02, 0.06, 0.95)
            Rectangle(pos=(0, 0), size=(Window.width, Window.height * 0.09))
            Color(0.2, 0.2, 0.3, 0.3)
            Line(points=[0, Window.height * 0.09, Window.width, Window.height * 0.09], width=1)

        nav_box = BoxLayout(orientation='horizontal', size_hint=(1, 1), pos_hint={'x': 0, 'y': 0})
        nav_items = [("home", "Beranda"), ("chat", "Chat"), ("action", "Aksi"), ("history", "Riwayat")]
        
        for icon_name, label_text in nav_items:
            item_box = BoxLayout(orientation='vertical', padding=(0, 4), spacing=2)
            
            # Container untuk menengahkan Canvas Icon
            icon_container = FloatLayout(size_hint=(1, 0.6))
            icon_widget = CanvasIcon(icon_type=icon_name, pos_hint={'center_x': 0.5, 'center_y': 0.5})
            icon_container.add_widget(icon_widget)
            
            lbl_txt = Label(text=label_text, font_size='10sp', color=GRAY_DIM, size_hint=(1, 0.4))
            
            item_box.add_widget(icon_container)
            item_box.add_widget(lbl_txt)
            nav_box.add_widget(item_box)

        nav_bar.add_widget(nav_box)
        self.add_widget(nav_bar)

    # ─── HANDLERS ───
    def handle_command(self, text):
        self.status_label.text = f"📩 {text}"

    def handle_voice_start(self):
        self.status_label.text = "🎤 Mendengarkan..."

    def handle_voice_stop(self):
        self.status_label.text = "Siap mendengarkan..."


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 APP ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════

class NyxApp(App):
    def build(self):
        return NyxMainScreen()


if __name__ == '__main__':
    NyxApp().run()
