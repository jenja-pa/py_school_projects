from  tkinter import *
import time
 
tk = Tk()
tk.title = "Sea War"


canvas = Canvas(tk, width=500, height=500)
canvas.pack()

ship_image = PhotoImage(file = "ship.gif")
s = canvas.create_image(500, 0, anchor =NW, image = ship_image)

for y in range(200):
  canvas.move(s, -3, 0)
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