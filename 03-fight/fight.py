from  tkinter import *
import time
 
tk = Tk()
tk.title = "Sea War"

canvas = Canvas(tk, width=500, height=500)
canvas.pack()

def draw_gun(c_x):
  canvas.create_rectangle(c_x-60, 480, c_x+60, 500, fill="black")
  canvas.create_rectangle(c_x-10, 460, c_x+10, 480, fill="black")

def ball(event):
  global b, shots
  canvas.delete(b)
  b=canvas.create_oval(240, 460,260,480, fill="gray")
canvas.bind_all("<space>", ball)

ship_image = PhotoImage(file = "ship.gif")
s = canvas.create_image(500, 0, anchor =NW, image = ship_image)
b = 0

shots = 0

draw_gun(250)

for y in range(200):
  canvas.move(s, -3, 0)
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