from kivy.app import App
from kivy.uix.button import Button

class AIAssistantApp(App):
    def build(self):
        return Button(text='Hello, My System is Ready!', font_size=50)

if __name__ == '__main__':
    AIAssistantApp().run()
