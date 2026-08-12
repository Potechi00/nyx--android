"""
🌑 NYX - Personal AI Assistant
Crash-Proof & Seamless Vortex Edition
"""

import kivy
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import (
    Color, Rectangle, Line, RoundedRectangle, 
    PushMatrix, PopMatrix, Rotate, Ellipse,
    StencilPush, StencilUse, StencilUnpush
)
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation

Window.clearcolor = (0, 0, 0, 1)

# Skema Warna Elegan & High Contrast
WHITE_BRIGHT = (1.0, 1.0, 1.0, 1)
WHITE_SOFT   = (0.95, 0.95, 1.0, 0.90)
PURPLE_GLOW  = (0.65, 0.25, 0.98, 1)
GRAY_TEXT    = (0.75, 0.75, 0.85, 0.85)


# ═══════════════════════════════════════════════════════════════════════════
# 🌀 SEAMLESS ROTATING VORTEX (CIRCULAR STENCIL MASK)
# ═══════════════════════════════════════════════════════════════════════════

class RotatingVortex(FloatLayout):
    """Memuat vortex.png & memotong ujung kotaknya menjadi LINGKARAN SEMPURNA"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle = 0

        # ✂️ STENCIL MASKING: Memotong bentuk kotak menjadi lingkaran
        with self.canvas.before:
            StencilPush()
            self.mask = Ellipse(pos=self.pos, size=self.size)
            StencilUse()

        self.vortex_img = Image(
            source='vortex.png',
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        with self.vortex_img.canvas.before:
            PushMatrix()
            self.rot = Rotate(angle=0, axis=(0, 0, 1), origin=self.center)
        with self.vortex_img.canvas.after:
            PopMatrix()

        self.add_widget(self.vortex_img)

        with self.canvas.after:
            StencilUnpush()

        self.bind(pos=self._update_mask, size=self._update_mask)
        Clock.schedule_interval(self._rotate, 1 / 30)

    def _update_mask(self, *args):
        self.mask.pos = self.pos
        self.mask.size = self.size
        self.rot.origin = self.vortex_img.center

    def _rotate(self, dt):
        self.angle = (self.angle + 0.6) % 360
        self.rot.angle = self.angle


# ═══════════════════════════════════════════════════════════════════════════
# 🎨 CANVAS DRAWN ICONS & VOICE FAB
# ═══════════════════════════════════════════════════════════════════════════

class CanvasIcon(Widget):
    """Ikon Vektor Presisi Tinggi"""
    def __init__(self, icon_type="menu", **kwargs):
        super().__init__(**kwargs)
        self.icon_type = icon_type
        self.size_hint = (None, None)
        self.size = (22, 22)
        self.bind(pos=self._draw, size=self._draw)

    def _draw(self, *args):
        self.canvas.clear()
        x, y = self.x, self.y
        w, h = self.width, self.height
        cx, cy = self.center_x, self.center_y

        with self.canvas:
            Color(0.9, 0.9, 1.0, 0.90)
            
            if self.icon_type == "menu":
                Line(points=[x, y + h*0.75, x + w, y + h*0.75], width=2)
                Line(points=[x, y + h*0.50, x + w*0.75, y + h*0.50], width=2)
                Line(points=[x, y + h*0.25, x + w, y + h*0.25], width=2)

            elif self.icon_type == "settings":
                Line(ellipse=(cx - 7, cy - 7, 14, 14), width=1.8)
                Line(ellipse=(cx - 2.5, cy - 2.5, 5, 5), width=1.5)

            elif self.icon_type == "home":
                Line(points=[x + 2, y + h*0.45, cx, y + h*0.85, x + w - 2, y + h*0.45], width=1.8)
                Line(rectangle=(x + 4, y + 2, w - 8, h*0.45), width=1.6)

            elif self.icon_type == "chat":
                Line(rounded_rectangle=(x + 2, y + 4, w - 4, h - 8, 4), width=1.6)
                Line(points=[x + 6, y + 4, x + 2, y], width=1.6)

            elif self.icon_type == "action":
                Line(rectangle=(x + 2, y + h/2 + 1, w/2 - 3, h/2 - 3), width=1.5)
                Line(rectangle=(x + w/2 + 1, y + h/2 + 1, w/2 - 3, h/2 - 3), width=1.5)
                Line(rectangle=(x + 2, y + 2, w/2 - 3, h/2 - 3), width=1.5)
                Line(rectangle=(x + w/2 + 1, y + 2, w/2 - 3, h/2 - 3), width=1.5)

            elif self.icon_type == "history":
                Line(ellipse=(cx - 8, cy - 8, 16, 16), width=1.6)
                Line(points=[cx, cy, cx, cy + 5], width=1.5)
                Line(points=[cx, cy, cx + 4, cy], width=1.5)


class VoiceFAB(Widget):
    """Tombol Mikrofon Ungu Glowing"""
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
            Color(0.5, 0.2, 0.9, 0.35)
            Ellipse(pos=(self.x - 5, self.y - 5), size=(self.width + 10, self.height + 10))

            Color(*PURPLE_GLOW)
            Ellipse(pos=(self.x, self.y), size=self.size)

            Color(1, 1, 1, 0.95)
            heights = [10, 22, 15, 26, 12]
            spacing = 6
            start_x = cx - (len(heights) * spacing) / 2 + 3

            for i, h in enumerate(heights):
                x = start_x + (i * spacing)
                Line(points=[x, cy - h / 2, x, cy + h / 2], width=2.2)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.is_active = not self.is_active
            app = App.get_running_app()
            if self.is_active:
                app.root.handle_voice_start()
            else:
                app.root.handle_voice_stop()
            return True
        return super().on_touch_down(touch)


# ═══════════════════════════════════════════════════════════════════════════
# 🏷️ GLASSMORPHISM COMPONENTS
# ═══════════════════════════════════════════════════════════════════════════

class GlassStatusCard(FloatLayout):
    """Kartu Status Utama Atas"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.85, 0.065)
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.82}
        
        with self.canvas.before:
            Color(0.05, 0.03, 0.12, 0.65)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[16])
            Color(0.45, 0.25, 0.65, 0.35)
            self.border = Line(rounded_rectangle=(self.x, self.y, self.width, self.height, 16), width=1)

        self.bind(pos=self._update_bg, size=self._update_bg)

        self.label = Label(
            text="Siap mendengarkan...",
            font_size='15sp',
            color=WHITE_BRIGHT,
            bold=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(self.label)

    def _update_bg(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.border.rounded_rectangle = (self.x, self.y, self.width, self.height, 16)

    def set_text(self, text):
        self.label.text = text


class SubtitleBox(FloatLayout):
    """Kapsul Subtitle Hint (Aman dari Bug)"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.72, 0.05)
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.31}

        with self.canvas.before:
            Color(0.05, 0.03, 0.12, 0.65)
            self.bg = RoundedRectangle(pos=self.pos, size=self.size, radius=[14])

        self.bind(pos=self._update_bg, size=self._update_bg)

        self.label = Label(
            text='Ucapkan "Nyx" diikuti perintah',
            font_size='12.5sp',
            color=GRAY_TEXT,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(self.label)

    def _update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


class SuggestionChip(Label):
    """Chip Perintah Cepat Kapsul"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = '12.5sp'
        self.color = WHITE_SOFT
        self.size_hint = (1, None)
        self.height = 38
        self.padding = (16, 0)
        self.halign = 'left'
        self.valign = 'middle'
        self.bind(size=self._draw_bg, pos=self._draw_bg)

    def _draw_bg(self, *args):
        self.text_size = (self.width - 32, None)
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.08, 0.06, 0.16, 0.70)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[14])
            Color(0.35, 0.25, 0.50, 0.35)
            Line(rounded_rectangle=(self.x, self.y, self.width, self.height, 14), width=1)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            anim = (Animation(color=PURPLE_GLOW, duration=0.15) + Animation(color=WHITE_SOFT, duration=0.15))
            anim.start(self)
            app = App.get_running_app()
            app.root.handle_command(self.text.replace('"', ''))
            return True
        return super().on_touch_down(touch)


# ═══════════════════════════════════════════════════════════════════════════
# 📱 MAIN SCREEN (NYX UI STABLE)
# ═══════════════════════════════════════════════════════════════════════════

class NyxMainScreen(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._build_ui()

    def _build_ui(self):
        # 1. Background Nebula
        self.bg_image = Image(
            source='nebula01.jpg',
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1.25, 1.25),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(self.bg_image)

        # Animasi Background Floating Lambat
        bg_anim = (
            Animation(pos_hint={'center_x': 0.46, 'center_y': 0.54}, duration=14, t='in_out_sine') +
            Animation(pos_hint={'center_x': 0.54, 'center_y': 0.46}, duration=16, t='in_out_sine') +
            Animation(pos_hint={'center_x': 0.50, 'center_y': 0.50}, duration=14, t='in_out_sine')
        )
        bg_anim.bind(on_complete=lambda *x: bg_anim.start(self.bg_image))
        bg_anim.start(self.bg_image)

        # 2. Header Bar
        header = FloatLayout(size_hint=(1, 0.09), pos_hint={'x': 0, 'top': 1.0})
        
        with header.canvas.before:
            Color(0.02, 0.01, 0.05, 0.80)
            Rectangle(pos=(0, Window.height * 0.91), size=(Window.width, Window.height * 0.09))
            Color(0.4, 0.2, 0.6, 0.25)
            Line(points=[0, Window.height * 0.91, Window.width, Window.height * 0.91], width=1)

        icon_menu = CanvasIcon(icon_type="menu", pos_hint={'x': 0.06, 'center_y': 0.5})
        title = Label(
            text="N Y X",
            font_size='28sp',
            color=WHITE_BRIGHT,
            bold=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        icon_settings = CanvasIcon(icon_type="settings", pos_hint={'right': 0.94, 'center_y': 0.5})

        header.add_widget(icon_menu)
        header.add_widget(title)
        header.add_widget(icon_settings)
        self.add_widget(header)

        # 3. Status Card
        self.status_card = GlassStatusCard()
        self.add_widget(self.status_card)

        # 4. Black Hole Rotating Vortex (Seamless Circular Mask)
        self.vortex = RotatingVortex(
            size_hint=(0.75, 0.38),
            pos_hint={'center_x': 0.5, 'center_y': 0.52}
        )
        self.add_widget(self.vortex)

        # 5. Subtitle Hint
        sub_box = SubtitleBox()
        self.add_widget(sub_box)

        # 6. Suggestion Chips
        chips_box = BoxLayout(
            orientation='vertical',
            spacing=10,
            size_hint=(0.60, 0.14),
            pos_hint={'x': 0.06, 'center_y': 0.20}
        )
        chips_box.add_widget(SuggestionChip(text='"Nyx, timer 10 menit"'))
        chips_box.add_widget(SuggestionChip(text='"Nyx, buka YouTube"'))
        self.add_widget(chips_box)

        # 7. Voice FAB Button
        fab = VoiceFAB(pos_hint={'right': 0.94, 'center_y': 0.20})
        self.add_widget(fab)

        # 8. Navigation Bar Bawah
        nav_bar = FloatLayout(size_hint=(1, 0.09), pos_hint={'x': 0, 'y': 0})
        
        with nav_bar.canvas.before:
            Color(0.03, 0.02, 0.07, 0.92)
            Rectangle(pos=(0, 0), size=(Window.width, Window.height * 0.09))
            Color(0.3, 0.2, 0.5, 0.3)
            Line(points=[0, Window.height * 0.09, Window.width, Window.height * 0.09], width=1)

        nav_box = BoxLayout(orientation='horizontal', size_hint=(1, 1), pos_hint={'x': 0, 'y': 0})
        nav_items = [("home", "Beranda"), ("chat", "Chat"), ("action", "Aksi"), ("history", "Riwayat")]
        
        for icon_name, label_text in nav_items:
            item_box = BoxLayout(orientation='vertical', padding=(0, 6), spacing=2)
            icon_container = FloatLayout(size_hint=(1, 0.55))
            icon_widget = CanvasIcon(icon_type=icon_name, pos_hint={'center_x': 0.5, 'center_y': 0.5})
            icon_container.add_widget(icon_widget)
            
            lbl_txt = Label(text=label_text, font_size='10sp', color=GRAY_TEXT, size_hint=(1, 0.45))
            
            item_box.add_widget(icon_container)
            item_box.add_widget(lbl_txt)
            nav_box.add_widget(item_box)

        nav_bar.add_widget(nav_box)
        self.add_widget(nav_bar)

    # ─── HANDLERS ───
    def handle_command(self, text):
        self.status_card.set_text(f"📩 {text}")

    def handle_voice_start(self):
        self.status_card.set_text("🎤 Mendengarkan...")

    def handle_voice_stop(self):
        self.status_card.set_text("Siap mendengarkan...")


class NyxApp(App):
    def build(self):
        return NyxMainScreen()


if __name__ == '__main__':
    NyxApp().run()
