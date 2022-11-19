import tkinter as tk

class MainWindow(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('TextPro Editor')
    self.geometry('500x500')
    self.rowconfigure(0, minsize=800, weight=1)
    self.columnconfigure(1, minsize=800, weight=1)
    self.iconphoto(True, tk.PhotoImage(file=".//resources//icon.png"))