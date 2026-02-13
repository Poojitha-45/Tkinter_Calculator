import tkinter as tk

# -------------------- Window Setup --------------------
root = tk.Tk()
root.title("Calculator")
root.configure(bg="black")
root.resizable(False, False)

# -------------------- Display --------------------
entry = tk.Entry(
    root,
    font=("Segoe UI", 20),
    bg="black",
    fg="white",
    bd=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=20, ipady=15)

# -------------------- Functions --------------------
def press(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# -------------------- Buttons --------------------
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for btn in buttons:
    if btn == '=':
        command = calculate
    else:
        command = lambda x=btn: press(x)

    tk.Button(
        root,
        text=btn,
        command=command,
        font=("Segoe UI", 14),
        width=5,
        height=2,
        bg="orange" if btn in "+-*/=" else "darkgrey",
        fg="white",
        bd=0
    ).grid(row=row, column=col, padx=6, pady=6)

    col += 1
    if col > 3:
        col = 0
        row += 1

# -------------------- Clear Button --------------------
tk.Button(
    root,
    text="C",
    command=clear,
    font=("Segoe UI", 14),
    bg="red",
    fg="white",
    bd=0,
    width=22,
    height=2
).grid(row=row, column=0, columnspan=4, pady=8)

# -------------------- Run App --------------------
root.mainloop()