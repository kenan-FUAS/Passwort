from tkinter import Tk
import time



r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(input(":"))
r.update() # now it stays on the clipboard after the window is closed
#r.destroy()

time.sleep(5)
r.clipboard_append("")

# Anwendung: input mit timer, wenn 'e' eingegeben --> clipboard_append(""), optionen()
#           wenn timer vorbei --> clipboard_append("")

