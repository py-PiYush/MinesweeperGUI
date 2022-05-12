from ctypes import util
from tkinter import *
import settings
import utils

# Instantiate window instance
root = Tk()

root.configure(bg=settings.COLOR)
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")  # changes size of window
root.title("Minesweeper")  # changes title
root.resizable(False, False)  # Prevents resizing of window

top_frame = Frame(
    root, bg=settings.COLOR, width=settings.WIDTH, height=utils.height_prct(20)
)

top_frame.place(x=0, y=0)

bottom_frame = Frame(
    root, bg=settings.COLOR, width=settings.WIDTH, height=utils.height_prct(20)
)
bottom_frame.place(x=0, y=utils.height_prct(80))

center_frame = Frame(
    root, bg=settings.COLOR, width=settings.WIDTH, height=utils.height_prct(60)
)
center_frame.place(x=0, y=utils.height_prct(20))

# Run the window

root.mainloop()
