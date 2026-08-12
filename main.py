"""
🌑 NYX — Personal AI Assistant
Cosmic Edition v1.1
Pure Kivy — No External Assets
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

# ═══════════════════════════════════
# THEME
# ═══════════════════════════════════
Window.clearcolor = (0.03, 0.02, 0.06, 1)

SPACE_DARK  = (0.03, 0.02, 0.06, 1)
PURPLE_GLOW = (0.55, 0.2, 0.95, 1)
BLUE_NEBULA = (0.2, 0.1, 0.4, 1)
WHITE_SOFT  = (0.9, 0.9, 0.95, 1)
GRAY_DIM    = (0.5, 0.5, 0.65, 1)


# ═══════════════════════════════════
# COSMIC VORTEX (BLACK HOLE)
# ═══════════════════════════════════

class CosmicVortex(Widget):
    """Pusaran black hole animasi dengan partikel"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle = 0
        self.particles = []
        self._init_particles()
        self.bind(pos=self.draw_vortex, size=self.draw_vortex)
        Clock.schedule_interval(self.animate, 1 / 30)

    def _init_particles(self):
        for _ in range(20):
            self.particles.append({
                'angle': _ * 18,
                'radius': 0,
                'speed': 0.5 + (_ * 0.1),
                'alpha': 0.3 + (_ * 0.03),
                'size': 2 + (_ % 3),
            })

    def animate(self, dt):
        self.angle = (self.angle + 1.5) % 360
        
        # Update partikel
        for p in self.particles:
            p['radius'] = (p['radius'] + p['speed']) % 60
            p['angle'] = (p['angle'] + p['speed'] * 2) % 360

        self.draw_vortex()

    def draw_vortex(self, *args):
        self.canvas.clear()
        cx, cy = self.center_x, self.center_y
        max_r = min(self.width, self.height) / 2

        with self.canvas:
            # 1. Glow nebula luar
            for i in range(12, 0, -1):
                r = max_r * (i / 12.0)
                if i > 8:
                    Color(0.2, 0.1, 0.4, 0.06)
                elif i > 4:
                    Color(0.6, 0.2, 0.7, 0.10)
                else:
                    Color(0.4, 0.2, 0.9, 0.20)
                Ellipse(pos=(cx - r, cy - r), size=(r * 2, r * 2))

            # 2. Partikel berputar
            for p in self.particles:
                rad = math.radians(p['angle'])
                px = cx + p['radius'] * math.cos(rad) - p['size'] / 2
                py = cy + p['radius'] * math.sin(rad) - p['size'] / 2
                Color(0.7, 0.4, 1, p['alpha'])
                Ellipse(pos=(px, py), size=(p['size'], p['size']))

            # 3. Cincin spiral
            Color(0.8, 0.4, 1.0, 0.35)
            for ring in range(3):
                r_ring = (max_r * 0.35) + (ring * 14)
                Line(
                    ellipse=(cx - r_ring, cy - r_ring, r_ring * 2, r_ring * 2),
                    width=1.5,
                    angle_start=self.angle + (ring * 40),
                    angle_end=self.angle + 280 + (ring * 40)
                )

            # 4. Inti black hole
            core_r = max_r * 0.32
            Color(0.01, 0.01, 0.03, 1)
            Ellipse(pos=(cx - core_r, cy - core_r), size=(core_r * 2, core_r * 2))

            # 5. Pinggiran accretion disk
            Color(0.9, 0.3, 0.8, 0.7)
            Line(
                ellipse=(cx - core_r, cy - core_r, core_r * 2, core_r * 2),
                width=2
            )


# ═══════════════════════════════════
# SUGGESTION CHIP
# ═══════════════════════════════════

class SuggestionChip(Label):
    """Chip kapsul perintah"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = '13sp'
        self.color = WHITE_SOFT
        self.size_hint = (1, None)
        self.height = 44
        self.padding = (18, 0)
        self.halign = 'left'
        self.valign = 'middle'
        self.bind(size=self._draw_bg, pos=self._draw_bg)
        self._draw_bg()

    def _draw_bg(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.1, 0.1, 0.16, 0.8)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[22])
            Color(0.25, 0.25, 0.35, 0.4)
            Line(
                rounded_rectangle=(self.x, self.y, self.width, self.height, 22),
                width=1
            )

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            # Animasi klik
            anim = (
                Animation(color=(0.55, 0.2, 0.95, 1), duration=0.15)
                + Animation(color=WHITE_SOFT, duration=0.15)
            )
            anim.start(self)
            
            app = App.get_running_app()
            app.root.handle_command(self.text.replace('"', ''))
            return True
        return super().on_touch_down(touch)


# ═══════════════════════════════════
# VOICE FAB
# ═══════════════════════════════════

class VoiceFAB(Widget):
    """Tombol suara dengan waveform"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (68, 68)
        self.is_active = False
        self.bind(pos=self._draw, size=self._draw)

    def _draw(self, *args):
        self.canvas.clear()
        cx, cy = self.center_x, self.center_y

        with self.canvas:
            # Glow luar
            if self.is_active:
                Color(0.3, 0.9, 0.4, 0.3)
                Ellipse(pos=(self.x - 8, self.y - 8), size=(self.width + 16, self.height + 16))

            # Lingkaran ungu
            Color(*PURPLE_GLOW)
            Ellipse(pos=(self.x, self.y), size=self.size)

            # Waveform icon
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


# ═══════════════════════════════════
# NAVIGATION BAR
# ═══════════════════════════════════

class NavBar(FloatLayout):
    """Bottom navigation bar"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 0.09)
        self.pos_hint = {'x': 0, 'y': 0}
        self.bind(pos=self._draw_bg, size=self._draw_bg)
        self._build_items()

    def _draw_bg(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.04, 0.03, 0.07, 0.95)
            Rectangle(pos=self.pos, size=self.size)
            Color(0.2, 0.2, 0.3, 0.3)
            Line(points=[self.x, self.y + self.height, self.x + self.width, self.y + self.height], width=1)

    def _build_items(self):
        items = [
            ("🏠", "Beranda"),
            ("💬", "Chat"),
            ("⚡", "Aksi"),
            ("📜", "Riwayat"),
        ]

        nav_box = BoxLayout(orientation='horizontal', size_hint=(1, 1))
        
        for icon, label in items:
            item_box = BoxLayout(orientation='vertical', padding=(0, 6))
            lbl_icon = Label(text=icon, font_size='18sp', color=(0.7, 0.7, 0.85, 1))
            lbl_txt = Label(text=label, font_size='10sp', color=GRAY_DIM)
            item_box.add_widget(lbl_icon)
            item_box.add_widget(lbl_txt)
            nav_box.add_widget(item_box)

        self.add_widget(nav_box)


# ═══════════════════════════════════
# STATUS LABEL (dengan animasi ketik)
# ═══════════════════════════════════

class StatusLabel(Label):
    """Status dengan animasi ketik"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = '18sp'
        self.color = WHITE_SOFT
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.83}
        self.size_hint = (0.85, 0.06)

    def set_text(self, text, animate=True):
        if animate:
            self.text = ''
            self._type_text(text)
        else:
            self.text = text

    def _type_text(self, text, index=0):
        if index < len(text):
            self.text += text[index]
            Clock.schedule_once(lambda dt: self._type_text(text, index + 1), 0.03)


# ═══════════════════════════════════
# MAIN SCREEN
# ═══════════════════════════════════

class NyxMainScreen(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._build_ui()
        self._animate_in()

    def _build_ui(self):
        # Header
        self.header = FloatLayout(size_hint=(1, 0.08), pos_hint={'x': 0, 'top': 0.98})

        btn_menu = Label(
            text="☰", font_size='22sp', color=(0.8, 0.8, 0.9, 1),
            size_hint=(None, None), size=(44, 44),
            pos_hint={'x': 0.03, 'center_y': 0.5}
        )
        title = Label(
            text="N Y X", font_size='18sp', color=(1, 1, 1, 1), bold=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        btn_settings = Label(
            text="⚙", font_size='22sp', color=(0.8, 0.8, 0.9, 1),
            size_hint=(None, None), size=(44, 44),
            pos_hint={'right': 0.97, 'center_y': 0.5}
        )

        self.header.add_widget(btn_menu)
        self.header.add_widget(title)
        self.header.add_widget(btn_settings)
        self.add_widget(self.header)

        # Status
        self.status_label = StatusLabel()
        self.add_widget(self.status_label)

        # Cosmic Vortex
        self.vortex = CosmicVortex(
            size_hint=(0.75, 0.38),
            pos_hint={'center_x': 0.5, 'center_y': 0.55}
        )
        self.add_widget(self.vortex)

        # Subtitle
        self.sub_label = Label(
            text='Ucapkan "Nyx" diikuti perintah',
            font_size='13sp',
            color=GRAY_DIM,
            pos_hint={'center_x': 0.5, 'center_y': 0.33}
        )
        self.add_widget(self.sub_label)

        # Suggestion Chips
        self.chips_container = BoxLayout(
            orientation='vertical',
            spacing=10,
            size_hint=(0.62, 0.15),
            pos_hint={'x': 0.05, 'center_y': 0.21}
        )
        self.chips_container.add_widget(SuggestionChip(text='"Nyx, timer 10 menit"'))
        self.chips_container.add_widget(SuggestionChip(text='"Nyx, buka YouTube"'))
        self.add_widget(self.chips_container)

        # Voice FAB
        self.voice_fab = VoiceFAB(
            pos_hint={'right': 0.93, 'center_y': 0.21}
        )
        self.add_widget(self.voice_fab)

        # Navbar
        self.navbar = NavBar()
        self.add_widget(self.navbar)

    def _animate_in(self):
        """Animasi awal"""
        # Status label animasi ketik
        Clock.schedule_once(
            lambda dt: self.status_label.set_text("Siap mendengarkan..."), 0.3
        )

    # ─── HANDLERS ─────────────────

    def handle_command(self, text):
        """Handle perintah dari chip atau input"""
        self.status_label.set_text(f"📩 {text}", animate=True)
        
        # Simulasi respon
        Clock.schedule_once(
            lambda dt: self.status_label.set_text("⚡ Memproses..."), 1.5
        )
        Clock.schedule_once(
            lambda dt: self.status_label.set_text("✅ Selesai!", animate=True), 2.5
        )

    def handle_voice_start(self):
        """Mulai voice recording"""
        self.status_label.set_text("🎤 Mendengarkan...", animate=False)
        Clock.schedule_once(
            lambda dt: self.status_label.set_text("🔊 Suara diterima!", animate=True), 2
        )

    def handle_voice_stop(self):
        """Stop voice"""
        self.status_label.set_text("Siap mendengarkan...", animate=False)


# ═══════════════════════════════════
# APP
# ═══════════════════════════════════

class NyxApp(App):
    def build(self):
        return NyxMainScreen()


if __name__ == '__main__':
    NyxApp().run()
