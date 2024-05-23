from tkinter import * 

class Paint():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Paint")
        self.ventana.geometry("1100x600")
        self.ventana.resizable(0,0)

        frame1 = Frame(self.ventana, height=100, width=1100, bg="light gray")
        frame1.grid(row=0, column=0)

        frame2 = Frame(self.ventana, height=100, width=1100, bg="light blue")
        frame2.grid(row=1, column=0)
        canvas = Canvas(frame2, height=500, width=1100, bg="white")
        canvas.grid(row=0, column=0)

    def paint(event):
        x = event.x
        y = event.y
        canvas.create_oval(x, y, x + 20, y + 20, fill="black")

        canvas.bind("<B1-Motion>", paint)

        self.ventana.mainloop()

app = Paint()