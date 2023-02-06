import tkinter.messagebox
from tkinter import *
from tkinter import filedialog as fd
import PIL
from PIL import Image, ImageDraw, ImageFont, ImageTk

save_route = "D:/Photos/WatermarkApp/"
IMG = None
FILE = None
OPACITY = 255
FONT_SIZE = 50
HEIGHT = 0
WIDTH = 0
ROTATION = 0


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
    # if len(file_entry.get()) != 0:
    img = (Image.open(filename))
    width, height = img.size[0], img.size[1]
    r_img = resize(img)
    panel.configure(image=r_img)
    panel.image = r_img
    image_size.config(text=f"Image size {height}/{width} (height/width)", bg="#000000", fg="#fafafa",
                       font=("Arial", 8))
    HEIGHT = height/2
    WIDTH = width/2
    # else:
    #     tkinter.messagebox.showerror("Error", "You have to provide a file path to continue.")


def resize(img):
    size = img.size
    f_size = (700, 600)
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
            fnt = ImageFont.truetype("arial.ttf", FONT_SIZE)
            # get a drawing context
            d = ImageDraw.Draw(txt)
            # draw text

            d.text((WIDTH, HEIGHT), f"{wmark_entry.get()}", font=fnt, fill=(255, 255, 255, OPACITY))
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


def opacity(value):
    global OPACITY
    OPACITY = int(value)
    watermark()


def font_size():
    global FONT_SIZE
    FONT_SIZE = int(font_size.get())
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

blank_photo = Image.new(mode="RGBA", size=(700, 600), color="#242424")
image1 = ImageTk.PhotoImage(blank_photo)
panel = Label(window, image=image1)
panel.image = image1 #keep a reference
panel.grid(column=0, rowspan=10)

image_size = Label(text=f"Image size {HEIGHT}/{WIDTH} (height/width)", bg="#000000", fg="#fafafa", font=("Arial", 8))
image_size.grid(column=0, row=12)

# label = Label(text="Image file path:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
# label.grid(column=1, row=0, columnspan=2, sticky=E)
# file_entry = Entry(width=60, bg="#242424", fg="#fafafa")
# file_entry.grid(column=3, row=0, columnspan=10)
# file_entry.get()
#
# show = Button(text="Show", bg="#000000", fg="#fafafa", command=show_image)
# show.grid(column=13, row=0)

wmark = Label(text="Watermark text:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
wmark.grid(column=1, row=2, columnspan=2, sticky=E)
wmark_entry = Entry(width=60, bg="#242424", fg="#fafafa")
wmark_entry.grid(column=3, row=2, columnspan=10)
wmark_entry.get()

opacity_label = Label(text="Opacity", bg="#000000", fg="#fafafa", font=("Arial", 8))
opacity_label.grid(column=4, row=6)
opacity = Scale(window, from_=0, to=255, orient="horizontal", bg="#000000", fg="#fafafa", highlightthickness=0,
                command=opacity)
opacity.set(255)
opacity.grid(column=5, row=6, ipadx=20)

font_label = Label(text="Font size", bg="#000000", fg="#fafafa", font=("Arial", 8))
font_label.grid(column=4, row=7, sticky=E)
default_font_size = StringVar(window)
default_font_size.set("50")
font_size = Spinbox(window, from_=1, to=500, width=5, highlightthickness=0, textvariable=default_font_size,
                    command=font_size)
font_size.grid(column=5, row=7, sticky=W)

show_wm = Button(text="Show", bg="#000000", fg="#fafafa", command=watermark)
show_wm.grid(column=13, row=2)

name = Label(text="Save as:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
name.grid(column=1, row=8, columnspan=2, sticky=E)
name_entry = Entry(width=60, bg="#242424", fg="#fafafa")
name_entry.grid(column=3, row=8, columnspan=10)
name_entry.get()

save_img = Button(text="Save", bg="#000000", fg="#fafafa", command=lambda: save(IMG))
save_img.grid(column=13, row=8)

up_btn = Button(text="↑", font=("Arial", 20), bg="#000000", fg="#fafafa", command=up)
up_btn.grid(column=3, row=3, sticky=S)

down_btn = Button(text="↓", font=("Arial", 20), bg="#000000", fg="#fafafa", command=down)
down_btn.grid(column=3, row=4)

left_btn = Button(text="←", font=("Arial", 20), bg="#000000", fg="#fafafa", command=left)
left_btn.grid(column=2, row=4, sticky=E, pady=0)

right_btn = Button(text="→", font=("Arial", 20), bg="#000000", fg="#fafafa", command=right)
right_btn.grid(column=4, row=4, sticky=W)

rotate_left_btn = Button(text="↺", font=("Arial", 20), bg="#000000", fg="#fafafa", width=4, command=rotate_left)
rotate_left_btn.grid(column=7, row=4)

rotate_right_btn = Button(text="↻", font=("Arial", 20), bg="#000000", fg="#fafafa", width=4, command=rotate_right)
rotate_right_btn.grid(column=8, row=4)

select = Button(text="Select file", font=("Arial", 10), bg="#000000", fg="#fafafa", command=select_file)
select.grid()

window.mainloop()