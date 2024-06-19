import tkinter as tk
from math import sqrt

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.expression = ""
        
        self.input_text = tk.StringVar()
        self.input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.input_frame.pack(side=tk.TOP)
        
        self.input_field = tk.Entry(self.input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)

        self.buttons_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        self.buttons_frame.pack()
        
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '√',
            '1', '2', '3', '-', '^',
            '0', '.', '=', '+'
        ]
        
        row = 0
        col = 0
        for button in buttons:
            if button not in {'=', 'C', '√', '^'}:
                b = tk.Button(self.buttons_frame, text=button, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda x=button: self.btn_click(x))
            elif button == '=':
                b = tk.Button(self.buttons_frame, text=button, fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=self.btn_equal)
            elif button == 'C':
                b = tk.Button(self.buttons_frame, text=button, fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=self.btn_clear)
            elif button == '√':
                b = tk.Button(self.buttons_frame, text=button, fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click('sqrt('))
            elif button == '^':
                b = tk.Button(self.buttons_frame, text=button, fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click('**'))
            
            b.grid(row=row, column=col, padx=1, pady=1)
            col += 1
            if col == 5:
                col = 0
                row += 1
                
    def btn_click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)
        
    def btn_clear(self):
        self.expression = ""
        self.input_text.set("")
        
    def btn_equal(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except ZeroDivisionError:
            self.input_text.set("Error: Div by 0")
            self.expression = ""
        except Exception:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
