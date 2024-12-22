import tkinter as tk
from tkinter import messagebox
import math

def calculate(operation):
    try:
        num1 = float(entry1.get()) if entry1.get() else None
        num2 = float(entry2.get()) if entry2.get() else None
        result = None

        if operation == "ADD":
            result = num1 + num2
        elif operation == "SUB":
            result = num1 - num2
        elif operation == "MULT":
            result = num1 * num2
        elif operation == "DIV":
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            result = num1 / num2
        elif operation == "SQR":
            result = num1 ** 2
        elif operation == "SQRT":
            if num1 < 0:
                raise ValueError("Cannot calculate square root of a negative number.")
            result = math.sqrt(num1)
        elif operation == "CUB":
            result = num1 ** 3
        elif operation == "CBRT":
            result = math.pow(num1, 1/3)
        elif operation == "LOG":
            if num1 <= 0:
                raise ValueError("Logarithm undefined for non-positive numbers.")
            result = math.log10(num1)
        elif operation == "SIN":
            result = math.sin(math.radians(num1))
        elif operation == "COS":
            result = math.cos(math.radians(num1))
        elif operation == "TAN":
            result = math.tan(math.radians(num1))
        elif operation == "POW":
            result = math.pow(num1, num2)

        result_label.config(text=f"Result: {result}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", "An error occurred. Please check your input.")

# Create the main application window
root = tk.Tk()
root.title("Calculator GUI")
root.geometry("400x500")

# Input fields
entry1_label = tk.Label(root, text="First Number:")
entry1_label.pack()
entry1 = tk.Entry(root)
entry1.pack()

entry2_label = tk.Label(root, text="Second Number (if applicable):")
entry2_label.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Buttons for operations
operations = ["ADD", "SUB", "MULT", "DIV", "SQR", "SQRT", "CUB", "CBRT", "LOG", "SIN", "COS", "TAN", "POW"]
for op in operations:
    button = tk.Button(root, text=op, command=lambda op=op: calculate(op))
    button.pack(pady=5)

# Result display
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=10)

# Start the main loop
root.mainloop()
