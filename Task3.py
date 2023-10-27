import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    
    if length <= 0:
        password_label.config(text="Invalid length")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_label.config(text="Generated Password:")

# Create the main window
window = tk.Tk()
window.title("Random Password Generating Application")

# Set the initial size of the window (width x height)
window.geometry("400x300")

# Label for password generation
length_label = tk.Label(window, text="Enter the Password Length:")
length_label.pack(pady=10)

# Entry field for password length
length_entry = tk.Entry(window, width=10, justify="center")
length_entry.pack(pady=5)

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Label to display the generated password
password_label = tk.Label(window, text="")
password_label.pack()

# Entry field to display the generated password
password_entry = tk.Entry(window, width=30, justify="center")
password_entry.pack(pady=5)

# Run the GUI application
window.mainloop()
