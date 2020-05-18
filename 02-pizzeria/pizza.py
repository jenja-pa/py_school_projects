from tkinter import *

tk = Tk()
tk.title = "Pizzeria"
tk.geometry("440x300")

# =====

lbl = Label(text="Найменування", font="10", justify="left")
lbl.place(x=20, y=20, width=130, height=40)

lbl = Label(text="Ціна, грн.", font="10", justify="left")
lbl.place(x=150, y=20, width=80, height=40)

lbl = Label(text="Кількість", font="10", justify="left")
lbl.place(x=230, y=20, width=80, height=40)

lbl = Label(text="Вартість, грн.", font="10", justify="left")
lbl.place(x=310, y=20, width=130, height=40)

# ----

lbl = Label(text="Піца", font="10", justify="left")
lbl.place(x=20, y=60, width=130, height=30)

P1 = Entry(font="Arial 12", bg="sky blue", justify="center")
P1.insert(END, "75")
P1.place(x=150, y=60, width=50, height=30)

def s1_click(val):
    k1 = int(val) 
    x1 = float(P1.get())
    y1 = x1*k1
    var1.set(y1)
S1 = Scale(orient=HORIZONTAL, length=50, from_=0, to=10, command=s1_click)
S1.place(x=230, y=50)

var1 = StringVar()
C1 = Label(text=0, font="Arial 12", bg="deep sky blue", textvariable=var1)
C1.place(x=310, y=60, width=60, height=30)


# ----

lbl = Label(text="Морозиво", font="10", justify="left")
lbl.place(x=20, y=100, width=130, height=30)

P2 = Entry(font="Arial 12", bg="sky blue", justify="center")
P2.insert(END, "12")
P2.place(x=150, y=100, width=50, height=30)

def s2_click(val):
    k2 = int(val) 
    x2 = float(P2.get())
    y2 = x2*k2
    var2.set(y2)
S2 = Scale(orient=HORIZONTAL, length=50, from_=0, to=10, command=s2_click)
S2.place(x=230, y=90, width=50, height=40)

var2 = StringVar()
C2 = Label(text=0, font="Arial 12", bg="deep sky blue", textvariable=var2)
C2.place(x=310, y=100, width=60, height=30)

# ----

lbl = Label(text="Тістечко", font="10", justify="left")
lbl.place(x=20, y=140, width=130, height=30)

P3 = Entry(font="Arial 12", bg="sky blue", justify="center")
P3.insert(END, "16")
P3.place(x=150, y=140, width=50, height=30)

def s3_click(val):
    k3 = int(val) 
    x3 = float(P3.get())
    y3 = x3*k3
    var3.set(y3)
S3 = Scale(orient=HORIZONTAL, length=50, from_=0, to=10, command=s3_click)
S3.place(x=230, y=130, width=50, height=40)

var3 = StringVar()
C3 = Label(text=0, font="Arial 12", bg="deep sky blue", textvariable=var3)
C3.place(x=310, y=140, width=60, height=30)

# ----

lbl = Label(text="Сік", font="10", justify="left")
lbl.place(x=20, y=180, width=130, height=40)

P4 = Entry(font="Arial 12", bg="sky blue", justify="center")
P4.insert(END, "8")
P4.place(x=150, y=180, width=50, height=30)

def s4_click(val):
    k4 = int(val) 
    x4 = float(P4.get())
    y4 = x4*k4
    var4.set(y4)
S4 = Scale(orient=HORIZONTAL, length=50, from_=0, to=10, command=s4_click)
S4.place(x=230, y=170, width=50, height=40)

var4 = StringVar()
C4 = Label(text=0, font="Arial 12", bg="deep sky blue", textvariable=var4)
C4.place(x=310, y=180, width=60, height=30)

# -------

lbl = Label(text="Вартість замовлення", justify="left", font="10")
lbl.place(x=20, y=230, width=170, height=40)

var5 = StringVar()
C5 = Label(text=0, justify="center", bg="sky blue", font="Arial 12", textvariable=var5)
C5.place(x=190, y=235, width=60, height=30)

lbl = Label(text="грн.", justify="cente", font="10")
lbl.place(x=250, y=230, width=60, height=40)

def btn_click(val):
    print(val)
    var5.set("btn-click")

btn = Button(text="Розрахувати", justify="center", font=10, command=btn_click)
btn.place(x=310, y=230, width=120, height=40)

# ====




tk.mainloop()