import tkinter as tk

# Function to add button text to the entry
def press(key):
    entry.insert(tk.END, key)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Function to delete the last character
def delete():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("480x480")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=('Arial', 24), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('DEL', 5, 1)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=clear)
    elif text == 'DEL':
        btn = tk.Button(root, text=text, width=11, height=2, font=('Arial', 14), command=delete)
        btn.grid(row=row, column=col, columnspan=2, padx=5, pady=5)
        continue
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                        command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
