import tkinter.messagebox
from tkinter import *
from tkinter import filedialog as fd
from tkinter.colorchooser import askcolor
import PIL
import matplotlib
from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont, ImageTk

save_route = "D:/Photos/WatermarkApp/"
IMG = None
FILE = None
OPACITY = (255,)
FONT_SIZE = 60
HEIGHT = 0
WIDTH = 0
ROTATION = 0
COLOR = (255, 255, 255)
FONT = "arial.ttf"


def select_file():
    global FILE
    filename = fd.askopenfilename(filetypes=[("jpeg", ".jpg .jpeg"),
                                             ("png", ".png"),
                                             ("bitmap", "bmp"),
                                             ("gif", ".gif")])
    show_image(filename)
    FILE = filename


def show_image(filename):
    global HEIGHT, WIDTH
    img = (Image.open(filename))
    width, height = img.size[0], img.size[1]
    r_img = resize(img)
    panel.configure(image=r_img)
    panel.image = r_img
    image_size.config(text=f"Image size {height}/{width} (height/width)", bg="#000000", fg="#fafafa",
                      font=("Arial", 8))
    HEIGHT = height / 2
    WIDTH = width / 2


def resize(img):
    size = img.size
    f_size = (600, 600)
    factor = min(float(f_size[1]) / size[1], float(f_size[0]) / size[0])
    width = int(size[0] * factor)
    height = int(size[1] * factor)
    r_img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(r_img)


def watermark():
    global IMG, FILE
    try:
        with Image.open(FILE).convert("RGBA") as base:
            # make a blank image for the text, initialized to transparent text color
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

            # get a font
            fnt = ImageFont.truetype(FONT, FONT_SIZE)
            # get a drawing context
            d = ImageDraw.Draw(txt)
            # draw text
            fill = COLOR + (OPACITY,)
            d.text((WIDTH, HEIGHT), f"{wmark_entry.get()}", font=fnt, fill=fill)
            rotated_txt = txt.rotate(ROTATION)
            out = Image.alpha_composite(base, rotated_txt)

            marked_img = out.convert("RGBA")
            w_img = resize(marked_img)
            panel.configure(image=w_img)
            panel.image = w_img

            IMG = marked_img
    except FileNotFoundError:
        tkinter.messagebox.showerror("Error", "No such file.")
    except PIL.UnidentifiedImageError:
        tkinter.messagebox.showerror("Error", "Wrong file extension.")
    except AttributeError:
        pass


def color():
    global COLOR
    colors = askcolor(title="Tkinter Color Chooser")
    new_color = colors[0]
    color_button.configure(bg=colors[1])
    COLOR = new_color
    watermark()


def opacity(value):
    global OPACITY
    OPACITY = int(value)
    watermark()


def font_size():
    global FONT_SIZE
    FONT_SIZE = int(font_size.get())
    watermark()


def font_change(new_font):
    global FONT
    FONT = new_font
    watermark()


def up():
    global HEIGHT
    HEIGHT -= 10
    watermark()


def down():
    global HEIGHT
    HEIGHT += 10
    watermark()


def left():
    global WIDTH
    WIDTH -= 10
    watermark()


def right():
    global WIDTH
    WIDTH += 10
    watermark()


def rotate_left():
    global ROTATION
    ROTATION += 5
    watermark()


def rotate_right():
    global ROTATION
    ROTATION -= 5
    watermark()


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

blank_photo = Image.new(mode="RGBA", size=(600, 600), color="#242424")
image1 = ImageTk.PhotoImage(blank_photo)
panel = Label(window, image=image1)
panel.image = image1  # keep a reference
panel.grid(column=0, rowspan=15)

image_size = Label(text=f"Image size {HEIGHT}/{WIDTH} (height/width)", bg="#000000", fg="#fafafa", font=("Arial", 8))
image_size.grid(column=0, row=16)

wmark = Label(text="Watermark:", width=15, bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
wmark.grid(column=3, row=2, sticky=E)
wmark_entry = Entry(width=40, bg="#242424", fg="#fafafa")
wmark_entry.grid(column=4, row=2, columnspan=2)
wmark_entry.get()

color_label = Label(text="Color:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
color_label.grid(column=4, row=7)
color_button = Button(text="      ", bg="#fafafa", fg="#fafafa", command=color)
color_button.grid(column=5, row=7, columnspan=3, sticky=W)

opacity_label = Label(text="Opacity:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
opacity_label.grid(column=4, row=8)
opacity = Scale(window, from_=0, to=255, orient="horizontal", bg="#000000", fg="#fafafa", highlightthickness=0,
                command=opacity)
opacity.set(255)
opacity.grid(column=5, row=8, ipadx=20)

font_label = Label(text="Font size:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
font_label.grid(column=4, row=9, sticky=E)
default_font_size = StringVar(window)
default_font_size.set("60")
font_size = Spinbox(window, from_=1, to=1000, width=5, highlightthickness=0, textvariable=default_font_size,
                    command=font_size)
font_size.grid(column=5, row=9, sticky=W)

font_list = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
formatted_font_list = [x.split("\\")[-1] for x in font_list]
font = StringVar(window)
font.set("arial.ttf")
font_type_label = Label(text="Font:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
font_type_label.grid(column=4, row=10)
font_type = OptionMenu(window, font, *formatted_font_list, command=font_change)
font_type.grid(column=5, row=10, sticky=W)

show_wm = Button(text="Show", bg="#000000", fg="#fafafa", command=watermark)
show_wm.grid(column=6, row=2)

name = Label(text="Save as:", width=15, bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
name.grid(column=3, row=11, sticky=E)
name_entry = Entry(width=40, bg="#242424", fg="#fafafa")
name_entry.grid(column=4, row=11, columnspan=2, sticky=W)
name_entry.get()

save_img = Button(text="Save", bg="#000000", fg="#fafafa", command=lambda: save(IMG))
save_img.grid(column=6, row=11)

up_btn = Button(text="⮝", font=("Arial", 20), bg="#000000", fg="#fafafa", command=up)
up_btn.grid(column=4, row=3, sticky=S)

down_btn = Button(text="⮟", font=("Arial", 20), bg="#000000", fg="#fafafa", command=down)
down_btn.grid(column=4, row=5, sticky=N)

left_btn = Button(text="⮜", font=("Arial", 20), bg="#000000", fg="#fafafa", command=left)
left_btn.grid(column=3, row=4, sticky=E, pady=0)

right_btn = Button(text="⮞", font=("Arial", 20), bg="#000000", fg="#fafafa", command=right)
right_btn.grid(column=5, row=4, sticky=W)

rotate_left_btn = Button(text="⟲", font=("Arial", 20), bg="#000000", fg="#fafafa", width=3, command=rotate_left)
rotate_left_btn.grid(column=6, row=4, sticky=W)

rotate_right_btn = Button(text="⟳", font=("Arial", 20), bg="#000000", fg="#fafafa", width=3, command=rotate_right)
rotate_right_btn.grid(column=7, row=4)

select = Button(text="Select file", font=("Arial", 12), bg="#000000", fg="#fafafa", command=select_file)
select.grid()

window.mainloop()
