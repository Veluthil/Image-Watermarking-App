import tkinter.messagebox
from tkinter import *
import PIL
from PIL import Image, ImageDraw, ImageFont, ImageTk

save_route = "D:/Photos/WatermarkApp/"
IMG = None
OPACITY = 255
FONT_SIZE = 50
UP_DOWN = 0
LEFT_RIGHT = 0


def show_image():
    if len(file_entry.get()) != 0:
        img = (Image.open(file_entry.get().replace('"', '')))
        r_img = resize(img)
        panel.configure(image=r_img)
        panel.image = r_img
    else:
        tkinter.messagebox.showerror("Error", "You have to provide a file path to continue.")


def resize(img):
    size = img.size
    f_size = (700, 600)
    factor = min(float(f_size[1]) / size[1], float(f_size[0]) / size[0])
    width = int(size[0] * factor)
    height = int(size[1] * factor)
    r_img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(r_img)


def create_watermark():
    try:
        with Image.open(file_entry.get().replace('"', '')).convert("RGBA") as base:
            # make a blank image for the text, initialized to transparent text color
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
            height, width = base.size[0], base.size[1] - 100
            # get a font
            fnt = ImageFont.truetype("arial.ttf", FONT_SIZE)
            # get a drawing context
            d = ImageDraw.Draw(txt)
            # draw text
            d.text((10, width), f"{wmark_entry.get()}", font=fnt, fill=(255, 255, 255, OPACITY))

            out = Image.alpha_composite(base, txt)
            marked_img = out.convert("RGBA")
            w_img = resize(marked_img)
            panel.configure(image=w_img)
            panel.image = w_img
    except FileNotFoundError:
        tkinter.messagebox.showerror("Error", "No such file.")
    except PIL.UnidentifiedImageError:
        tkinter.messagebox.showerror("Error", "Wrong file extension.")
    global IMG
    IMG = marked_img


def opacity(value):
    global OPACITY
    OPACITY = int(value)


def font_size():
    global FONT_SIZE
    FONT_SIZE = int(font_size.get())


def up_down(value):
    global UP_DOWN
    UP_DOWN = int(value)


def left_right(value):
    global LEFT_RIGHT
    LEFT_RIGHT = int(value)


def save(marked_img):
    file_name = name_entry.get()
    clean_save_route = save_route.replace('"', '')
    answer = tkinter.messagebox.askyesno("Procced", "Do you want to save?")
    with open("data.txt", mode="r") as file:
        names = file.read()
        if file_name not in names:
            if answer:
                with open("data.txt", mode="a") as file:
                    file.write(f"{file_name}\n")
                marked_img.save(f"{clean_save_route}/{file_name}.bmp")
                tkinter.messagebox.showinfo("Success", f"Image got watermarked and saved to"
                                                       f" {save_route}{file_name}.bmp.")
        elif file_name == "":
            tkinter.messagebox.showerror("Error", "Error: You have to provide a file name.")
        else:
            tkinter.messagebox.showerror("Error", f'You have already saved an image with "{file_name}" '
                                                  'name. Try something else.')


# ------------ Creating a GUI -------------------
window = Tk()
window.title("Image Watermarking App")
window.minsize(height=100, width=500)
window.config(padx=20, pady=20, bg="#000000")

blank_photo = Image.new(mode="RGBA", size=(700, 600), color="#696969")
image1 = ImageTk.PhotoImage(blank_photo)
panel = Label(window, image=image1)
panel.image = image1 #keep a reference
panel.grid(column=0, rowspan=10)

label = Label(text="Image full file path:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
label.grid(column=1, row=0)
file_entry = Entry(width=60)
file_entry.grid(column=2, row=0, columnspan=5)
file_entry.get()

show = Button(text="Show", bg="#000000", fg="#fafafa", command=show_image)
show.grid(column=7, row=0)

wmark = Label(text="Watermark text:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
wmark.grid(column=1, row=2)
wmark_entry = Entry(width=60)
wmark_entry.grid(column=2, row=2, columnspan=5)
wmark_entry.get()

opacity_label = Label(text="Opacity", bg="#000000", fg="#fafafa", font=("Arial", 8))
opacity_label.grid(column=1, row=3)
opacity = Scale(window, from_=0, to=255, orient="horizontal", bg="#000000", fg="#fafafa", command=opacity)
opacity.set(255)
opacity.grid(column=1, row=4, ipadx=20)

font_label = Label(text="Font size", bg="#000000", fg="#fafafa", font=("Arial", 8))
font_label.grid(column=2, row=3)
default_font_size = StringVar(window)
default_font_size.set("50")
font_size = Spinbox(window, from_=1, to=200, width=5, textvariable=default_font_size, command=font_size)
font_size.grid(column=2, row=4)

up_down_label = Label(text="Up/Down", bg="#000000", fg="#fafafa", font=("Arial", 8))
up_down_label.grid(column=3, row=3)
up_down = Scale(window, from_=0, to=255, bg="#000000", fg="#fafafa", command=up_down)
up_down.grid(column=3, row=4)

left_right_label = Label(text="Left/Right", bg="#000000", fg="#fafafa", font=("Arial", 8))
left_right_label.grid(column=4, row=3)
left_right = Scale(window, from_=0, to=255, orient="horizontal", bg="#000000", fg="#fafafa", command=left_right)
left_right.grid(column=4, row=4)

show_wm = Button(text="Show", bg="#000000", fg="#fafafa", command=create_watermark)
show_wm.grid(column=7, row=2)

name = Label(text="Watermarked image file name:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
name.grid(column=1, row=6)
name_entry = Entry(width=40)
name_entry.grid(column=2, row=6, columnspan=3)
name_entry.get()

save_img = Button(text="Save", bg="#000000", fg="#fafafa", command=lambda: save(IMG))
save_img.grid(column=6, row=6)

window.mainloop()
