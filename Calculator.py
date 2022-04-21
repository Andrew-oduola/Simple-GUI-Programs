# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 15:36:43 2022

@author: Andrew
"""

import tkinter as tk
#import math

LARGE_FONT_STYLE = ('Arial', 40, "bold" )
SMALL_FONT_STYLE = ('Arial', 16 )
DIGIT_FONT_STYLE = ('Arial', 24, "bold" )
DEFAULT_FONT_STYLE = ('Arial', 20 )

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOUR = "#25265E"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        
        self.total_expression = ""
        self.current_expresstion = ""
        
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_label()
        
        self.digits = {
            7:(1, 1), 8:(1, 2), 9:(1, 3),
            4:(2, 1), 5:(2, 2), 6:(2, 3),
            1:(3, 1), 2:(3, 2), 3:(3, 3),
            0:(4, 2), '.':(4, 1)
            
            }
        
        self.operations = {"/":"\u00F7", "*":"\u00D7","-":"-" ,"+":"+"}
        
        
        self.button_frame = self.create_button_frame()
        
        self.button_frame.rowconfigure(0, weight=1)
        
        for x in range(1, 5):
             self.button_frame.rowconfigure(x, weight=1)
             self.button_frame.columnconfigure(x, weight=1)
             
        self.create_digit_button()
        self.create_operators_button()
        self.create_special_buttons()
        self.bind_keys()
    
    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event,digit=key: self.add_to_expression(digit))
            
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operators(operator))
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()
        
    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, 
                              anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOUR,
                              padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")
        
        label = tk.Label(self.display_frame, text=self.current_expresstion, 
                              anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOUR,
                              padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill="both")
        
        return total_label, label
        
        
        
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame
    
    def add_to_expression(self, value):
        self.current_expresstion += str(value)
        self.update_label()
    
    
    def create_digit_button(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=WHITE, 
                               fg=LABEL_COLOUR, font=DIGIT_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
            
    def append_operators(self, operator):
        self.current_expresstion += operator
        self.total_expression += self.current_expresstion
        self.current_expresstion=""
        self.update_total_label()
        self.update_label() 
    
    def create_operators_button(self):
        i=0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=symbol, bg=OFF_WHITE, 
                               fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, 
                               borderwidth=0, command=lambda x=operator: self.append_operators(x) )
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i+=1
    
    
    def clear(self):
        self.current_expresstion=""
        self.total_expression=""
        self.update_label()
        self.update_total_label()
        
    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="C", bg=OFF_WHITE, 
                           fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, 
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)
        
    def square(self):
        self.current_expresstion = str(eval(f"{self.current_expresstion}**2"))
        
        self.update_label() 
        
    def create_square_button(self):
        button = tk.Button(self.button_frame, text="x\u00B2", bg=OFF_WHITE, 
                           fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, 
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)
        
    def sqrt(self):
        self.current_expresstion = str(eval(f"{self.current_expresstion}**0.5"))
        
        self.update_label() 
        
    def create_sqrt_button(self):
        button = tk.Button(self.button_frame, text="\u221ax", bg=OFF_WHITE, 
                            fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, 
                           borderwidth=0, command=self.sqrt )
        button.grid(row=0, column=3, sticky=tk.NSEW)
        
    
        
    def evaluate(self):
        self.total_expression += self.current_expresstion
        self.update_total_label()
        
        try:
            self.current_expresstion = str(eval(self.total_expression))
        
            self.total_expression = ""
        except Exception as e:
            self.current_expresstion = 'Error'
        finally:
            self.update_label()
        
        
    def create_equals_button(self):
        button = tk.Button(self.button_frame, text="=", bg=LIGHT_BLUE, 
                           fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, 
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)
    
    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f'{symbol}')
        self.total_label.config(text=expression)
        
    def update_label(self):
        self.label.config(text=self.current_expresstion[:11 ])
    
    def run(self):
        self.window.mainloop()
        

if __name__ == "__main__":
    calc = Calculator()
    calc.run()