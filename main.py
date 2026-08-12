"""
🌑 NYX - Conversational UI
v1.0 - Estetika Maksimal
"""

import kivy
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Line
from kivy.properties import StringProperty, ListProperty, NumericProperty
import random

Window.clearcolor = (0.02, 0.02, 0.04, 1)

# ═══════════════════════════════════
# PARTICLE ORB
# ═══════════════════════════════════

class ParticleOrb(Widget):
    """Orb dengan partikel berputar"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (160, 160)
        self.particles = []
        self.angle = 0
        self._create_particles()
        Clock.schedule_interval(self.update, 1/60)
    
    def _create_particles(self):
        for _ in range(12):
            self.particles.append({
                'angle': random.uniform(0, 360),
                'radius': random.uniform(55, 75),
                'size': random.uniform(2, 5),
                'speed': random.uniform(0.3, 0.8),
                'alpha': random.uniform(0.2, 0.6),
            })
    
    def update(self, dt):
        self.angle += 0.5
        self.canvas.clear()
        
        cx, cy = self.width/2, self.height/2
        
        with self.canvas:
            # Outer glow
            Color(0.3, 0.5, 0.9, 0.05)
            Ellipse(pos=(cx-75, cy-75), size=(150, 150))
            
            # Middle glow
            Color(0.3, 0.5, 0.9, 0.12)
            Ellipse(pos=(cx-55, cy-55), size=(110, 110))
            
            # Inner
            Color(0.3, 0.5, 0.9, 0.25)
            Ellipse(pos=(cx-35, cy-35), size=(70, 70))
            
            # Core
            Color(0.4, 0.6, 1, 0.5)
            Ellipse(pos=(cx-15, cy-15), size=(30, 30))
            
            # Partikel
            for p in self.particles:
                rad = (self.angle * p['speed'] + p['angle']) * 3.14 / 180
                px = cx + p['radius'] * (rad % 6.28 - 3.14) * 0.1 - p['size']/2
                py = cy + p['radius'] * (rad % 6.28 - 3.14) * 0.1 - p['size']/2
                
                Color(0.4, 0.6, 1, p['alpha'])
                Ellipse(pos=(px, py), size=(p['size'], p['size']))


# ═══════════════════════════════════
# FLOATING INPUT
# ═══════════════════════════════════

class FloatingInput(TextInput):
    """Input bar mengambang dengan glow"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.85, None)
        self.height = 52
        self.multiline = False
        self.background_normal = ''
        self.background_color = (0.06, 0.06, 0.1, 1)
        self.foreground_color = (0.9, 0.9, 1, 1)
        self.hint_text = '💬  Ketik atau ucapkan...'
        self.hint_text_color = (0.3, 0.3, 0.5, 1)
        self.font_size = '15sp'
        self.padding = [20, 14]
        self.cursor_color = (0.4, 0.6, 1, 1)
        
        with self.canvas.before:
            Color(0.3, 0.5, 0.9, 0.15)
            self.glow_rect = Line(
                rounded_rectangle=(self.x-2, self.y-2, self.width+4, self.height+4, 26),
                width=2
            )
        self.bind(pos=self._update_glow, size=self._update_glow)
    
    def _update_glow(self, *args):
        self.glow_rect.rounded_rectangle = (
            self.x-2, self.y-2, self.width+4, self.height+4, 26
        )


# ═══════════════════════════════════
# GLOW BUTTON
# ═══════════════════════════════════

class GlowButton(Button):
    """Tombol minimal dengan glow"""
    
    def __init__(self, icon='', label='', **kwargs):
        super().__init__(**kwargs)
        self.text = f'{icon}\n{label}'
        self.background_normal = ''
        self.background_color = (0.06, 0.06, 0.1, 1)
        self.color = (0.7, 0.7, 0.9, 1)
        self.font_size = '11sp'
        self.size_hint = (None, None)
        self.size = (90, 70)
        self.halign = 'center'
        self.valign = 'middle'
        
        with self.canvas.before:
            Color(0.3, 0.5, 0.9, 0.1)
            self.glow = Line(
                rounded_rectangle=(self.x, self.y, self.width, self.height, 18),
                width=1
            )
        self.bind(pos=self._update_glow, size=self._update_glow)
    
    def _update_glow(self, *args):
        self.glow.rounded_rectangle = (
            self.x, self.y, self.width, self.height, 18
        )
    
    def on_press(self):
        Animation(background_color=(0.1, 0.1, 0.2, 1), duration=0.1).start(self)
    
    def on_release(self):
        Animation(background_color=(0.06, 0.06, 0.1, 1), duration=0.2).start(self)


# ═══════════════════════════════════
# MAIN SCREEN
# ═══════════════════════════════════

class NyxMainScreen(FloatLayout):
    """Screen utama — Conversational UI"""
    
    status_text = StringProperty("Halo, aku Nyx ✨")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._build_ui()
        self._animate_in()
    
    def _build_ui(self):
        # Orb
        self.orb = ParticleOrb(
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        self.add_widget(self.orb)
        
        # Status text
        self.status_label = Label(
            text=self.status_text,
            font_size='18sp',
            color=(0.5, 0.6, 0.9, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.35},
            size_hint=(0.8, 0.08),
            opacity=0
        )
        self.add_widget(self.status_label)
        
        # Subtitle
        self.subtitle = Label(
            text='Ketik atau ucapkan perintah',
            font_size='12sp',
            color=(0.3, 0.3, 0.5, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            size_hint=(0.8, 0.05),
            opacity=0
        )
        self.add_widget(self.subtitle)
        
        # Input bar
        self.input_bar = FloatingInput(
            pos_hint={'center_x': 0.5, 'center_y': 0.18}
        )
        self.input_bar.bind(on_text_validate=self._on_input)
        self.add_widget(self.input_bar)
        
        # Quick buttons
        self.btn_timer = GlowButton(
            icon='⏰', label='Timer',
            pos_hint={'center_x': 0.35, 'center_y': 0.07}
        )
        self.btn_timer.bind(on_press=lambda x: self._on_action('timer'))
        self.add_widget(self.btn_timer)
        
        self.btn_music = GlowButton(
            icon='🎵', label='Musik',
            pos_hint={'center_x': 0.65, 'center_y': 0.07}
        )
        self.btn_music.bind(on_press=lambda x: self._on_action('musik'))
        self.add_widget(self.btn_music)
    
    def _animate_in(self):
        """Animasi masuk"""
        # Status fade in
        anim1 = Animation(opacity=1, duration=0.8)
        Clock.schedule_once(lambda dt: anim1.start(self.status_label), 0.3)
        Clock.schedule_once(lambda dt: anim1.start(self.subtitle), 0.6)
        
        # Input slide up
        self.input_bar.opacity = 0
        self.input_bar.pos_hint = {'center_x': 0.5, 'center_y': 0.1}
        anim2 = Animation(opacity=1, duration=0.6) + Animation(
            pos_hint={'center_x': 0.5, 'center_y': 0.18}, duration=0.4
        )
        Clock.schedule_once(lambda dt: anim2.start(self.input_bar), 0.8)
        
        # Buttons fade in
        self.btn_timer.opacity = 0
        self.btn_music.opacity = 0
        Clock.schedule_once(lambda dt: Animation(opacity=1, duration=0.4).start(self.btn_timer), 1.0)
        Clock.schedule_once(lambda dt: Animation(opacity=1, duration=0.4).start(self.btn_music), 1.2)
    
    def _on_input(self, instance):
        text = instance.text.strip()
        if text:
            self._type_text(f"📩 {text}")
            instance.text = ''
    
    def _on_action(self, action):
        messages = {
            'timer': '⏰ Timer dimulai',
            'musik': '🎵 Memutar musik',
        }
        self._type_text(messages.get(action, f'⚡ {action}'))
    
    def _type_text(self, text):
        """Animasi ketik"""
        self.status_label.text = ''
        self.status_label.opacity = 1
        
        def add_char(i):
            if i < len(text):
                self.status_label.text += text[i]
                Clock.schedule_once(lambda dt: add_char(i+1), 0.04)
        
        add_char(0)


# ═══════════════════════════════════
# APP
# ═══════════════════════════════════

class NyxApp(App):
    
    def build(self):
        return NyxMainScreen()
    
    def on_start(self):
        print("🌑 NYX v1.0 — Conversational UI Ready")


if __name__ == '__main__':
    NyxApp().run()
