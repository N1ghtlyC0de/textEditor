import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

class Controller:
  def __init__(self, window):
    self.window = window
    self.txt_edit = tk.Text(window)
    self.txt_edit.grid(row=0, column=1, sticky="nsew")
    
  def open_file(self):
    """Open a file for editing."""
    filepath = askopenfilename(
      title = 'Text Pro - Open a file',
      filetypes = [("Text File", "*.txt"), ("All Files", "*.*")]
    )
    
    if not filepath:
      return
      
    self.txt_edit.delete("1.0", tk.END)
    with open(filepath, mode = "r", encoding = "utf-8") as input_file:
        text = input_file.read()
        self.txt_edit.insert(tk.END, text)
    self.window.title(f"TextPro Editor - {filepath}")
  
  def save_file(self):
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
      title = 'TextPro – Save a file',
      defaultextension = ".txt",
      filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    
    if not filepath:
      return
      
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = self.txt_edit.get("1.0", tk.END)
        output_file.write(text)
    self.window.title(f"TextProEditor - {filepath}")
    
  def show_about(self):
    '''Show About Us'''
    tk.messagebox.showinfo(message='Versión: 1\nAutores:\nCamilo Esteban Paez Neuta: cpaezn@unal.edu.co\n\nPablo Esteban Olaya Arias: polayaa@unal.edu.co')