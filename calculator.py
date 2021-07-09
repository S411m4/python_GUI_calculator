from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


#calculator layout
class CalcLayout(GridLayout):
    def __init__(self, **kwargs):
        super(CalcLayout, self).__init__(**kwargs)

        self.ans = ''
        #main layout
        self.cols = 1

        #display screen
        self.display_screen = Label(text='')
        self.add_widget(self.display_screen)
        self.display_text = []
        #buttons
        self.btns_layout = GridLayout()
        self.btns_layout.cols = 4

        self.btn7 = Button(text = "7")
        self.btn8 = Button(text = "8")
        self.btn9 = Button(text = "9")
        self.button_add = Button(text = "+")
        self.button_subtract = Button (text = "-")
        self.button_divide = Button(text = "/")
        self.button_multiply = Button(text = "X")
        self.btn4 = Button(text = "4")
        self.btn5 = Button(text = "5")
        self.btn6 = Button(text = "6")
        self.btn1 = Button(text = "1")
        self.btn2 = Button(text = "2")
        self.btn3 = Button(text = "3")
        self.button_equal = Button(text = "=")
        self.btn0 = Button(text = "0")
        self.button_back_space = Button(text = "<x|")
        self.button_answer = Button(text = "Ans")
        
        self.btns_layout.add_widget(self.btn7)
        self.btns_layout.add_widget(self.btn8)
        self.btns_layout.add_widget(self.btn9)
        self.btns_layout.add_widget(self.button_add)
        self.btns_layout.add_widget(self.btn4)
        self.btns_layout.add_widget(self.btn5)
        self.btns_layout.add_widget(self.btn6)
        self.btns_layout.add_widget(self.button_subtract)
        self.btns_layout.add_widget(self.btn1)
        self.btns_layout.add_widget(self.btn2)
        self.btns_layout.add_widget(self.btn3)
        self.btns_layout.add_widget(self.button_multiply)
        self.btns_layout.add_widget(self.button_answer)
        self.btns_layout.add_widget(self.btn0)
        self.btns_layout.add_widget(self.button_back_space)
        self.btns_layout.add_widget(self.button_divide)

        #add buttons layout
        self.add_widget(self.btns_layout)
        
        #Ans button
        self.add_widget(self.button_equal)


        # buttons functionality
        self.btn1.bind(on_press = self.display_btn1)
        self.btn2.bind(on_press = self.display_btn2)
        self.btn3.bind(on_press = self.display_btn3)
        self.btn4.bind(on_press = self.display_btn4)
        self.btn5.bind(on_press = self.display_btn5)
        self.btn6.bind(on_press = self.display_btn6)
        self.btn7.bind(on_press = self.display_btn7)
        self.btn8.bind(on_press = self.display_btn8)
        self.btn9.bind(on_press = self.display_btn9)
        self.btn0.bind(on_press = self.display_btn0)
        self.button_add.bind(on_press = self.display_button_add)
        self.button_subtract.bind(on_press = self.display_button_subtract)
        self.button_divide.bind(on_press = self.display_button_divide)
        self.button_multiply.bind(on_press = self.display_button_multiply)
        self.button_back_space.bind(on_press = self.backspace)
        self.button_equal.bind(on_press = self.calculate)
        self.button_answer.bind(on_press = self.answer)

    # def buttons functions:
    def display_btn1(self, instance):
        self.display_text.append(self.btn1.text)
        self.text_ = ''.join(self.display_text)
        self.display_screen.text = self.text_

        return self.display_screen.text

    def display_btn2(self, instance):
        self.display_text.append(self.btn2.text)
        self.text_ = ''.join(self.display_text)
        self.display_screen.text = self.text_

        return self.display_screen.text

    def display_btn3(self, instance):
        self.display_text.append(self.btn3.text)
        self.text_ = ''.join(self.display_text)
        self.display_screen.text = self.text_

        return self.display_screen.text


    def display_btn4(self, instance):
        self.display_text.append(self.btn4.text)
        self.text_ = ''.join(self.display_text)
        self.display_screen.text = self.text_

        return self.display_screen.text

    def display_btn5(self, instance):
        self.display_text.append(self.btn5.text)
        self.text_ = ''.join(self.display_text)
        self.display_screen.text = self.text_

        return self.display_screen.text


    def display_btn6(self, instance):
        self.display_text.append(self.btn6.text)
        self.text_ = ''.join(self.display_text)
        self.display_screen.text = self.text_

        return self.display_screen.text

    def display_btn7(self, instance):
        self.display_text.append(self.btn7.text)
        self.text_ = ''.join(self.display_text)
        self.display_screen.text = self.text_

        return self.display_screen.text

    def display_btn8(self, instance):
        self.display_text.append(self.btn8.text)
        self.text_ = ''.join(self.display_text)
        self.display_screen.text = self.text_

        return self.display_screen.text

    def display_btn9(self, instance):
        self.display_text.append(self.btn9.text)
        self.text_ = ''.join(self.display_text)
        self.display_screen.text = self.text_

        return self.display_screen.text
    
    def display_btn0(self, instance):
        self.display_text.append(self.btn0.text)
        self.text_ = ''.join(self.display_text)
        self.display_screen.text = self.text_

        return self.display_screen.text

    def display_button_subtract(self, instance):
        self.display_text.append(self.button_subtract.text)
        self.text_ = ''.join(self.display_text)
        self.display_screen.text = self.text_

        return self.display_screen.text

    def display_button_add(self, instance):
        self.display_text.append(self.button_add.text)
        self.text_ = ''.join(self.display_text)
        self.display_screen.text = self.text_

        return self.display_screen.text

    def display_button_multiply(self, instance):
        self.display_text.append("*")
        self.text_ = ''.join(self.display_text)
        self.display_screen.text = self.text_

        return self.display_screen.text

    def display_button_divide(self, instance):
        self.display_text.append(self.button_divide.text)
        self.text_ = ''.join(self.display_text)
        self.display_screen.text = self.text_

        return self.display_screen.text

    def backspace(self, instance):
        try:
            self.display_text.pop()
            self.text_ = ''.join(self.display_text)
            self.display_screen.text = self.text_
        except:
            pass
        return self.display_screen.text

    def calculate(self, instance):
        try:
            self.equation = ''.join(self.display_text)
            self.ans = str(eval(self.equation))
            self.display_screen.text = self.ans
        except:
            self.display_screen.text = "Error"
        
        self.display_text.clear()
        return self.display_screen.text

    def answer(self, instance):
        self.display_text.append(self.ans)
        self.text_ = ''.join(self.display_text)
        self.display_screen.text = self.text_
        return self.display_screen.text
    
    

    

class Calculator(App):
    def build(self):
        return CalcLayout()

if __name__ == '__main__':
    Calculator().run()
