import tkinter as tk

def press(key):
    current = entry_display.get()
    if key == "=":
        try:
            result = eval(current)
            entry_display.delete(0, tk.END)
            entry_display.insert(tk.END, str(result))
        except Exception as e:
            entry_display.delete(0, tk.END)
            entry_display.insert(tk.END, "Lỗi")
    elif key == "C":
        entry_display.delete(0, tk.END)
    else:
        entry_display.insert(tk.END, key)

root = tk.Tk()
root.title("Máy tính")

entry_display = tk.Entry(root, width=20)
entry_display.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, command=lambda key=button: press(key)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
