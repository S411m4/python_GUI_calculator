from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label



class CalcLayout(GridLayout):
    def __init__(self, **kwagrs):
        super(CalcLayout, self).__init__(**kwagrs)

        self.display_text = []
        self.cols = 1

        self.display_label = Label(text = '')
        self.btn_equal = Button(text = "=")
        
        self.add_widget(self.display_label)
        self.add_widget(self.btn_equal)
        self.btn_equal.bind(on_press=self.display)

        self.btn1 = Button(text = '1')
        self.add_widget(self.btn1)
        self.btn1.bind(on_press = self.display)
        
    def display(self, instance):
        self.display_text.append(self.btn1.text)
        text_ = ' '.join(self.display_text)
        self.display_label.text = text_

        return self.display_label.text



class myApp(App):
    def build(self):
        
        return CalcLayout()



myApp().run()
print(display_text)
