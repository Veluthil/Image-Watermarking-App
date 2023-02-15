from tkinter import *
from tkinter import filedialog as fd
from tkinter.colorchooser import askcolor
import tkinter.messagebox
import PIL
from PIL import Image, ImageDraw, ImageFont, ImageTk
import matplotlib
from matplotlib import font_manager
import os


# --------- Variables for Watermark and Image -----------------
img_main = ""
file_main = ""
opacity_main = (255,)
font_size_main = 60
height_main = 0
width_main = 0
rotation_main = 0
color_main = (255, 255, 255)
font_main = "arial"
original_height = 0
original_width = 0


# ---------- Creating Main Functions ------------------------

def select_file():
    global file_main
    try:
        filename = fd.askopenfilename(filetypes=[("jpeg", ".jpg .jpeg"),
                                                 ("png", ".png"),
                                                 ("bitmap", "bmp"),
                                                 ("gif", ".gif")])
        show_image(filename)
        file_main = filename
    except AttributeError:
        pass


def show_image(filename):
    global height_main, width_main, original_height, original_width
    img = (Image.open(filename))
    width, height = img.size[0], img.size[1]
    r_img = resize(img)
    panel.configure(image=r_img)
    panel.image = r_img
    image_size.config(text=f"Image size {height}/{width} (height/width)", bg="#000000", fg="#fafafa",
                      font=("Arial", 8))
    height_main = height / 2
    width_main = width / 2
    original_height = height
    original_width = width


def resize(img):
    size = img.size
    f_size = (700, 600)
    factor = min(float(f_size[1]) / size[1], float(f_size[0]) / size[0])
    width = int(size[0] * factor)
    height = int(size[1] * factor)
    r_img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(r_img)


def watermark():
    global img_main, file_main, font_size_main
    try:
        with Image.open(file_main).convert("RGBA") as base:
            # make a blank image for the text, initialized to transparent text color
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
            # get a font
            fnt = ImageFont.truetype(font_main, font_size_main)
            # get a drawing context
            d = ImageDraw.Draw(txt)
            # draw text
            fill = color_main + (opacity_main,)
            d.text((width_main, height_main), f"{wmark_entry.get()}", font=fnt, fill=fill)
            rotated_txt = txt.rotate(rotation_main)
            out = Image.alpha_composite(base, rotated_txt)

            marked_img = out.convert("RGBA")
            w_img = resize(marked_img)
            panel.configure(image=w_img)
            panel.image = w_img

            img_main = marked_img
    except FileNotFoundError:
        tkinter.messagebox.showerror("Error", "No such file.")
    except PIL.UnidentifiedImageError:
        tkinter.messagebox.showerror("Error", "Wrong file extension.")
    except AttributeError:
        pass


def save(marked_img):
    path = fd.asksaveasfilename(confirmoverwrite=True, defaultextension="png", filetypes=[("jpeg", ".jpg"),
                                                                                          ("png", ".png"),
                                                                                          ("bitmap", "bmp"),
                                                                                          ("gif", ".gif")])
    if path is not None:
        if os.path.splitext(path)[1] == ".jpg":
            image = marked_img.convert("RGB")
            image.save(path)
            tkinter.messagebox.showinfo("Success", "Image got watermarked and saved.")

#  ----------------- Watermark Appearance Functions --------------


def color():
    global color_main
    colors = askcolor(title="Tkinter Color Chooser")
    new_color = colors[0]
    color_button.configure(bg=colors[1])
    color_main = new_color
    watermark()


def opacity(value):
    global opacity_main
    opacity_main = int(value)
    watermark()


def font_size():
    global font_size_main
    font_size_main = int(font_size.get())
    watermark()


def font_change(new_font):
    global font_main
    font_main = new_font
    watermark()


def up():
    global height_main, original_height
    if original_height > 1500:
        height_main -= 50
    else:
        height_main -= 10
    watermark()


def down():
    global height_main, original_height
    if original_height > 1500:
        height_main += 50
    else:
        height_main += 10
    watermark()


def left():
    global width_main, original_width
    if original_width > 1500:
        width_main -= 50
    else:
        width_main -= 10
    watermark()


def right():
    global width_main, original_width
    if original_width > 1500:
        width_main += 50
    else:
        width_main += 10
    watermark()


def rotate_left():
    global rotation_main
    rotation_main += 5
    watermark()


def rotate_right():
    global rotation_main
    rotation_main -= 5
    watermark()


# ----------- Creating a GUI -------------------
window = Tk()
window.title("Image Watermarking App")
window.minsize(height=100, width=500)
window.config(padx=20, pady=20, bg="#000000")

# ----------- Blank Photo ----------------------
blank_photo = Image.new(mode="RGBA", size=(700, 600), color="#242424")
image1 = ImageTk.PhotoImage(blank_photo)
panel = Label(window, image=image1)
panel.image = image1  # keep a reference
panel.grid(column=0, rowspan=15)

# ----------- Image Size Label -----------------
image_size = Label(text=f"Image size {height_main}/{width_main} (height/width)", bg="#000000", fg="#fafafa",
                   font=("Arial", 8))
image_size.grid(column=0, row=16)

# ----------- Watermark Text -------------------
wmark = Label(text="Watermark:", width=15, bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
wmark.grid(column=3, row=2, sticky=W)
wmark_entry = Entry(width=50, bg="#242424", fg="#fafafa")
wmark_entry.grid(column=4, row=2, columnspan=4)
wmark_entry.get()

# ------------ Watermark Color ---------------------
color_label = Label(text="Color:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
color_label.grid(column=4, row=9, sticky=W)
color_button = Button(text="      ", bg="#fafafa", fg="#fafafa", command=color)
color_button.grid(column=5, row=9, sticky=E)

# ------------ Watermark Opacity ------------------
opacity_label = Label(text="Opacity:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
opacity_label.grid(column=4, row=10, sticky=W)
opacity = Scale(window, from_=0, to=255, orient="horizontal", bg="#000000", fg="#fafafa", highlightthickness=0,
                command=opacity)
opacity.set(255)
opacity.grid(column=5, row=10, ipadx=20, sticky=E)

# ------------- Watermark Font Size ----------------
font_label = Label(text="Font size:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
font_label.grid(column=4, row=11, sticky=W)
default_font_size = StringVar(window)
default_font_size.set("60")
font_size = Spinbox(window, from_=1, to=1000, width=5, highlightthickness=0, textvariable=default_font_size,
                    command=font_size)
font_size.grid(column=5, row=11, sticky=E)

# -------------- Watermark Font Type ---------------
font_list = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
final_font_list = []
formatted_font_list = [x.split("\\")[-1] for x in font_list]
for font in formatted_font_list:
    if ".otf" not in font:
        final_font_list.append(font.replace(".ttf", "").replace(".TTF", "").replace(".ttc", ""))
font = StringVar(window)
font.set("arial")
font_type_label = Label(text="Font:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
font_type_label.grid(column=4, row=12, sticky=W)
font_type = OptionMenu(window, font, *final_font_list, command=font_change)
font_type.grid(column=5, row=12, sticky=E)

# -------------- Show Watermark Button -------------
show_wm = Button(text="Show", bg="#000000", fg="#fafafa", command=watermark)
show_wm.grid(column=8, row=2)

# -------------- Save Watermarked Image Button ----------------
save_img = Button(text="Save", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"), command=lambda: save(img_main))
save_img.grid(column=7, row=16)

# -------------- Watermark Location Settings -----------------
up_btn = Button(text="⮝", font=("Arial", 20), bg="#000000", fg="#fafafa", command=up)
up_btn.grid(column=4, row=3, sticky=S)

down_btn = Button(text="⮟", font=("Arial", 20), bg="#000000", fg="#fafafa", command=down)
down_btn.grid(column=4, row=5, sticky=N)

left_btn = Button(text="⮜", font=("Arial", 20), bg="#000000", fg="#fafafa", command=left)
left_btn.grid(column=3, row=4, sticky=E, pady=0)

right_btn = Button(text="⮞", font=("Arial", 20), bg="#000000", fg="#fafafa", command=right)
right_btn.grid(column=5, row=4, sticky=W)

rotate_left_btn = Button(text="⟲", font=("Arial", 20), bg="#000000", fg="#fafafa", command=rotate_left)
rotate_left_btn.grid(column=6, row=4, sticky=W)

rotate_right_btn = Button(text="⟳", font=("Arial", 20), bg="#000000", fg="#fafafa", command=rotate_right)
rotate_right_btn.grid(column=7, row=4, sticky=W)

# --------------- Select Image File --------------------
select = Button(text="Select file", font=("Arial", 12), bg="#000000", fg="#fafafa", command=select_file)
select.grid(column=0, row=17)

# -------------- Application Loop -----------------
window.mainloop()
