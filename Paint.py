from tkinter import * 
from tkinter import colorchooser

class Paint():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Paint")
        self.ventana.geometry("1100x600")
        self.ventana.resizable(0,0)
        
        stroke_size = IntVar()
        stroke_size.set(1)

        stroke_color = StringVar()
        stroke_color.set("black")

        frame1 = Frame(self.ventana, height=100, width=1100)
        frame1.grid(row=0, column=0, sticky= NW)

        toolsFrame = Frame(frame1 , height=100 , width=100, relief=SUNKEN, borderwidth=3)
        toolsFrame.grid(row=0 , column=0)
        
        def usePencil():
            stroke_color.set("black")
            canvas["cursor"] = "arrow"

        def useEraser():
            stroke_color.set("white")
            canvas["cursor"] = DOTBOX

        pencilButton = Button(toolsFrame , text="Pencil" , width=10, command=usePencil)
        pencilButton.grid(row=0 , column=0)

        eraserButton = Button(toolsFrame , text="Eraser" , width=10, command=useEraser)
        eraserButton.grid(row=1 , column=0)

        toolsLabel = Label(toolsFrame , text="Tools" , width=10)
        toolsLabel.grid(row=3 , column=0)

        sizeFrame = Frame(frame1 , height=100 , width=100, relief=SUNKEN, borderwidth=3)
        sizeFrame.grid(row=0 , column=1)

        defaultButton = Button(sizeFrame, text="Default" , width=10, command=usePencil)
        defaultButton.grid(row=0 , column=0)

        options = [1,2,3,4,5,10]

        sizeList = OptionMenu(sizeFrame, stroke_size, *options)
        sizeList.grid(row=1, column=0)

        sizeLabel = Label(sizeFrame , text="Size" , width=10)
        sizeLabel.grid(row=2 , column=0)

        colorBoxFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
        colorBoxFrame.grid(row=0, column=2)

        def selectColor():
            selectedColor = colorchooser.askcolor("blue", title="Select Color")
            print(selectedColor)

        colorBoxButton = Button(colorBoxFrame, text="Select Color", width=10, command=selectColor)
        colorBoxButton.grid(row=0, column=0)


        frame2 = Frame(self.ventana, height=500, width=1100, bg="light blue")
        frame2.grid(row=1, column=0)

        canvas = Canvas(frame2, height=500, width=1100, bg="white")
        canvas.grid(row=0, column=0)


        prevPoint = [0,0]
        currentPoint = [0,0]

        def paint(event):
            global prevPoint
            global currentPoint
            x = event.x
            y = event.y
            currentPoint = [x,y]
            #canvas.create_oval(x, y, x + 5, y + 5, fill="black")

            if prevPoint != [0,0] :
                canvas.create._polygon(prevPoint[0] , prevPoint[1] , currentPoint[0] , currentPoint[1], fill = stroke_color.get(), outline=stroke_color.et(), width=stroke_size.get())

            prevPoint = currentPoint

            if event.type == "5" :
                prevPoint = [0,0]

        canvas.bind("<B1-Motion>", paint)
        canvas.bind("<ButtonRelease-1>" , paint)

        self.ventana.mainloop()

app = Paint()