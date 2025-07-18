#!/usr/bin/env python3
"""
Python Calculator
A comprehensive calculator with command-line and GUI interfaces.
Supports basic arithmetic, scientific functions, and expression evaluation.
"""

import math
import re
import sys

# Try to import tkinter, handle gracefully if not available
try:
    import tkinter as tk
    from tkinter import ttk, messagebox
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False


class Calculator:
    """A calculator class with basic and scientific operations."""
    
    def __init__(self):
        self.history = []
        self.memory = 0
    
    def add(self, a, b):
        """Addition operation."""
        return a + b
    
    def subtract(self, a, b):
        """Subtraction operation."""
        return a - b
    
    def multiply(self, a, b):
        """Multiplication operation."""
        return a * b
    
    def divide(self, a, b):
        """Division operation with zero division handling."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        """Power operation."""
        return a ** b
    
    def sqrt(self, a):
        """Square root operation."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(a)
    
    def sin(self, a):
        """Sine function (radians)."""
        return math.sin(a)
    
    def cos(self, a):
        """Cosine function (radians)."""
        return math.cos(a)
    
    def tan(self, a):
        """Tangent function (radians)."""
        return math.tan(a)
    
    def log(self, a, base=10):
        """Logarithm function."""
        if a <= 0:
            raise ValueError("Cannot calculate logarithm of non-positive number")
        return math.log(a, base)
    
    def ln(self, a):
        """Natural logarithm."""
        if a <= 0:
            raise ValueError("Cannot calculate natural logarithm of non-positive number")
        return math.log(a)
    
    def factorial(self, n):
        """Factorial operation."""
        if n < 0 or not isinstance(n, int):
            raise ValueError("Factorial is only defined for non-negative integers")
        return math.factorial(n)
    
    def evaluate_expression(self, expression):
        """Safely evaluate a mathematical expression."""
        # Remove spaces and convert to lowercase
        expression = expression.replace(' ', '').lower()
        
        # Replace common mathematical functions
        replacements = {
            'sin': 'math.sin',
            'cos': 'math.cos',
            'tan': 'math.tan',
            'sqrt': 'math.sqrt',
            'log': 'math.log10',
            'ln': 'math.log',
            'pi': 'math.pi',
            'e': 'math.e',
            '^': '**'
        }
        
        for old, new in replacements.items():
            expression = expression.replace(old, new)
        
        # Only allow safe characters and functions
        allowed_chars = set('0123456789+-*/().math sincoqrtloge')
        if not all(c in allowed_chars for c in expression.replace('math.', '')):
            raise ValueError("Invalid characters in expression")
        
        try:
            result = eval(expression, {"__builtins__": {}}, {"math": math})
            self.history.append(f"{expression} = {result}")
            return result
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {str(e)}")
    
    def store_memory(self, value):
        """Store value in memory."""
        self.memory = value
    
    def recall_memory(self):
        """Recall value from memory."""
        return self.memory
    
    def clear_memory(self):
        """Clear memory."""
        self.memory = 0
    
    def get_history(self):
        """Get calculation history."""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()


class CalculatorGUI:
    """GUI interface for the calculator."""
    
    def __init__(self):
        if not TKINTER_AVAILABLE:
            raise ImportError("tkinter is not available. Please use CLI mode instead.")
        self.calculator = Calculator()
        self.create_gui()
        
    def create_gui(self):
        """Create the GUI interface."""
        self.root = tk.Tk()
        self.root.title("Python Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Display frame
        display_frame = ttk.Frame(self.root, padding="10")
        display_frame.pack(fill=tk.X)
        
        # Entry widget for display
        self.display_var = tk.StringVar(value="0")
        self.display = ttk.Entry(
            display_frame, 
            textvariable=self.display_var, 
            font=("Arial", 16),
            justify="right",
            state="readonly"
        )
        self.display.pack(fill=tk.X, pady=(0, 10))
        
        # Memory and history display
        self.info_var = tk.StringVar(value="Memory: 0")
        info_label = ttk.Label(display_frame, textvariable=self.info_var, font=("Arial", 10))
        info_label.pack()
        
        # Button frame
        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create buttons
        self.create_buttons(button_frame)
        
        # Bind keyboard events
        self.root.bind('<Key>', self.on_key_press)
        self.root.focus_set()
        
        self.current_input = ""
        self.last_result = 0
        
    def create_buttons(self, parent):
        """Create calculator buttons."""
        buttons = [
            ['C', 'CE', '⌫', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '='],
            ['sin', 'cos', 'tan', 'sqrt'],
            ['log', 'ln', '^', '!'],
            ['MC', 'MR', 'MS', 'M+']
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                btn = ttk.Button(
                    parent,
                    text=text,
                    command=lambda t=text: self.on_button_click(t),
                    width=8
                )
                btn.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
        
        # Configure grid weights
        for i in range(len(buttons)):
            parent.grid_rowconfigure(i, weight=1)
        for j in range(4):
            parent.grid_columnconfigure(j, weight=1)
    
    def on_button_click(self, text):
        """Handle button clicks."""
        try:
            if text == 'C':
                self.clear_all()
            elif text == 'CE':
                self.clear_entry()
            elif text == '⌫':
                self.backspace()
            elif text == '=':
                self.calculate()
            elif text == '±':
                self.toggle_sign()
            elif text in ['MC', 'MR', 'MS', 'M+']:
                self.memory_operation(text)
            elif text in ['sin', 'cos', 'tan', 'sqrt', 'log', 'ln', '!']:
                self.function_operation(text)
            elif text == '^':
                self.add_to_input('**')
            else:
                self.add_to_input(text)
        except Exception as e:
            self.display_error(str(e))
    
    def on_key_press(self, event):
        """Handle keyboard input."""
        key = event.char
        if key in '0123456789+-*/.()':
            self.add_to_input(key)
        elif key == '\r' or key == '=':
            self.calculate()
        elif key == '\b':
            self.backspace()
        elif key.lower() == 'c':
            self.clear_all()
    
    def add_to_input(self, text):
        """Add text to current input."""
        if self.current_input == "0" and text.isdigit():
            self.current_input = text
        else:
            self.current_input += text
        self.update_display()
    
    def clear_all(self):
        """Clear all input and reset."""
        self.current_input = ""
        self.display_var.set("0")
    
    def clear_entry(self):
        """Clear current entry."""
        self.current_input = ""
        self.display_var.set("0")
    
    def backspace(self):
        """Remove last character."""
        if self.current_input:
            self.current_input = self.current_input[:-1]
            if not self.current_input:
                self.display_var.set("0")
            else:
                self.update_display()
    
    def toggle_sign(self):
        """Toggle the sign of current input."""
        if self.current_input and self.current_input != "0":
            if self.current_input.startswith('-'):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
            self.update_display()
    
    def calculate(self):
        """Perform calculation."""
        if not self.current_input:
            return
        
        try:
            result = self.calculator.evaluate_expression(self.current_input)
            self.display_var.set(str(result))
            self.last_result = result
            self.current_input = str(result)
        except Exception as e:
            self.display_error(str(e))
    
    def function_operation(self, func):
        """Perform function operations."""
        try:
            if not self.current_input:
                value = self.last_result
            else:
                value = float(self.current_input)
            
            if func == 'sin':
                result = self.calculator.sin(value)
            elif func == 'cos':
                result = self.calculator.cos(value)
            elif func == 'tan':
                result = self.calculator.tan(value)
            elif func == 'sqrt':
                result = self.calculator.sqrt(value)
            elif func == 'log':
                result = self.calculator.log(value)
            elif func == 'ln':
                result = self.calculator.ln(value)
            elif func == '!':
                result = self.calculator.factorial(int(value))
            
            self.display_var.set(str(result))
            self.current_input = str(result)
            self.last_result = result
        except Exception as e:
            self.display_error(str(e))
    
    def memory_operation(self, op):
        """Handle memory operations."""
        try:
            if op == 'MC':
                self.calculator.clear_memory()
            elif op == 'MR':
                result = self.calculator.recall_memory()
                self.display_var.set(str(result))
                self.current_input = str(result)
            elif op == 'MS':
                value = float(self.current_input) if self.current_input else self.last_result
                self.calculator.store_memory(value)
            elif op == 'M+':
                value = float(self.current_input) if self.current_input else self.last_result
                self.calculator.store_memory(self.calculator.recall_memory() + value)
            
            self.update_memory_display()
        except Exception as e:
            self.display_error(str(e))
    
    def update_display(self):
        """Update the display with current input."""
        self.display_var.set(self.current_input)
    
    def update_memory_display(self):
        """Update memory display."""
        memory_value = self.calculator.recall_memory()
        self.info_var.set(f"Memory: {memory_value}")
    
    def display_error(self, message):
        """Display error message."""
        messagebox.showerror("Error", message)
        self.clear_entry()
    
    def run(self):
        """Start the GUI."""
        self.root.mainloop()


class CalculatorCLI:
    """Command-line interface for the calculator."""
    
    def __init__(self):
        self.calculator = Calculator()
    
    def print_menu(self):
        """Print the main menu."""
        print("\n" + "="*50)
        print("         PYTHON CALCULATOR")
        print("="*50)
        print("1. Basic Operations")
        print("2. Scientific Functions")
        print("3. Expression Evaluator")
        print("4. Memory Operations")
        print("5. View History")
        print("6. Clear History")
        print("7. Exit")
        print("-"*50)
    
    def basic_operations(self):
        """Handle basic arithmetic operations."""
        print("\nBasic Operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        
        try:
            choice = input("\nSelect operation (1-5): ")
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            operations = {
                '1': self.calculator.add,
                '2': self.calculator.subtract,
                '3': self.calculator.multiply,
                '4': self.calculator.divide,
                '5': self.calculator.power
            }
            
            if choice in operations:
                result = operations[choice](a, b)
                print(f"\nResult: {result}")
                self.calculator.history.append(f"{a} {['+', '-', '*', '/', '^'][int(choice)-1]} {b} = {result}")
            else:
                print("Invalid choice!")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def scientific_functions(self):
        """Handle scientific function operations."""
        print("\nScientific Functions:")
        print("1. Square Root")
        print("2. Sine (radians)")
        print("3. Cosine (radians)")
        print("4. Tangent (radians)")
        print("5. Logarithm (base 10)")
        print("6. Natural Logarithm")
        print("7. Factorial")
        
        try:
            choice = input("\nSelect function (1-7): ")
            
            if choice == '7':  # Factorial
                n = int(input("Enter integer: "))
                result = self.calculator.factorial(n)
            else:
                a = float(input("Enter number: "))
                functions = {
                    '1': self.calculator.sqrt,
                    '2': self.calculator.sin,
                    '3': self.calculator.cos,
                    '4': self.calculator.tan,
                    '5': self.calculator.log,
                    '6': self.calculator.ln
                }
                
                if choice in functions:
                    result = functions[choice](a)
                else:
                    print("Invalid choice!")
                    return
            
            print(f"\nResult: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def expression_evaluator(self):
        """Handle expression evaluation."""
        print("\nExpression Evaluator")
        print("Supported: +, -, *, /, ^, sin, cos, tan, sqrt, log, ln, pi, e")
        print("Example: sin(pi/2) + sqrt(16) * 2")
        
        try:
            expression = input("\nEnter expression: ")
            result = self.calculator.evaluate_expression(expression)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def memory_operations(self):
        """Handle memory operations."""
        print("\nMemory Operations:")
        print("1. Store in memory")
        print("2. Recall from memory")
        print("3. Clear memory")
        print(f"Current memory value: {self.calculator.recall_memory()}")
        
        try:
            choice = input("\nSelect operation (1-3): ")
            
            if choice == '1':
                value = float(input("Enter value to store: "))
                self.calculator.store_memory(value)
                print(f"Stored {value} in memory")
            elif choice == '2':
                value = self.calculator.recall_memory()
                print(f"Memory value: {value}")
            elif choice == '3':
                self.calculator.clear_memory()
                print("Memory cleared")
            else:
                print("Invalid choice!")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def view_history(self):
        """Display calculation history."""
        history = self.calculator.get_history()
        if history:
            print("\nCalculation History:")
            print("-" * 30)
            for i, calc in enumerate(history, 1):
                print(f"{i}. {calc}")
        else:
            print("\nNo calculations in history.")
    
    def clear_history(self):
        """Clear calculation history."""
        self.calculator.clear_history()
        print("\nHistory cleared.")
    
    def run(self):
        """Start the command-line interface."""
        print("Welcome to Python Calculator!")
        
        while True:
            self.print_menu()
            choice = input("Enter your choice (1-7): ")
            
            if choice == '1':
                self.basic_operations()
            elif choice == '2':
                self.scientific_functions()
            elif choice == '3':
                self.expression_evaluator()
            elif choice == '4':
                self.memory_operations()
            elif choice == '5':
                self.view_history()
            elif choice == '6':
                self.clear_history()
            elif choice == '7':
                print("\nThank you for using Python Calculator!")
                break
            else:
                print("\nInvalid choice! Please try again.")
            
            input("\nPress Enter to continue...")


def main():
    """Main function to choose interface."""
    if len(sys.argv) > 1:
        if sys.argv[1] == '--cli':
            cli = CalculatorCLI()
            cli.run()
        elif sys.argv[1] == '--gui':
            gui = CalculatorGUI()
            gui.run()
        else:
            print("Usage: python calculator.py [--cli|--gui]")
            print("No argument defaults to GUI mode")
    else:
        # Default to GUI if no arguments
        if TKINTER_AVAILABLE:
            try:
                gui = CalculatorGUI()
                gui.run()
            except Exception as e:
                print(f"GUI error: {e}")
                print("Starting CLI mode...")
                cli = CalculatorCLI()
                cli.run()
        else:
            print("GUI not available (tkinter not installed), starting CLI mode...")
            cli = CalculatorCLI()
            cli.run()


if __name__ == "__main__":
    main()