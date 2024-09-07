import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.title("Note Taking App")
root.geometry("500x500")
text_area = tk.Text(root, wrap='word', font=("Arial", 12))
text_area.pack(expand=1, fill='both')
def save_note():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
def open_note():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
save_button = tk.Button(root, text="Save", command=save_note)
save_button.pack(side='left', padx=10, pady=10)

open_button = tk.Button(root, text="Open", command=open_note)
open_button.pack(side='right', padx=10, pady=10)
root.mainloop()
