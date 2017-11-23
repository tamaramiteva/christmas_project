# tk.overrideredirect(1) causes full screen behaviour
# If run from the command line you can exit with Ctrl-c or Alt-F4 to close window

import time
import random
from datetime import datetime
from Tkinter import *

tk = Tk()

w, h = tk.winfo_screenwidth(), tk.winfo_screenheight()
tk.overrideredirect(1)
tk.geometry("%dx%d+0+0" % (w, h))
tk.focus_set()  # <-- move focus to this widget
tk.bind("<Escape>", lambda e: e.widget.quit())

# canvas = Canvas(tk, width=w, height=h, bg='black')
canvas = Canvas(tk, width=800, height=600, bg='black')
canvas.create_text(400, 130, text="Christmas",
                   fill='red', font=('Times', 100))

canvas.create_text(400, 250, text="Countdown!",
                   fill='red', font=('Times', 100))
canvas.pack()

flake = [];
moves = []
for i in range(30):
    flake.append(
        canvas.create_text(random.randrange(800), random.randrange(600), text="*", fill="#ffffff", font="Times 30"))
    moves.append([0.1 + random.random() / 10, 2.7 + 3.0 * random.random()])


def update():
    global canvas, tk, t1, t2

    try:
        canvas.delete(t1)
        canvas.delete(t2)
    except:
        pass

    days = str(24 - int(datetime.now().strftime('%d')))
    hours = str(23 - int(datetime.now().strftime('%H')))
    mins = str(59 - int(datetime.now().strftime('%M')))
    secs = str(59 - int(datetime.now().strftime('%S')))

    time_str = days + ' days ' + hours + ' hours '
    t1 = canvas.create_text(380, 410, text=time_str,
                            fill='green', font=('Times', 64))
    time_str = mins + ' mins ' + secs + ' seconds'
    t2 = canvas.create_text(400, 490, text=time_str,
                            fill='green', font=('Times', 64))
    tk.update_idletasks()  # redraw
    tk.update()


def update_snow():
    global flake, canvas, tk, moves

    for i in range(len(flake)):
        p = canvas.coords(flake[i])
        p[0] += moves[i][0]
        p[1] += moves[i][1]
        canvas.coords(flake[i], p[0], p[1])
        if (p[1] > 610):
            canvas.coords(flake[i], random.randrange(800), -10)
        tk.update_idletasks()  # redraw
        tk.update()  # process events


try:
    while 1:
        update()
        update_snow()
        time.sleep(0.05)
except:
    pass