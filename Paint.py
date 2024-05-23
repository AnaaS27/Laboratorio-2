from tkinter import * 

class Paint():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Paint")
        self.ventana.geometry("1100x600")
        self.ventana.resizable(0,0)

        frame1 = Frame(self.ventana, height=100, width=1100, bg="light gray")
        frame1.grid(row=0, column=0, sticky= NW)

        toolsFrame = Frame(frame1 , height=100 , width=100 , bg="green")
        toolsFrame.grid(row=0 , column=0)

        pencilButton = Button(toolsFrame , text="Pencil" , width=10)
        pencilButton.grid(row=0 , column=0)

        eraserButton = Button(toolsFrame , text="Eraser" , width=10)
        eraserButton.grid(row=1 , column=0)

        toolsLabel = Label(toolsFrame , text="Tools" , width=10)
        toolsLabel.grid(row=2 , column=0)

        frame2 = Frame(self.ventana, height=100, width=1100, bg="light blue")
        frame2.grid(row=1, column=0)

        canvas = Canvas(frame2, height=500, width=1100, bg="white")
        canvas.grid(row=0, column=0)

        prevpoint =[0,0]
        currentpoint = [0,0]

        def paint(event):
            print(event.type)
            global prevpoint
            global currentpoint
            x = event.x
            y = event.y
            currentpoint = [x,y]
            canvas.create_oval(x, y, x + 5, y + 5, fill="black")

            if prevpoint != [0,0]:
                canvas.create_line(prevpoint[0] , prevpoint[1] , currentpoint[0] , currentpoint[1])

            prevpoint = currentpoint

            if event.type == "5" :
                prevpoint = [0,0]

        canvas.bind("<B1-Motion>", paint)
        canvas.bind("<ButtonRelease-1>" , paint)

        self.ventana.mainloop()

app = Paint()