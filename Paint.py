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
            if selectedColor[1] == None :
             stroke_color.set("black")
            else:
             stroke_color.set(selectedColor[1])
            print(selectedColor)

        colorBoxButton = Button(colorBoxFrame, text="Select Color", width=10, command=selectColor)
        colorBoxButton.grid(row=0, column=0)

        colorsFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3,)
        colorsFrame.grid(row = 0 , column=3)

        redButton = Button(colorsFrame , text="Red" , bg="Red" , width=10 , command=lambda: stroke_color.set("red"))
        redButton.grid(row=0, column=0)

        greenButton = Button(colorsFrame , text="Green" , bg="Green" , width=10 , command=lambda: stroke_color.set("Green"))
        greenButton.grid(row=1, column=0)

        blueButton = Button(colorsFrame , text="Blue" , bg="Blue" , width=10 , command=lambda: stroke_color.set("Blue"))
        blueButton.grid(row=2 , column=0) 


        frame2 = Frame(self.ventana, height=500, width=1100, bg="light blue")
        frame2.grid(row=1, column=0)

        canvas = Canvas(frame2, height=500, width=1100, bg="white")
        canvas.grid(row=0, column=0)

        self.prevPoint = [0,0]
        self.currentPoint = [0,0]

        def paint(self, event, prevPoint, currentPoint):
            x = event.x
            y = event.y
            self.currentPoint = [x,y]
            #canvas.create_oval(x, y, x + 5, y + 5, fill="black")

            if prevPoint != [0,0] :
                canvas.create_polygon(prevPoint[0] , prevPoint[1] , self.currentPoint[0] , self.currentPoint[1], fill = stroke_color.get(), outline=stroke_color.get(), width=stroke_size.get())

            self.prevPoint = self.currentPoint

            if event.type == "5" :
                self.prevPoint = [0,0]

        canvas.bind("<B1-Motion>", lambda event: paint(self, event, self.prevPoint, self.currentPoint))
        canvas.bind("<ButtonRelease-1>" , lambda event: paint(self, event, self.prevPoint, self.currentPoint))

        self.ventana.mainloop()

app = Paint()