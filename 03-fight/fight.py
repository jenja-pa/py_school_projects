import time
from tkinter import *
import random

tk = Tk()
tk.title = "Sea War"

canvas = Canvas(tk, width=500, height=500)
canvas.pack()

def draw_gun(c_x):
    canvas.create_rectangle(c_x-60, 480, c_x+60, 500, fill="black")
    canvas.create_rectangle(c_x-10, 460, c_x+10, 480, fill="black")

b = 0
shots = 0
def ball(event):
    global b, shots
    # Витираємо попередній напис
    canvas.create_text(420, 100, text="кількість пострілів: " + str(shots), fill="#F0F0ED")
    if shots < 10:
        shots = shots + 1
        canvas.create_text(420, 100, text="кількість пострілів: " + str(shots))            
        canvas.delete(b)
        b=canvas.create_oval(240, 460,260,480, fill="gray")
    else:
        canvas.create_text(420, 100, text="Ядра закінчилися!")            

canvas.bind_all("<space>", ball)

ship_image = PhotoImage(file = "ship.gif")

draw_gun(250)

# Основний процес гри
for z in range(10):
    s = canvas.create_image(500, 0, anchor =NW, image = ship_image)
    v = random.randint(2, 5)
    for y in range(300):
        canvas.move(s, -v, 0)
        canvas.move(b, 0, -5)
        tk.update()
        time.sleep(0.02)


# gFrame = Frame(master=  tk,width=500, height=500, bg="white")
 
# e = Entry(width=20)
# b = Button(text="Преобразовать")
# l = Label(bg='black', fg='white', width=20)
 
# def strToSortlist(event):
#     s = e.get()
#     s = s.split()
#     s.sort()
#     l['text'] = ' '.join(s)
 
# b.bind('<Button-1>', strToSortlist)
 
# e.pack()
# b.pack()
# l.pack()

tk.mainloop()