import tkinter as tk
from tkinter import messagebox

def show_alert():
  messagebox.showinfo("Alert", "Hello, World!")

# Create the main window
root = tk.Tk()
root.title("Hello World GUI")

# Create a button that shows an alert
alert_button = tk.Button(root, text="Click Me", command=show_alert)
alert_button.pack(pady=20)

# Run the application
root.mainloop()