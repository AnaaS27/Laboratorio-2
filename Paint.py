from tkinter import * 
from tkinter import colorchooser
import PIL.ImageGrab as ImageGrab
from tkinter import filedialog
from tkinter import messagebox


class Paint():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Paint")
        self.ventana.geometry("1100x600")
        self.ventana.resizable(0,0)
        
        self.opciones = [1,2,3,4,5,10]

        self.tamatoTrazo = IntVar()
        self.tamatoTrazo.set(1)

        self.colorTrazo = StringVar()
        self.colorTrazo.set("black")

        self.previousColor = StringVar()
        self.previousColor.set("white")
        self.previousColor2 = StringVar()
        self.previousColor2.set("white")

        self.prevPoint = [0,0]
        self.currentPoint = [0,0]

        self.textValue = StringVar()

    def usePencil(self):
        self.colorTrazo.set("black")
        self.canvas["cursor"] = "arrow"

    def useEraser(self):
        self.colorTrazo.set("white")
        self.canvas["cursor"] = DOTBOX

    def selectColor(self):
        selectedColor = colorchooser.askcolor("blue", title="Select Color")
        if selectedColor[1] == None :
            self.colorTrazo.set("black")
        else:
            self.colorTrazo.set(selectedColor[1])
            self.previousColor2.set(self.previousColor.get())
            self.previousColor.set(selectedColor[1])

            self.previousColorButton["bg"] = self.previousColor.get()
            self.previousColor2Button["bg"] = self.previousColor2.get()

    def paint(self, event, prevPoint, currentPoint):
        x = event.x
        y = event.y
        currentPoint = [x,y]
        #self.canvas.create_oval(x, y, x + 5, y + 5, fill="black")

        if prevPoint != [0,0] :
            self.canvas.create_polygon(prevPoint[0] , prevPoint[1] , currentPoint[0] , currentPoint[1], fill = self.colorTrazo.get(), outline=self.colorTrazo.get(), width=self.tamatoTrazo.get())

        self.prevPoint = currentPoint

        if event.type == "5" :
            self.prevPoint = [0,0]
    
    def paintRight(self,event):
        x = event.x
        y = event.y
        self.canvas.create_arc(x,y,x+self.tamatoTrazo.get(), y+self.tamatoTrazo.get(), fill = self.colorTrazo.get(), outline=self.colorTrazo.get(), width=self.tamatoTrazo.get())

    def saveImage(self):
        try:
            filelocation = filedialog.asksaveasfilename(defaultextension = "jpg")
            x = self.ventana.winfo_rootx()
            y = self.ventana.winfo_rooty()+100
            img = ImageGrab.grab(bbox=(x,y,x+1100,y+500))
            img.save(filelocation)
            showImage = messagebox.askyesno("Paint" , "¿Desea abrir la Imagen?")
            if showImage:
                img.show()
        except Exception as e:
            messagebox.showinfo("Paint" , "Ocurrio un error")
        
    def clear(self):
        if messagebox.askokcancel("Paint" , "¿Quieres borrar todo?"):
            self.canvas.delete("all")

    def createNew(self):
        if messagebox.askyesno("Paint" , "¿Quieres guardar los cambios antes de borrar todo?"):
            self.clear()
    
    def help():
        messagebox.showinfo("Ayuda", "1. Click en el Boton Seleccionar Color para elegir un color especifico\n2. Click en el Boton Limpiar para limpiar el Lienzo")

    def settings():
        messagebox.showwarning("Configuracion", "No disponible" )
    
    def about():
        messagebox.showinfo("Acerca de", "Aplicacion de Pintura para estimular la creatividad de las personas")

    def writeText(self, event):
        self.canvas.create_text(event.x, event.y, text=self.textValue.get())

    def principal(self):
        frame1 = Frame(self.ventana, height=100, width=1100)
        frame1.grid(row=0, column=0, sticky= NW)

        toolsFrame = Frame(frame1 , height=100 , width=100, relief=SUNKEN, borderwidth=3)
        toolsFrame.grid(row=0 , column=0)

        pencilButton = Button(toolsFrame , text="Pencil" , width=10, command=self.usePencil)
        pencilButton.grid(row=0 , column=0)
        eraserButton = Button(toolsFrame , text="Eraser" , width=10, command=self.useEraser)
        eraserButton.grid(row=1 , column=0)
        toolsLabel = Label(toolsFrame , text="Tools" , width=10)
        toolsLabel.grid(row=3 , column=0)

        sizeFrame = Frame(frame1 , height=100 , width=100, relief=SUNKEN, borderwidth=3)
        sizeFrame.grid(row=0 , column=1)

        defaultButton = Button(sizeFrame, text="Default" , width=10, command=self.usePencil)
        defaultButton.grid(row=0 , column=0)
        sizeList = OptionMenu(sizeFrame, self.tamatoTrazo, *self.opciones)
        sizeList.grid(row=1, column=0)
        sizeLabel = Label(sizeFrame , text="Size" , width=10)
        sizeLabel.grid(row=2 , column=0)

        colorBoxFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
        colorBoxFrame.grid(row=0, column=2)

        colorBoxButton = Button(colorBoxFrame, text="Select Color", width=10, command=self.selectColor)
        colorBoxButton.grid(row=0, column=0)
        self.previousColorButton = Button(colorBoxFrame, text="self.previous", width=10, command=lambda:self.colorTrazo.set(self.previousColor.get()))
        self.previousColorButton.grid(row=1, column=0)
        self.previousColor2Button = Button(colorBoxFrame, text="self.previous 2", width=10, command=lambda:self.colorTrazo.set(self.previousColor2.get()))
        self.previousColor2Button.grid(row=2, column=0)

        colorsFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3,)
        colorsFrame.grid(row = 0 , column=3)

        redButton = Button(colorsFrame , text="Red" , bg="Red" , width=10 , command=lambda: self.colorTrazo.set("red"))
        redButton.grid(row=0, column=0)
        greenButton = Button(colorsFrame , text="Green" , bg="Green" , width=10 , command=lambda: self.colorTrazo.set("Green"))
        greenButton.grid(row=1, column=0)
        blueButton = Button(colorsFrame , text="Blue" , bg="Blue" , width=10 , command=lambda: self.colorTrazo.set("Blue"))
        blueButton.grid(row=2 , column=0) 
        yellowButton = Button(colorsFrame , text="Yellow" , bg="yellow" , width=10 , command=lambda: self.colorTrazo.set("yellow"))
        yellowButton.grid(row=0, column=1)
        orangeButton = Button(colorsFrame , text="Orange" , bg="orange" , width=10 , command=lambda: self.colorTrazo.set("orange"))
        orangeButton.grid(row=1, column=1)
        purpleButton = Button(colorsFrame , text="Purple" , bg="purple" , width=10 , command=lambda: self.colorTrazo.set("purple"))
        purpleButton.grid(row=2 , column=1)

        saveImageFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3,)
        saveImageFrame.grid(row = 0 , column=4)

        newImageButton = Button(saveImageFrame , text="New" , bg="white" , width=10 , command=self.createNew)
        newImageButton.grid(row=1 , column=0)

        clearImageButton = Button(saveImageFrame , text="Clear" , bg="white" , width=10 , command=self.clear)
        clearImageButton.grid(row=2 , column=0)

        saveImageButton = Button(saveImageFrame , text="Save" , bg="white" , width=10 , command=self.saveImage)
        saveImageButton.grid(row=0, column=0)

        helpSettingFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
        helpSettingFrame.grid(row=0, column=5)
        
        helpButton = Button(helpSettingFrame, text="Help", bg="white", width=10, command=help)
        helpButton.grid(row=0, column=0)
        settingButton = Button(helpSettingFrame, text="Settings", bg="white", width=10, command=self.settings)
        settingButton.grid(row=1, column=0)
        aboutButton = Button(helpSettingFrame, text="About", bg="white", width=10, command=self.about)
        aboutButton.grid(row=2, column=0)


        textFrame = Frame(frame1, height=100, width=200, relief=SUNKEN, borderwidth=3)
        textFrame.grid(row=0, column=6)

        textTitleButton = Label(textFrame, text="Write you text here:", bg="white", width=20 )
        textTitleButton.grid(row=0, column=0)
        entryButton = Entry(textFrame, textvariable=self.textValue, bg="white", width=20 )
        entryButton.grid(row=1, column=0)
        clearButton = Button(textFrame, text="Clear", bg="white", width=20, command=lambda:self.textValue.set(""))
        clearButton.grid(row=2, column=0)

        noteFrame = Frame(frame1 ,  height=100 , width=200 , relief=SUNKEN , borderwidth=3)
        noteFrame.grid(row = 0 , column = 7)

        textTitleButton = Text(noteFrame, bg="white", width=40, height=4 )
        textTitleButton.grid(row=0, column=0)
        #entryButton = Entry(textFrame, textvariable=self.textValue, bg="white", width=20 )
        #entryButton.grid(row=1, column=0)
        #clearButton = Button(textFrame, text="Clear", bg="white", width=20, command=lambda:self.textValue.set(""))
        #clearButton.grid(row=2, column=0)



        frame2 = Frame(self.ventana, height=500, width=1100, bg="light blue")
        frame2.grid(row=1, column=0)

        self.canvas = Canvas(frame2, height=500, width=1100, bg="white")
        self.canvas.grid(row=0, column=0)
        self.canvas.bind("<B1-Motion>", lambda event: self.paint(self, event, self.prevPoint, self.currentPoint))
        self.canvas.bind("<ButtonRelease-1>" , lambda event: self.paint(self, event, self.prevPoint, self.currentPoint))
        self.canvas.bind("<B3-Motion>", self.paintRight)
        self.canvas.bind("<Button-1>", self.writeText)

        self.ventana.mainloop()

app = Paint()