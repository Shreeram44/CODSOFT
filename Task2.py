import tkinter as tk
import math

new_calculation = True

def button_click(event):
    global new_calculation
    text = event.widget.cget("text")

    if text == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            new_calculation = True
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "C":
        entry.delete(0, tk.END)
        new_calculation = True  

    elif text == "√":
        expression = entry.get()
        try:
            result = math.sqrt(float(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            new_calculation = True  
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    else:
        if new_calculation:
            entry.delete(0, tk.END)
            new_calculation = False  # Clear new calculation flag
        entry.insert(tk.END, text)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry widget to display the expression and results
entry = tk.Entry(window, font=("Times New Roman Bold", 24), justify="center")
entry.grid(row=0, column=0, columnspan=4)

# Define button labels
button_labels = [
    'C', '[', ']', '√',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '=', '+'
]

# Create and place buttons in a grid
row, col = 1, 0
buttons = []
for label in button_labels:
    button = tk.Button(window, text=label, padx=20, pady=20, font=("Helvetica", 18))
    button.grid(row=row, column=col)
    button.bind("<Button-1>", button_click)
    buttons.append(button)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the GUI application
window.mainloop()
