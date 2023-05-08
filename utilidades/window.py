from tkinter import *
from PIL import Image, ImageTk

def btn_clicked():
    print("Button Clicked")


window = Tk()
window.resizable(False, False)


window.geometry("1950x1950")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

fundo =Image.open("background.png")
fundo.resize((1200, 1200), Image.ANTIALIAS)
fundo_bg = ImageTk.PhotoImage(fundo) 

background_img = fundo_bg
background = canvas.create_image(
    36.0, 42.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    -159.5, 8.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#cacaca",
    highlightthickness = 0)

entry0.place(
    x = -276.0, y = -31,
    width = 233.0,
    height = 77)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    191.0, 8.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#cacaca",
    highlightthickness = 0)

entry1.place(
    x = 25.0, y = -31,
    width = 332.0,
    height = 77)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = -45, y = 287,
    width = 172,
    height = 49)


window.mainloop()
