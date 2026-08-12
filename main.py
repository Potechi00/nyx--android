"""
🌑 NYX V3.0 - Goddess of Night Edition
Dynamic Cosmic Sky, Alive Pulsing Orb & High-End Minimalist Glass UI
100% Pure Code OpenGL Canvas - Zero Static Images
"""

import math
import random
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import (
    Color, Ellipse, Line, PushMatrix, PopMatrix, Rotate, RoundedRectangle
)

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFloatingActionButton, MDIconButton

# Deep Cosmic Space Background
Window.clearcolor = (0.02, 0.01, 0.06, 1)


# ═══════════════════════════════════════════════════════════════════════════
# 🌌 DYNAMIC COSMIC SKY (Langit Malam & Bintang Berkelip)
# ═══════════════════════════════════════════════════════════════════════════

class CosmicSkyBackground(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stars = []
        self.time = 0
        
        # Generate 70 titik bintang acak di langit
        for _ in range(70):
            self.stars.append({
                'x': random.random(),
                'y': random.random(),
                'size': random.uniform(1.2, 3.2),
                'speed': random.uniform(1.5, 4.0),
                'phase': random.uniform(0, 6.28)
            })

        self.bind(pos=self._draw_sky, size=self._draw_sky)
        Clock.schedule_interval(self._animate_sky, 1 / 30)

    def _animate_sky(self, dt):
        self.time += dt
        self._draw_sky()

    def _draw_sky(self, *args):
        self.canvas.before.clear()
        w, h = self.width, self.height
        if w == 0 or h == 0:
            return

        with self.canvas.before:
            # 1. Aura Nebula Kosmik di Tengah
            Color(0.25, 0.08, 0.45, 0.18)
            Ellipse(pos=(w * 0.1, h * 0.25), size=(w * 0.8, h * 0.5))

            Color(0.12, 0.05, 0.35, 0.22)
            Ellipse(pos=(w * 0.2, h * 0.3), size=(w * 0.6, h * 0.4))

            # 2. Bintang-Bintang Berkelip (Twinkling Stars)
            for star in self.stars:
                # Alpha bintang menggunakan gelombang sinus agar berkelip lembut
                alpha = 0.3 + 0.6 * (0.5 + 0.5 * math.sin(self.time * star['speed'] + star['phase']))
                Color(0.9, 0.88, 1.0, alpha)
                sx = star['x'] * w
                sy = star['y'] * h
                sz = star['size']
                Ellipse(pos=(sx, sy), size=(sz, sz))


# ═══════════════════════════════════════════════════════════════════════════
# 🔮 GODDESS ORB (Inti NYX Hidup & Bernafas)
# ═══════════════════════════════════════════════════════════════════════════

class AliveGoddessOrb(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = 0
        self.bind(pos=self._draw_orb, size=self._draw_orb)
        Clock.schedule_interval(self._animate_orb, 1 / 30)

    def _animate_orb(self, dt):
        self.time += dt
        self._draw_orb()

    def _draw_orb(self, *args):
        self.canvas.before.clear()
        
        # Efek melayang (Bobbing motion) pada sumbu Y
        float_offset = math.sin(self.time * 1.8) * 12
        cx, cy = self.center_x, self.center_y + float_offset
        
        if cx == 0 or cy == 0:
            return

        # Denyut nafas (Pulse factor)
        pulse = 1.0 + 0.06 * math.sin(self.time * 2.5)
        
        with self.canvas.before:
            # A. Outer Goddess Halo (Aura Cahaya Luar)
            Color(0.55, 0.15, 0.95, 0.12)
            r_aura1 = 165 * pulse
            Ellipse(pos=(cx - r_aura1, cy - r_aura1), size=(r_aura1 * 2, r_aura1 * 2))

            Color(0.70, 0.25, 1.0, 0.22)
            r_aura2 = 120 * pulse
            Ellipse(pos=(cx - r_aura2, cy - r_aura2), size=(r_aura2 * 2, r_aura2 * 2))

            # B. 3 Cincin Orbit Kosmik Berputar
            # Cincin 1 (Horizontal Rotate)
            PushMatrix()
            Rotate(angle=(self.time * 35) % 360, origin=(cx, cy))
            Color(0.85, 0.5, 1.0, 0.65)
            Line(ellipse=(cx - 100, cy - 32, 200, 64), width=1.8)
            PopMatrix()

            # Cincin 2 (Diagonal Rotate Inverse)
            PushMatrix()
            Rotate(angle=(-self.time * 48) % 360, origin=(cx, cy))
            Color(0.35, 0.75, 1.0, 0.55)
            Line(ellipse=(cx - 40, cy - 100, 80, 200), width=1.5)
            PopMatrix()

            # Cincin 3 (Outer Thin Ring)
            PushMatrix()
            Rotate(angle=(self.time * 20) % 360, origin=(cx, cy))
            Color(0.9, 0.7, 1.0, 0.35)
            Line(ellipse=(cx - 115, cy - 115, 230, 230), width=1.2)
            PopMatrix()

            # C. Inti Orb (Core Energy)
            Color(0.65, 0.2, 0.98, 0.85)
            r_core = 62 * pulse
            Ellipse(pos=(cx - r_core, cy - r_core), size=(r_core * 2, r_core * 2))

            # D. Pure White Glowing Center
            Color(1.0, 0.95, 1.0, 0.98)
            r_center = 24 * pulse
            Ellipse(pos=(cx - r_center, cy - r_center), size=(r_center * 2, r_center * 2))


# ═══════════════════════════════════════════════════════════════════════════
# 📱 MAIN SCREEN UI
# ═══════════════════════════════════════════════════════════════════════════

class NyxMainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._build_ui()

    def _build_ui(self):
        # 1. Background Langit Malam Kosmik
        self.sky_bg = CosmicSkyBackground()
        self.add_widget(self.sky_bg)

        root_layout = MDFloatLayout()

        # ─── 2. HEADER MEGAH (N Y X - Goddess of Night) ───
        header_box = MDBoxLayout(
            orientation='vertical',
            size_hint=(1, 0.12),
            pos_hint={'top': 0.98},
            padding=[16, 0],
            spacing=-2
        )
        
        top_bar = MDBoxLayout(orientation='horizontal', size_hint=(1, 0.7))
        btn_menu = MDIconButton(
            icon="text-alignment-left",
            theme_icon_color="Custom",
            icon_color=(0.85, 0.80, 1.0, 0.9),
            pos_hint={'center_y': 0.5}
        )
        
        # Title Megah NYX
        title_label = MDLabel(
            text="N  Y  X",
            font_style="H4",
            bold=True,
            halign="center",
            theme_text_color="Custom",
            text_color=(1.0, 0.98, 1.0, 0.98),
            pos_hint={'center_y': 0.5}
        )
        
        btn_settings = MDIconButton(
            icon="cog-outline",
            theme_icon_color="Custom",
            icon_color=(0.85, 0.80, 1.0, 0.9),
            pos_hint={'center_y': 0.5}
        )
        
        top_bar.add_widget(btn_menu)
        top_bar.add_widget(title_label)
        top_bar.add_widget(btn_settings)
        
        # Subtitle Elegan
        sub_title = MDLabel(
            text="G O D D E S S   O F   N I G H T",
            font_style="Overline",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.65, 0.55, 0.85, 0.75),
            size_hint=(1, 0.3)
        )

        header_box.add_widget(top_bar)
        header_box.add_widget(sub_title)
        root_layout.add_widget(header_box)

        # ─── 3. STATUS BADGE MINIMALIS (Siap Mendengarkan) ───
        # Dibuat kecil, mungil, dan tidak mencolok
        self.status_card = MDCard(
            size_hint=(0.58, 0.042),
            pos_hint={'center_x': 0.5, 'center_y': 0.82},
            md_bg_color=(0.06, 0.03, 0.15, 0.55),
            line_color=(0.5, 0.3, 0.8, 0.25),
            radius=[20]
        )
        status_box = MDBoxLayout(
            orientation='horizontal',
            padding=[10, 0],
            spacing=6,
            halign="center"
        )
        
        # Dot Indikator Status
        self.dot_card = MDCard(
            size_hint=(None, None),
            size=(8, 8),
            radius=[4],
            md_bg_color=(0.65, 0.25, 0.98, 1),
            pos_hint={'center_y': 0.5}
        )
        
        self.status_label = MDLabel(
            text="Siap mendengarkan...",
            halign="center",
            font_style="Caption",
            theme_text_color="Custom",
            text_color=(0.85, 0.85, 0.95, 0.85),
            pos_hint={'center_y': 0.5}
        )
        
        status_box.add_widget(self.dot_card)
        status_box.add_widget(self.status_label)
        self.status_card.add_widget(status_box)
        root_layout.add_widget(self.status_card)

        # ─── 4. ALIVE GODDESS ORB (Pusat Perhatian) ───
        self.goddess_orb = AliveGoddessOrb(
            size_hint=(0.85, 0.42),
            pos_hint={'center_x': 0.5, 'center_y': 0.51}
        )
        root_layout.add_widget(self.goddess_orb)

        # ─── 5. SUBTITLE HINT ───
        sub_card = MDCard(
            size_hint=(0.68, 0.04),
            pos_hint={'center_x': 0.5, 'center_y': 0.28},
            md_bg_color=(0.05, 0.02, 0.12, 0.45),
            radius=[12]
        )
        sub_hint = MDLabel(
            text='Ucapkan "Nyx" diikuti perintah',
            halign="center",
            font_style="Caption",
            theme_text_color="Custom",
            text_color=(0.6, 0.55, 0.75, 0.7)
        )
        sub_card.add_widget(sub_hint)
        root_layout.add_widget(sub_card)

        # ─── 6. SUGGESTION CHIPS ───
        chips_box = MDBoxLayout(
            orientation='vertical',
            spacing=8,
            size_hint=(0.60, 0.11),
            pos_hint={'x': 0.06, 'center_y': 0.18}
        )
        
        for text in ['"Nyx, timer 10 menit"', '"Nyx, buka YouTube"']:
            chip_card = MDCard(
                size_hint=(1, 0.48),
                md_bg_color=(0.08, 0.05, 0.18, 0.65),
                line_color=(0.4, 0.25, 0.6, 0.25),
                radius=[12],
                padding=[12, 0]
            )
            chip_label = MDLabel(
                text=text,
                font_style="Caption",
                theme_text_color="Custom",
                text_color=(0.85, 0.85, 0.95, 0.8)
            )
            chip_card.add_widget(chip_label)
            chips_box.add_widget(chip_card)

        root_layout.add_widget(chips_box)

        # ─── 7. NEON VOICE FAB BUTTON ───
        self.fab = MDFloatingActionButton(
            icon="microphone",
            pos_hint={'right': 0.94, 'center_y': 0.18},
            md_bg_color=(0.65, 0.25, 0.98, 1),
            icon_color=(1, 1, 1, 1),
            on_release=self._toggle_voice
        )
        self.fab.is_active = False
        root_layout.add_widget(self.fab)

        # ─── 8. NAVIGATION BAR GLASSMORPHISM ───
        nav_bar = MDCard(
            size_hint=(1, 0.08),
            pos_hint={'x': 0, 'y': 0},
            md_bg_color=(0.03, 0.01, 0.08, 0.92),
            line_color=(0.35, 0.2, 0.55, 0.25),
            radius=[0]
        )
        nav_box = MDBoxLayout(orientation='horizontal')
        nav_items = [
            ("home-variant", "Beranda"),
            ("chat-processing-outline", "Chat"),
            ("dots-grid", "Aksi"),
            ("clock-time-four-outline", "Riwayat")
        ]

        for icon_name, label_text in nav_items:
            item_box = MDBoxLayout(orientation='vertical', padding=[0, 3], spacing=-2)
            icon_btn = MDIconButton(
                icon=icon_name,
                theme_icon_color="Custom",
                icon_color=(0.7, 0.65, 0.85, 0.75),
                pos_hint={'center_x': 0.5}
            )
            lbl = MDLabel(
                text=label_text,
                halign="center",
                font_style="Overline",
                theme_text_color="Custom",
                text_color=(0.65, 0.6, 0.8, 0.7)
            )
            item_box.add_widget(icon_btn)
            item_box.add_widget(lbl)
            nav_box.add_widget(item_box)

        nav_bar.add_widget(nav_box)
        root_layout.add_widget(nav_bar)

        self.add_widget(root_layout)

    def _toggle_voice(self, instance):
        self.fab.is_active = not self.fab.is_active
        if self.fab.is_active:
            self.fab.icon = "square"
            self.fab.md_bg_color = (0.9, 0.2, 0.4, 1)
            self.dot_card.md_bg_color = (0.9, 0.2, 0.4, 1)
            self.status_label.text = "Mendengarkan..."
        else:
            self.fab.icon = "microphone"
            self.fab.md_bg_color = (0.65, 0.25, 0.98, 1)
            self.dot_card.md_bg_color = (0.65, 0.25, 0.98, 1)
            self.status_label.text = "Siap mendengarkan..."


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 APP ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════

class NyxApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        return NyxMainScreen()


if __name__ == '__main__':
    NyxApp().run()
