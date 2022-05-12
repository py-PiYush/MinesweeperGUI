from tkinter import *
from cell import Cell
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
center_frame.place(x=utils.width_prct(20), y=utils.height_prct(20))

left_frame = Frame(
    root, bg=settings.COLOR, width=utils.width_prct(20), height=utils.height_prct(60)
)
left_frame.place(x=0, y=utils.height_prct(20))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell()
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x + 3, row=y + 1)

# Run the window
root.mainloop()
