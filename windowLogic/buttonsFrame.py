import tkinter as tk

class ButtonsFrame:
  def __init__(self, window, controller):
    self.window = window
    self.controller = controller
    self.frmButtons = tk.Frame(self.window, relief=tk.RAISED, bd=3, bg = "gray")
    self.btnOpen = tk.Button(self.frmButtons, text="Open", bg='cyan', fg='black' , command=self.controller.open_file)
    self.btnSave = tk.Button(self.frmButtons, text="Save As...", bg='cyan', fg='black' , command=self.controller.save_file)
    self.btnAbout = tk.Button(self.frmButtons, text='About Us', bg='cyan', fg='black' , command=self.controller.show_about)
    self.btnOpen.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    self.btnSave.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    self.btnAbout.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
    self.frmButtons.grid(row=0, column=0, sticky="ns")