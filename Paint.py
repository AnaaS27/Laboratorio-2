from tkinter import * 
from tkinter import colorchooser
import PIL.ImageGrab as ImageGrab
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import math
from Tooltip import Tooltip


class Paint():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Paint")
        self.ventana.geometry("1100x600")
        self.ventana.resizable(0,0)
        
        self.opciones = [1,2,3,4,5,10,20,30,40,50,60,70,80,90,100]

        self.tamañoTrazo = IntVar()
        self.tamañoTrazo.set(5)

        self.colorTrazo = StringVar()
        self.colorTrazo.set("black")

        self.previousColor = StringVar()
        self.previousColor.set("white")
        self.previousColor2 = StringVar()
        self.previousColor2.set("white")

        self.prevPoint = [0,0]
        self.currentPoint = [0,0]

        self.formas_var = StringVar()
        self.formas_var.set("Figuras")

        self.forma = None

        self.forma_start_x = None
        self.forma_start_y = None

        self.previous_x = None
        self.previous_y = None

        self.actions = []

        self.selected_item = None
        self.prev_x = None
        self.prev_y = None
        self.image_id = None

        self.image_moving = False

        self.textValue = StringVar()

        self.principal()

    def principal(self):
        frame1 = Frame(self.ventana, height=100, width=1100)
        frame1.grid(row=0, column=0, sticky= NW)

        toolsFrame = Frame(frame1 , height=100 , width=100, relief=SUNKEN, borderwidth=3)
        toolsFrame.grid(row=0 , column=0)

        pencilIcon = tk.PhotoImage(file=r"icons\pencil.png")
        pencilButton = Button(toolsFrame , text="Lapiz" , bg="white", width=65,  image=pencilIcon, compound=LEFT, command=self.usePencil)
        pencilButton.grid(row=0 , column=0)
        Tooltip(pencilButton, "Presione para Dibujar")

        eraserIcon = tk.PhotoImage(file=r"icons\borrador.png")
        eraserButton = Button(toolsFrame , text="Borrador" , bg="white", width=65, command=self.useEraser, image=eraserIcon, compound=LEFT)
        eraserButton.grid(row=1 , column=0)
        Tooltip(eraserButton, "Presione para borrar")

        toolsLabel = Label(toolsFrame , text="Herramientas" , width=9)
        toolsLabel.grid(row=4 , column=0)

        sizeFrame = Frame(frame1 , height=100 , width=100, relief=SUNKEN, borderwidth=3)
        sizeFrame.grid(row=0 , column=1)

        defaultButton = Button(sizeFrame, text="Por Defecto" , bg="white", width=10, command=self.usePencil)
        defaultButton.grid(row=0 , column=0)
        Tooltip(defaultButton, "Opcion predeterminada")

        sizeList = OptionMenu(sizeFrame, self.tamañoTrazo, *self.opciones)
        sizeList.grid(row=1, column=0)

        sizeLabel = Label(sizeFrame , text="Tamaño" , width=10)
        sizeLabel.grid(row=2 , column=0)

        colorBoxFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
        colorBoxFrame.grid(row=0, column=2)

        paletaIcon = tk.PhotoImage(file=r"icons\palette.png")
        colorBoxButton = Button(colorBoxFrame, text="Seleccionar Color", bg="white", width=115, command=self.selectColor, image=paletaIcon, compound=LEFT)
        colorBoxButton.grid(row=0, column=0)

        anteriorIcon = tk.PhotoImage(file=r"icons\anterior.png")
        self.previousColorButton = Button(colorBoxFrame, text="Color Anterior", bg="white", width=115, command=lambda:self.colorTrazo.set(self.previousColor.get()), image=anteriorIcon, compound=LEFT)
        self.previousColorButton.grid(row=1, column=0)

        self.previousColor2Button = Button(colorBoxFrame, text="Color Anterior 2", bg="white", width=115, command=lambda:self.colorTrazo.set(self.previousColor2.get()), image=anteriorIcon, compound=LEFT)
        self.previousColor2Button.grid(row=2, column=0)

        coloresLabel = Label(colorBoxFrame, text="Colores", width=10)
        coloresLabel.grid(row=4, column=0)

        colorsFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3,)
        colorsFrame.grid(row = 0 , column=3)

        redButton = Button(colorsFrame , bg="Red" , width=3 , command=lambda: self.colorTrazo.set("red"))
        redButton.grid(row=0, column=0)
        Tooltip(redButton, "Color Rojo")
        greenButton = Button(colorsFrame , bg="Green" , width=3 , command=lambda: self.colorTrazo.set("Green"))
        greenButton.grid(row=1, column=0)
        Tooltip(greenButton, "Color Verde")
        blueButton = Button(colorsFrame , bg="Blue" , width=3 , command=lambda: self.colorTrazo.set("Blue"))
        blueButton.grid(row=2 , column=0) 
        Tooltip(blueButton, "Color Azul")
        yellowButton = Button(colorsFrame , bg="yellow" , width=3 , command=lambda: self.colorTrazo.set("yellow"))
        yellowButton.grid(row=0, column=1)
        Tooltip(yellowButton, "Color Amarillo")
        orangeButton = Button(colorsFrame , bg="orange" , width=3 , command=lambda: self.colorTrazo.set("orange"))
        orangeButton.grid(row=1, column=1)
        Tooltip(orangeButton, "Color Naranja")
        purpleButton = Button(colorsFrame , bg="purple" , width=3 , command=lambda: self.colorTrazo.set("purple"))
        purpleButton.grid(row=2 , column=1)
        Tooltip(purpleButton, "Color Purpura")

        saveImageFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3,)
        saveImageFrame.grid(row = 0 , column=4)

        nuevoIcon = tk.PhotoImage(file=r"icons\new.png")
        newImageButton = Button(saveImageFrame , text="Nuevo" , bg="white" , width=80, height=20, command=self.createNew, image=nuevoIcon)
        newImageButton.grid(row=1 , column=0)
        Tooltip(newImageButton, "Presione para crear un nuevo lienzo")
        newImageButton.bind("<Control-n>", self.createNew)

        limpiarIcon = tk.PhotoImage(file=r"icons\limpiar.png")
        clearImageButton = Button(saveImageFrame , text="Limpiar" , bg="white" , width=80 , command=self.clear, image=limpiarIcon, compound=LEFT)
        clearImageButton.grid(row=2 , column=0)
        Tooltip(clearImageButton, "Presione Para Limpiar Lienzo")
        clearImageButton.bind("<Control-l>", self.clear)

        guardarIcon = tk.PhotoImage(file=r"icons\guardar.png")
        saveImageButton = Button(saveImageFrame , text="Guardar" , bg="white" , width=80, command=self.saveImage, image=guardarIcon, compound=LEFT)
        saveImageButton.grid(row=0, column=0)
        Tooltip(saveImageButton, "Presione Para Guardar Imagen")
        saveImageButton.bind("<Control-N>", self.saveImage)

        helpSettingFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
        helpSettingFrame.grid(row=0, column=5)

        ayudaIcon = tk.PhotoImage(file=r"icons\help.png")   
        helpButton = Button(helpSettingFrame, text="Ayuda", bg="white", width=80, command=help, image=ayudaIcon, compound=LEFT)
        helpButton.grid(row=1, column=0)
        Tooltip(helpButton, "Ayuda")
        helpButton.bind("<Control-a>", self.help)
        
        deshacerIcon = tk.PhotoImage(file=r"icons\deshacer.png")
        undoButton = Button(helpSettingFrame, text="Deshacer", bg="white", width=80, command=self.undo, image=deshacerIcon, compound=LEFT)
        undoButton.grid(row=0, column=0)
        Tooltip(undoButton, "Presione el Boton Para Deshacer")
        undoButton.bind("Control-d", self.undo)

        infoIcon = tk.PhotoImage(file=r"icons\information.png")
        aboutButton = Button(helpSettingFrame, text="Acerca De", bg="white", width=80, command=self.about, image=infoIcon, compound=LEFT)
        aboutButton.grid(row=2, column=0)
        Tooltip(aboutButton, "Acerca de")
        aboutButton.bind("<Control-i>", self.about)


        textFrame = Frame(frame1, height=100, width=200, relief=SUNKEN, borderwidth=3)
        textFrame.grid(row=0, column=6)

        textTitleButton = Label(textFrame, text="Escriba su texto aqui:", bg="white", width=20 )
        textTitleButton.grid(row=0, column=0)
        Tooltip(textTitleButton, "Escriba su Texto Aqui")
        entryButton = Entry(textFrame, textvariable=self.textValue, bg="white", width=20 )
        entryButton.grid(row=1, column=0)
        clearButton = Button(textFrame, text="Limpiar", bg="white", width=80, command=lambda:self.textValue.set(""), image=limpiarIcon, compound=LEFT)
        clearButton.grid(row=2, column=0)
        Tooltip(clearButton, "Presione Para Ingresar el Texto Limpiar")

        imagenesIcon = tk.PhotoImage(file=r"icons\pictures.png")
        importFrame = Frame(frame1, height=100, width=200, relief=SUNKEN, borderwidth=3)
        importFrame.grid(row=0, column=8)
        importImageButton = Button(importFrame, text="Insertar Imagen", bg="white", width=100, command=self.import_image, image=imagenesIcon, compound=LEFT)
        importImageButton.grid(row=3, column=0)
        Tooltip(importImageButton, "Presione para buscar\nuna imagen e insertar")
        importImageButton.bind("<Control-t>", self.import_image)

        noteFrame = Frame(frame1 ,  height=100 , width=150 , relief=SUNKEN , borderwidth=3)
        noteFrame.grid(row = 0 , column = 7)

        textTitleButton = Text(noteFrame, bg="white", width=32, height=4 )
        textTitleButton.grid(row=0, column=0) 
        Tooltip(textTitleButton, "Ingrese su Texto")

        self.create_menu(toolsFrame)

        frame2 = Frame(self.ventana, height=500, width=1100, bg="light blue")
        frame2.grid(row=1, column=0)

        self.canvas = Canvas(frame2, height=500, width=1100, bg="white")
        self.canvas.grid(row=0, column=0)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>" , self.reset)
        self.canvas.bind("<B3-Motion>", self.paintRight)
        self.canvas.bind("<Button-1>", self.writeText)
        self.canvas.bind("<ButtonPress-2>", self.start_forma)
        self.canvas.bind("<B2-Motion>", self.draw_forma)
        self.canvas.bind("<ButtonRelease-2>", self.finalize_forma)
        self.canvas.bind("<Double-Button-1>", self.controlImagen)

        self.ventana.mainloop()

    def create_menu(self, toolsFrame):
        formas = ["Linea", "Rectángulo", "Óvalo", "Poligono"]
        formas_menu = OptionMenu(toolsFrame, self.formas_var, *formas, command=self.select_forma)
        formas_menu.grid(row=3, column=0)

    def usePencil(self):
        self.colorTrazo.set("black")
        self.canvas["cursor"] = "arrow"

    def useEraser(self):
        self.colorTrazo.set("white")
        self.canvas["cursor"] = DOTBOX

    def useLine(self):
        self.forma = "line"
        self.canvas["cursor"] = "crosshair"

    def useRectangle(self):
        self.forma = "rectangle"
        self.canvas["cursor"] = "crosshair"

    def useOval(self):
        self.forma = "oval"
        self.canvas["cursor"] = "crosshair"

    def usePolygon(self):
        self.forma= "polygon"
        self.canvas["cursor"] = "crosshair"

    def start_forma(self, event):
        self.forma_start_x = event.x
        self.forma_start_y = event.y

    def select_forma(self, forma):
        if forma == "Linea":
            self.useLine()
        elif forma == "Rectángulo":
            self.useRectangle()
        elif forma == "Óvalo":
            self.useOval()
        elif forma == "Poligono":
            self.usePolygon()

    def draw_forma(self, event):
        if self.forma:
            if self.forma_start_x and self.forma_start_y:
                self.canvas.delete("preview")
                if self.forma == "line":
                    self.canvas.create_line(self.forma_start_x, self.forma_start_y, event.x, event.y, fill=self.colorTrazo.get(), width=self.tamañoTrazo.get(), tags="preview")
                elif self.forma == "rectangle":
                    self.canvas.create_rectangle(self.forma_start_x, self.forma_start_y, event.x, event.y, outline=self.colorTrazo.get(), width=self.tamañoTrazo.get(), tags="preview")
                elif self.forma == "oval":
                    self.canvas.create_oval(self.forma_start_x, self.forma_start_y, event.x, event.y, outline=self.colorTrazo.get(), width=self.tamañoTrazo.get(), tags="preview")
                elif self.forma == "polygon":
                    if self.forma_start_x and self.forma_start_y:
                        num_vertices = 5
                        angle_increment = 360 / num_vertices
                        radius = math.sqrt((event.x - self.forma_start_x)**2 + (event.y - self.forma_start_y)**2)
                        points = []
                        for i in range(num_vertices):
                            angle = math.radians(i * angle_increment)
                            x = self.forma_start_x + radius * math.cos(angle)
                            y = self.forma_start_y + radius * math.sin(angle)
                            points.extend([x, y])
                        self.canvas.create_polygon(points, fill="", outline=self.colorTrazo.get(), width=self.tamañoTrazo.get(), tags="preview")

    def finalize_forma(self, event):
        if self.forma:
            self.canvas.delete("preview")
            if self.forma_start_x and self.forma_start_y:
                if self.forma:
                    if self.forma == "line":
                        self.actions.append(self.canvas.create_line(self.forma_start_x, self.forma_start_y, event.x, event.y, fill=self.colorTrazo.get(), width=self.tamañoTrazo.get()))
                    elif self.forma == "rectangle":
                        self.actions.append(self.canvas.create_rectangle(self.forma_start_x, self.forma_start_y, event.x, event.y, outline=self.colorTrazo.get(), width=self.tamañoTrazo.get()))
                    elif self.forma == "oval":
                        self.actions.append(self.canvas.create_oval(self.forma_start_x, self.forma_start_y, event.x, event.y, outline=self.colorTrazo.get(), width=self.tamañoTrazo.get()))
                    elif self.forma == "polygon":
                        if self.forma_start_x and self.forma_start_y:
                            num_vertices = 5
                            angle_increment = 360 / num_vertices
                            radius = math.sqrt((event.x - self.forma_start_x)**2 + (event.y - self.forma_start_y)**2)
                            points = []
                            for i in range(num_vertices):
                                angle = math.radians(i * angle_increment)
                                x = self.forma_start_x + radius * math.cos(angle)
                                y = self.forma_start_y + radius * math.sin(angle)
                                points.extend([x, y])
                            self.actions.append(self.canvas.create_polygon(points, fill="", outline=self.colorTrazo.get(), width=self.tamañoTrazo.get()))
            self.forma_start_x, self.forma_start_y = None, None

    def selectColor(self):
        selectedColor = colorchooser.askcolor("blue", title="Seleccionar Color")
        if selectedColor[1] == None :
            self.colorTrazo.set("black")
        else:
            self.colorTrazo.set(selectedColor[1])
            self.previousColor2.set(self.previousColor.get())
            self.previousColor.set(selectedColor[1])

            self.previousColorButton["bg"] = self.previousColor.get()
            self.previousColor2Button["bg"] = self.previousColor2.get()

    def paint(self, event):
            if not self.image_moving:
                x = event.x
                y = event.y
                self.currentPoint = [x, y]

                if self.prevPoint != [0, 0]:
                    self.actions.append(self.canvas.create_line(self.prevPoint[0], self.prevPoint[1], self.currentPoint[0], self.currentPoint[1],
                                            fill=self.colorTrazo.get(), width=self.tamañoTrazo.get()))

                self.prevPoint = self.currentPoint
    
    def paintRight(self,event):
        if not self.image_moving:
            x = event.x
            y = event.y
            self.actions.append(self.canvas.create_arc(x,y,x+self.tamañoTrazo.get(), y+self.tamañoTrazo.get(), fill = self.colorTrazo.get(), outline=self.colorTrazo.get(), width=self.tamañoTrazo.get()))

    def reset(self, event):
        self.prevPoint = [0, 0]
    
    def saveImage(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension=".png")
            print(f"Guardar Imagen {filename}")
            x = self.ventana.winfo_rootx()
            y = self.ventana.winfo_rooty()+ 100
            imagen = ImageGrab.grab().crop((x, y, x+1100, y+500))
            imagen.save(filename)
            messagebox.showinfo("Paint", "La imagen se guardo como" + str(filename))
            showImage = messagebox.askyesno("Paint", "¿Desea abrir la imagen?")
            if showImage:
                imagen.show()
        except:
            messagebox.showerror("Paint", "¡¡La imagen no se guardo. Intente de nuevo!!")
    
    def undo(self):
        if len(self.actions) > 0:
            self.canvas.delete(self.actions.pop())
        else:
            messagebox.showwarning("Advertencia", "No hay más acciones para deshacer")
        
    def clear(self):
        if messagebox.askokcancel("Paint" , "¿Quieres borrar todo?"):
            self.canvas.delete(ALL)
            self.actions = []

    def createNew(self):
        respuesta = messagebox.askyesno("Nuevo", "¿Quieres guardar el Lienzo actual?")
        if respuesta == True:
            self.saveImage()
        self.canvas.delete(ALL)
        self.actions = []

    def help():
        messagebox.showinfo("Ayuda", "1. Click en el Boton Seleccionar Color para elegir un color especifico\n2. Click en el Boton Limpiar para limpiar el Lienzo")
    
    def about():
        messagebox.showinfo("Acerca de", "Aplicacion de Pintura para estimular la creatividad de las personas")

    def writeText(self, event):
        if not self.image_moving:
            x = event.x
            y = event.y
            self.actions.append(self.canvas.create_text(x, y, fill=self.colorTrazo.get(), font=("Arial", 20), text=self.textValue.get()))
            self.textValue.set("")
    
    def import_image(self):
        image_path = filedialog.askopenfilename()
        if image_path:
            img = Image.open(image_path)
            self.img = ImageTk.PhotoImage(img)
            self.image_id = self.canvas.create_image(0, 0, anchor=NW, image=self.img)
            self.canvas.tag_bind(self.image_id, "<ButtonPress-1>", self.imagen_click)
            self.canvas.tag_bind(self.image_id, "<B1-Motion>", self.ArrastrarImagen)
            self.actions.append(self.image_id)
            messagebox.showinfo("Advertencia", "Para volver a pintar, haga doble clic en el lienzo\nY al mover la imagen repita la misma accion")

    def imagen_click(self, event):
        self.prev_x = event.x
        self.prev_y = event.y
        self.image_moving = True

    def ArrastrarImagen(self, event):
        if self.image_moving:
            dx = event.x - self.prev_x
            dy = event.y - self.prev_y
            self.canvas.move(self.image_id, dx, dy)
            self.prev_x = event.x
            self.prev_y = event.y
        else:
            self.paint()
            self.paintRight()

    def controlImagen(self, event):
        self.image_moving = False
    

app = Paint()