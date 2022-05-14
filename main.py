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

game_title = Label(
    top_frame,
    bg=settings.COLOR,
    fg="white",
    text="MineSweeper",
    font=("Jokerman", 24),
)
game_title.place(x=utils.width_prct(23), y=10)

bottom_frame = Frame(
    root, bg=settings.COLOR, width=settings.WIDTH, height=utils.height_prct(20)
)
bottom_frame.place(x=0, y=utils.height_prct(80))

center_frame = Frame(
    root, bg=settings.COLOR, width=settings.WIDTH, height=utils.height_prct(60)
)
center_frame.place(x=utils.width_prct(10), y=utils.height_prct(20))

left_frame = Frame(
    root, bg=settings.COLOR, width=utils.width_prct(10), height=utils.height_prct(60)
)
left_frame.place(x=0, y=utils.height_prct(20))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(y, x)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y)

Cell.create_cell_count_label(bottom_frame)
Cell.cell_count_label_object.place(x=utils.width_prct(10), y=0)

Cell.create_timer_label(bottom_frame)
Cell.timer_object.place(x=utils.width_prct(60), y=0)
Cell.update_time()

Cell.randomize_mines()


# Run the window
root.mainloop()
