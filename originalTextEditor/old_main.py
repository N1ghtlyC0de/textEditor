import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
      title = 'Text Pro – Open a file',
      filetypes = [("Text File", "*.txt"), ("All Files", "*.*")]
    )
  
    if not filepath:
        return
      
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode = "r", encoding = "utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"TextPro Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
      title = 'TextPro – Save a file',
      defaultextension = ".txt",
      filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"TextProEditor - {filepath}")

def show_about():
  '''Show About Us'''
  tk.messagebox.showinfo(message='Versión: 1\nAutores:\nCamilo Esteban Paez Neuta: cpaezn@unal.edu.co\n\nPablo Esteban Olaya Arias: polayaa@unal.edu.co')
    
window = tk.Tk()
window.title("TextPro Editor")
window.geometry('500x500')

icon = tk.PhotoImage(file='icon.png')
window.iconphoto(True, icon)

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2, bg='gray')
btn_open = tk.Button(frm_buttons, text="Open", bg='cyan', fg='black' , command=open_file)
btn_save = tk.Button(frm_buttons, text="Save As...", bg='cyan', fg='black' , command=save_file)
btn_about = tk.Button(frm_buttons, text='About Us', bg='cyan', fg='black' , command=show_about)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_about.grid(row=2, column=0, sticky='ew', padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()