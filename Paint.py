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
        
        options = [1,2,3,4,5,10]

        stroke_size = IntVar()
        stroke_size.set(1)

        stroke_color = StringVar()
        stroke_color.set("black")

        previousColor = StringVar()
        previousColor.set("white")
        previousColor2 = StringVar()
        previousColor2.set("white")

        self.prevPoint = [0,0]
        self.currentPoint = [0,0]

        def usePencil():
            stroke_color.set("black")
            canvas["cursor"] = "arrow"

        def useEraser():
            stroke_color.set("white")
            canvas["cursor"] = DOTBOX

        def selectColor():
            selectedColor = colorchooser.askcolor("blue", title="Select Color")
            if selectedColor[1] == None :
             stroke_color.set("black")
            else:
             stroke_color.set(selectedColor[1])
             previousColor2.set(previousColor.get())
             previousColor.set(selectedColor[1])

             previousColorButton["bg"] = previousColor.get()
             previousColor2Button["bg"] = previousColor2.get()

        def paint(self, event, prevPoint, currentPoint):
            x = event.x
            y = event.y
            currentPoint = [x,y]
            #canvas.create_oval(x, y, x + 5, y + 5, fill="black")

            if prevPoint != [0,0] :
                canvas.create_polygon(prevPoint[0] , prevPoint[1] , currentPoint[0] , currentPoint[1], fill = stroke_color.get(), outline=stroke_color.get(), width=stroke_size.get())

            self.prevPoint = currentPoint

            if event.type == "5" :
                self.prevPoint = [0,0]
        
        def paintRight(event):
            x = event.x
            y = event.y
            canvas.create_arc(x,y,x+stroke_size.get(), y+stroke_size.get(), fill = stroke_color.get(), outline=stroke_color.get(), width=stroke_size.get())

        def saveImage():
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
            
        def clear():
            if messagebox.askokcancel("Paint" , "¿Quieres borrar todo?"):
                canvas.delete("all")

        def createNew():
            if messagebox.askyesno("Paint" , "¿Quieres guardar los cambios antes de borrar todo?"):
                clear()
        
        def help():
            messagebox.showinfo("Ayuda", "1. Click en el Boton Seleccionar Color para elegir un color especifico\n2. Click en el Boton Limpiar para limpiar el Lienzo")

        def settings():
            messagebox.showwarning("Configuracion", "No disponible" )
        
        def about():
            messagebox.showinfo("Acerca de", "Aplicacion de Pintura para estimular la creatividad de las personas")
            
        frame1 = Frame(self.ventana, height=100, width=1100)
        frame1.grid(row=0, column=0, sticky= NW)

        toolsFrame = Frame(frame1 , height=100 , width=100, relief=SUNKEN, borderwidth=3)
        toolsFrame.grid(row=0 , column=0)

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
        sizeList = OptionMenu(sizeFrame, stroke_size, *options)
        sizeList.grid(row=1, column=0)
        sizeLabel = Label(sizeFrame , text="Size" , width=10)
        sizeLabel.grid(row=2 , column=0)

        colorBoxFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
        colorBoxFrame.grid(row=0, column=2)

        colorBoxButton = Button(colorBoxFrame, text="Select Color", width=10, command=selectColor)
        colorBoxButton.grid(row=0, column=0)
        previousColorButton = Button(colorBoxFrame, text="Previous", width=10, command=lambda:stroke_color.set(previousColor.get()))
        previousColorButton.grid(row=1, column=0)
        previousColor2Button = Button(colorBoxFrame, text="Previous 2", width=10, command=lambda:stroke_color.set(previousColor2.get()))
        previousColor2Button.grid(row=2, column=0)

        colorsFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3,)
        colorsFrame.grid(row = 0 , column=3)

        redButton = Button(colorsFrame , text="Red" , bg="Red" , width=10 , command=lambda: stroke_color.set("red"))
        redButton.grid(row=0, column=0)
        greenButton = Button(colorsFrame , text="Green" , bg="Green" , width=10 , command=lambda: stroke_color.set("Green"))
        greenButton.grid(row=1, column=0)
        blueButton = Button(colorsFrame , text="Blue" , bg="Blue" , width=10 , command=lambda: stroke_color.set("Blue"))
        blueButton.grid(row=2 , column=0) 
        yellowButton = Button(colorsFrame , text="Yellow" , bg="yellow" , width=10 , command=lambda: stroke_color.set("yellow"))
        yellowButton.grid(row=0, column=1)
        orangeButton = Button(colorsFrame , text="Orange" , bg="orange" , width=10 , command=lambda: stroke_color.set("orange"))
        orangeButton.grid(row=1, column=1)
        purpleButton = Button(colorsFrame , text="Purple" , bg="purple" , width=10 , command=lambda: stroke_color.set("purple"))
        purpleButton.grid(row=2 , column=1)

        saveImageFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3,)
        saveImageFrame.grid(row = 0 , column=4)

        newImageButton = Button(saveImageFrame , text="New" , bg="white" , width=10 , command=createNew)
        newImageButton.grid(row=1 , column=0)

        clearImageButton = Button(saveImageFrame , text="Clear" , bg="white" , width=10 , command=clear)
        clearImageButton.grid(row=2 , column=0)

        saveImageButton = Button(saveImageFrame , text="Save" , bg="white" , width=10 , command=saveImage)
        saveImageButton.grid(row=0, column=0)

        helpSettingFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
        helpSettingFrame.grid(row=0, column=5)

        helpButton = Button(helpSettingFrame, text="Help", bg="white", width=10, command=help)
        helpButton.grid(row=0, column=0)

        settingButton = Button(helpSettingFrame, text="Settings", bg="white", width=10, command=settings)
        settingButton.grid(row=1, column=0)

        aboutButton = Button(helpSettingFrame, text="About", bg="white", width=10, command=about)
        aboutButton.grid(row=2, column=0)

        frame2 = Frame(self.ventana, height=500, width=1100, bg="light blue")
        frame2.grid(row=1, column=0)

        canvas = Canvas(frame2, height=500, width=1100, bg="white")
        canvas.grid(row=0, column=0)
        canvas.bind("<B1-Motion>", lambda event: paint(self, event, self.prevPoint, self.currentPoint))
        canvas.bind("<ButtonRelease-1>" , lambda event: paint(self, event, self.prevPoint, self.currentPoint))
        canvas.bind("<B3-Motion>", paintRight)

        self.ventana.mainloop()

app = Paint()