"""
SRIJAL AI - MASTER PRO v4.0
(Optimized for Android Build)
"""

import re
import random
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.metrics import dp, sp
from kivy.graphics import Color, RoundedRectangle

Window.clearcolor = (0.95, 0.95, 0.97, 1) # हल्का बैकग्राउंड

# ═══════════════════════════════════════════════════════════════
#  NLP ENGINE - सृजल AI भाषा इंजन
# ═══════════════════════════════════════════════════════════════

class NLPEngine:
    def __init__(self):
        self.intents = {
            'greeting': {
                'patterns': ['namaste', 'hello', 'hi', 'hey', 'kaise ho', 'नमस्ते', 'हैलो'],
                'responses': [
                    'नमस्ते सूर्यांश! मैं सृजल हूँ। आज आपकी कैसे मदद कर सकती हूँ?',
                    'Namaste! Main Srijal hoon. Boliye, kya sahayata karoon?'
                ]
            },
            'farewell': {
                'patterns': ['bye', 'goodbye', 'alvida', 'phir milenge', 'अलविदा'],
                'responses': [
                    'अलविदा! फिर मिलेंगे। अपना ध्यान रखें!',
                    'Bye! Phir milte hain. Have a great day!'
                ]
            },
            'identity': {
                'patterns': ['tum kaun ho', 'who are you', 'naam kya hai', 'नाम'],
                'responses': [
                    'मेरा नाम सृजल है। मैं आपकी अपनी पर्सनल एआई असिस्टेंट हूँ।',
                    'Main Srijal hoon, aapki AI assistant!'
                ]
            }
        }
        
    def get_response(self, text):
        text = text.lower()
        for intent, data in self.intents.items():
            for pattern in data['patterns']:
                if pattern in text:
                    return random.choice(data['responses'])
        
        # अगर कुछ समझ न आए
        default_responses = [
            "यह काफी दिलचस्प है। क्या आप मुझे इसके बारे में थोड़ा और बता सकते हैं?",
            "मैं समझ रही हूँ। आगे क्या करना है?",
            "अच्छा! मैंने इसे नोट कर लिया है।"
        ]
        return random.choice(default_responses)

# ═══════════════════════════════════════════════════════════════
#  USER INTERFACE (UI)
# ═══════════════════════════════════════════════════════════════

class SrijalApp(App):
    def build(self):
        self.nlp = NLPEngine()
        
        main_layout = BoxLayout(orientation='vertical', spacing=0)
        
        # ─── Header ───
        header = BoxLayout(orientation='horizontal', size_hint=(1, None), height=dp(60), padding=[dp(15), dp(10)])
        with header.canvas.before:
            Color(0.1, 0.45, 0.9, 1) # नीला रंग
            RoundedRectangle(pos=header.pos, size=header.size, radius=[0, 0, dp(15), dp(15)])
        header.bind(pos=self._update_bg, size=self._update_bg)
        
        title_label = Label(text="Srijal AI - Master Pro", font_size=sp(20), bold=True, color=(1, 1, 1, 1), halign='left', valign='middle')
        title_label.bind(size=title_label.setter('text_size'))
        header.add_widget(title_label)
        
        # ─── Chat Display ───
        self.chat_container = GridLayout(cols=1, spacing=dp(10), padding=dp(15), size_hint_y=None)
        self.chat_container.bind(minimum_height=self.chat_container.setter('height'))
        
        self.scroll = ScrollView(size_hint=(1, 1))
        self.scroll.add_widget(self.chat_container)
        
        # Welcome Message
        self.add_message("नमस्ते! मैं सृजल हूँ। सिस्टम रेडी है।", is_user=False)
        
        # ─── Input Area ───
        input_box = BoxLayout(orientation='horizontal', size_hint=(1, None), height=dp(70), padding=dp(10), spacing=dp(10))
        with input_box.canvas.before:
            Color(1, 1, 1, 1)
            RoundedRectangle(pos=input_box.pos, size=input_box.size)
        input_box.bind(pos=self._update_bg, size=self._update_bg)
        
        self.text_input = TextInput(
            hint_text="अपना संदेश यहाँ लिखें...", 
            font_size=sp(16), 
            size_hint=(0.8, 1), 
            multiline=False,
            background_color=(0.95, 0.95, 0.95, 1),
            foreground_color=(0.1, 0.1, 0.1, 1)
        )
        
        send_btn = Button(
            text="➤", 
            font_size=sp(24), 
            size_hint=(0.2, 1), 
            background_color=(0.1, 0.45, 0.9, 1), 
            color=(1, 1, 1, 1),
            bold=True
        )
        send_btn.bind(on_press=self.send_message)
        self.text_input.bind(on_text_validate=self.send_message)
        
        input_box.add_widget(self.text_input)
        input_box.add_widget(send_btn)
        
        main_layout.add_widget(header)
        main_layout.add_widget(self.scroll)
        main_layout.add_widget(input_box)
        
        return main_layout
        
    def _update_bg(self, instance, value):
        instance.canvas.before.children[1].pos = instance.pos
        instance.canvas.before.children[1].size = instance.size

    def add_message(self, text, is_user=True):
        msg_color = (0.1, 0.45, 0.9, 1) if is_user else (1, 1, 1, 1)
        text_color = (1, 1, 1, 1) if is_user else (0.1, 0.1, 0.1, 1)
        align = 'right' if is_user else 'left'
        prefix = "आप: " if is_user else "सृजल: "
        
        msg_box = BoxLayout(orientation='vertical', size_hint_y=None, padding=dp(10))
        msg_label = Label(
            text=prefix + text,
            font_size=sp(16),
            color=text_color,
            halign=align,
            valign='middle',
            size_hint_y=None
        )
        msg_label.bind(texture_size=lambda *x: setattr(msg_label, 'height', msg_label.texture_size[1] + dp(20)))
        msg_label.bind(width=lambda *x: msg_label.setter('text_size')(msg_label, (msg_label.width, None)))
        
        with msg_box.canvas.before:
            Color(*msg_color)
            RoundedRectangle(pos=msg_box.pos, size=msg_box.size, radius=[dp(10)])
        msg_box.bind(pos=self._update_bg, size=self._update_bg)
        
        msg_box.add_widget(msg_label)
        msg_box.height = msg_label.height + dp(20)
        
        self.chat_container.add_widget(msg_box)
        Clock.schedule_once(lambda dt: self.scroll_to_bottom(), 0.1)

    def scroll_to_bottom(self):
        self.scroll.scroll_y = 0

    def send_message(self, instance):
        user_text = self.text_input.text.strip()
        if not user_text: return
        
        self.text_input.text = ""
        self.add_message(user_text, is_user=True)
        
        # एआई को सोचने का समय देना
        Clock.schedule_once(lambda dt: self.bot_reply(user_text), 0.5)

    def bot_reply(self, user_text):
        response = self.nlp.get_response(user_text)
        self.add_message(response, is_user=False)

if __name__ == '__main__':
    SrijalApp().run()
    # Trigger build  
