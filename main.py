from windowLogic.controller import Controller 
from windowLogic.mainWindow import MainWindow
from windowLogic.buttonsFrame import ButtonsFrame 

def main():  
  window = MainWindow()
  ctrl = Controller(window)
  ButtonsFrame(window, ctrl)
  window.mainloop()
  pass
  
if __name__ == '__main__':
  main()