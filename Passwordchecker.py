import tkinter as tk
import re

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[0-9]', password):
        strength += 1
    if re.search(r'[^a-zA-Z0-9]', password):
        strength += 1
    return strength

def submit_password(event=None):  # Allow binding to events
    password = password_entry.get()
    strength_level = check_password_strength(password)
    color = ["red", "orange", "yellow", "lightgreen", "green"][strength_level-1]
    result_label.config(text=f"Password strength level: {strength_level} out of 5", fg=color)

def toggle_password_visibility():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_button.config(text='Show Password')
    else:
        password_entry.config(show='')
        toggle_button.config(text='Hide Password')

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")  # Set the size of the window
root.configure(bg="black")  # Set the background color to black

label = tk.Label(root, text="Enter a password to check its strength:", font=("Arial", 12), bg="black", fg="white")
label.pack(pady=10)  # Add some vertical padding

password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=25, bg="black", fg="white", insertbackground="white")
password_entry.pack(pady=5)
password_entry.bind("<Return>", submit_password)  # Bind the Enter key to submit_password function

toggle_button = tk.Button(root, text="Show Password", command=toggle_password_visibility, font=("Arial", 12), bg="black", fg="white")
toggle_button.pack(pady=5)

submit_button = tk.Button(root, text="Check Strength", command=submit_password, font=("Arial", 12), bg="black", fg="white")
submit_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="black", fg="white")
result_label.pack(pady=10)

root.mainloop()
