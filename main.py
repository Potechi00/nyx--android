"""
🌑 NYX V2.0 - Personal AI Assistant (Material Design Edition)
100% Pure Code - Zero JPG/PNG Dependencies
"""

import math
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.graphics import Color, Ellipse, Line, PushMatrix, PopMatrix, Rotate

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFloatingActionButton, MDIconButton

Window.clearcolor = (0.04, 0.03, 0.08, 1)  # Deep Midnight Navy Background


# ═══════════════════════════════════════════════════════════════════════════
# 🔮 PROCEDURAL AI GLOW CORE (Vector Dynamic Core - No PNG needed!)
# ═══════════════════════════════════════════════════════════════════════════

class ProceduralAICore(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle_1 = 0
        self.angle_2 = 0
        self.pulse = 1.0
        self.pulse_dir = 1

        self.bind(pos=self._update_canvas, size=self._update_canvas)
        Clock.schedule_interval(self._animate, 1 / 30)

    def _animate(self, dt):
        self.angle_1 = (self.angle_1 + 1.2) % 360
        self.angle_2 = (self.angle_2 - 0.8) % 360
        
        # Animasi Denyut Jantung Core
        self.pulse += 0.008 * self.pulse_dir
        if self.pulse > 1.12 or self.pulse < 0.88:
            self.pulse_dir *= -1

        self._update_canvas()

    def _update_canvas(self, *args):
        self.canvas.before.clear()
        cx, cy = self.center_x, self.center_y
        
        if cx == 0 or cy == 0:
            return

        with self.canvas.before:
            # 1. Outer Glow Aura (Soft Neon Purple)
            Color(0.55, 0.2, 0.95, 0.15)
            r_outer = 140 * self.pulse
            Ellipse(pos=(cx - r_outer, cy - r_outer), size=(r_outer * 2, r_outer * 2))

            Color(0.65, 0.25, 0.98, 0.25)
            r_mid = 100 * self.pulse
            Ellipse(pos=(cx - r_mid, cy - r_mid), size=(r_mid * 2, r_mid * 2))

            # 2. Rotating Orbit Rings
            PushMatrix()
            Rotate(angle=self.angle_1, origin=(cx, cy))
            Color(0.8, 0.4, 1.0, 0.6)
            Line(ellipse=(cx - 85, cy - 30, 170, 60), width=1.8)
            PopMatrix()

            PushMatrix()
            Rotate(angle=self.angle_2, origin=(cx, cy))
            Color(0.4, 0.7, 1.0, 0.5)
            Line(ellipse=(cx - 30, cy - 85, 60, 170), width=1.5)
            PopMatrix()

            # 3. Inner Pulsing Core
            Color(0.75, 0.35, 1.0, 0.85)
            r_core = 55 * self.pulse
            Ellipse(pos=(cx - r_core, cy - r_core), size=(r_core * 2, r_core * 2))

            # 4. Center Bright Star
            Color(1.0, 1.0, 1.0, 0.95)
            r_center = 20 * self.pulse
            Ellipse(pos=(cx - r_center, cy - r_center), size=(r_center * 2, r_center * 2))


# ═══════════════════════════════════════════════════════════════════════════
# 📱 MAIN NYX UI SCREEN
# ═══════════════════════════════════════════════════════════════════════════

class NyxMainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._build_ui()

    def _build_ui(self):
        root_layout = MDFloatLayout()

        # ─── 1. TOP HEADER BAR ───
        header = MDBoxLayout(
            orientation='horizontal',
            size_hint=(1, 0.08),
            pos_hint={'top': 1.0},
            padding=[16, 0]
        )
        btn_menu = MDIconButton(
            icon="menu-open",
            theme_icon_color="Custom",
            icon_color=(0.85, 0.85, 1.0, 0.9),
            pos_hint={'center_y': 0.5}
        )
        title = MDLabel(
            text="N Y X",
            font_style="H5",
            bold=True,
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 0.95),
            pos_hint={'center_y': 0.5}
        )
        btn_settings = MDIconButton(
            icon="cog-outline",
            theme_icon_color="Custom",
            icon_color=(0.85, 0.85, 1.0, 0.9),
            pos_hint={'center_y': 0.5}
        )
        header.add_widget(btn_menu)
        header.add_widget(title)
        header.add_widget(btn_settings)
        root_layout.add_widget(header)

        # ─── 2. GLASS STATUS CARD ───
        self.status_card = MDCard(
            size_hint=(0.88, 0.075),
            pos_hint={'center_x': 0.5, 'center_y': 0.83},
            md_bg_color=(0.08, 0.05, 0.18, 0.75),
            line_color=(0.4, 0.25, 0.65, 0.4),
            radius=[20]
        )
        self.status_label = MDLabel(
            text="Siap mendengarkan...",
            halign="center",
            bold=True,
            theme_text_color="Custom",
            text_color=(0.95, 0.95, 1.0, 0.95)
        )
        self.status_card.add_widget(self.status_label)
        root_layout.add_widget(self.status_card)

        # ─── 3. PROCEDURAL VECTOR AI CORE ───
        self.ai_core = ProceduralAICore(
            size_hint=(0.8, 0.4),
            pos_hint={'center_x': 0.5, 'center_y': 0.52}
        )
        root_layout.add_widget(self.ai_core)

        # ─── 4. SUBTITLE HINT CARD ───
        sub_card = MDCard(
            size_hint=(0.75, 0.05),
            pos_hint={'center_x': 0.5, 'center_y': 0.30},
            md_bg_color=(0.07, 0.04, 0.15, 0.6),
            radius=[14]
        )
        sub_label = MDLabel(
            text='Ucapkan "Nyx" diikuti perintah',
            halign="center",
            font_style="Caption",
            theme_text_color="Custom",
            text_color=(0.7, 0.7, 0.85, 0.8)
        )
        sub_card.add_widget(sub_label)
        root_layout.add_widget(sub_card)

        # ─── 5. SUGGESTION CHIPS ───
        chips_box = MDBoxLayout(
            orientation='vertical',
            spacing=8,
            size_hint=(0.62, 0.12),
            pos_hint={'x': 0.06, 'center_y': 0.19}
        )
        
        for text in ['"Nyx, timer 10 menit"', '"Nyx, buka YouTube"']:
            chip_card = MDCard(
                size_hint=(1, 0.48),
                md_bg_color=(0.1, 0.07, 0.22, 0.8),
                line_color=(0.35, 0.2, 0.55, 0.3),
                radius=[12],
                padding=[12, 0]
            )
            chip_label = MDLabel(
                text=text,
                font_style="Caption",
                theme_text_color="Custom",
                text_color=(0.9, 0.9, 1.0, 0.85)
            )
            chip_card.add_widget(chip_label)
            chips_box.add_widget(chip_card)

        root_layout.add_widget(chips_box)

        # ─── 6. FAB VOICE BUTTON ───
        self.fab = MDFloatingActionButton(
            icon="microphone-variant",
            pos_hint={'right': 0.94, 'center_y': 0.19},
            md_bg_color=(0.65, 0.25, 0.98, 1),
            icon_color=(1, 1, 1, 1),
            on_release=self._toggle_voice
        )
        self.fab.is_active = False
        root_layout.add_widget(self.fab)

        # ─── 7. BOTTOM NAVIGATION BAR ───
        nav_bar = MDCard(
            size_hint=(1, 0.085),
            pos_hint={'x': 0, 'y': 0},
            md_bg_color=(0.05, 0.03, 0.12, 0.95),
            line_color=(0.3, 0.2, 0.5, 0.3),
            radius=[0]
        )
        nav_box = MDBoxLayout(orientation='horizontal')
        nav_items = [
            ("home", "Beranda"),
            ("message-text-outline", "Chat"),
            ("widgets-outline", "Aksi"),
            ("history", "Riwayat")
        ]

        for icon_name, label_text in nav_items:
            item_box = MDBoxLayout(orientation='vertical', padding=[0, 4], spacing=0)
            icon_btn = MDIconButton(
                icon=icon_name,
                theme_icon_color="Custom",
                icon_color=(0.7, 0.7, 0.85, 0.8),
                pos_hint={'center_x': 0.5}
            )
            lbl = MDLabel(
                text=label_text,
                halign="center",
                font_style="Overline",
                theme_text_color="Custom",
                text_color=(0.7, 0.7, 0.85, 0.8)
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
            self.status_label.text = "🎤 Mendengarkan..."
        else:
            self.fab.icon = "microphone-variant"
            self.fab.md_bg_color = (0.65, 0.25, 0.98, 1)
            self.status_label.text = "Siap mendengarkan..."


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 MAIN APP CLASS
# ═══════════════════════════════════════════════════════════════════════════

class NyxApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        return NyxMainScreen()


if __name__ == '__main__':
    NyxApp().run()
