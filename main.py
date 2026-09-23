
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class XSMBApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        title = Label(text='XSMB Pro 365', font_size='28sp', bold=True, size_hint_y=0.3)
        info = Label(text='App da build thanh cong!\nKhong con loi Buildozer failed nua.', font_size='18sp')
        btn = Button(text='Bam vao day', size_hint_y=0.3, background_color=(0.2, 0.6, 1, 1))
        btn.bind(on_press=lambda x: setattr(info, 'text', 'Chuc mung! App chay ngon lanh roi!'))
        layout.add_widget(title)
        layout.add_widget(info)
        layout.add_widget(btn)
        return layout

XSMBApp().run()
