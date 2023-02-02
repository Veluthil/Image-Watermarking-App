from tkinter import *

import PIL
from PIL import Image, ImageDraw, ImageFont

save_route = "D:/Photos/WatermarkApp/"


def watermark():
    image = file_entry.get().replace('"', '')
    try:
        with Image.open(image).convert("RGBA") as base:
            # make a blank image for the text, initialized to transparent text color
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
            height, width = base.size[0], base.size[1] - 100
            # get a font
            fnt = ImageFont.truetype("arial.ttf", 50)
            # get a drawing context
            d = ImageDraw.Draw(txt)

            # draw text, full opacity
            d.text((10, width), "©Veluthil", font=fnt, fill=(255, 255, 255, 200))

            out = Image.alpha_composite(base, txt)
            out.show()
            marked_img = out.convert("RGB")
            clean_save_route = save_route.replace('"', '')
            try:
                marked_img.save(f"{clean_save_route}/{name_entry.get()}.bmp")
                success.config(text=f"Image got watermarked and saved in {save_route}{name_entry.get()}.bmp.")
            except FileNotFoundError:
                print("No such file")
    except FileNotFoundError:
        print("No such file.")
        output.config(text="No such file.")
    except PIL.UnidentifiedImageError:
        print("This is not an image file.")
        output.config(text="This is not an image file.")


# ------------ Creating a GUI -------------------
window = Tk()
window.title("Image Watermarking App")
window.minsize(height=100, width=500)
window.config(padx=20, pady=20)

label = Label(text="File path:")
label.grid(column=0, row=0)
file_entry = Entry(width=70)
file_entry.grid(column=1, row=0, columnspan=5)
file_entry.get()

name = Label(text="Watermarked image name:")
name.grid(column=0, row=1)
name_entry = Entry(width=70)
name_entry.grid(column=1, row=1, columnspan=5)
name_entry.get()

output = Label(text="")
output.grid(column=0, row=4)
#
# search = Button(text="Search", command=read_image)
# search.grid(column=0, row=2)
#
# search_success = Label()
# search_success.grid(column=0, row=1)

watermark = Button(text="Add watermark", command=watermark)
watermark.grid(column=1, row=2)
success = Label(text="", width=70)
success.grid(column=1, row=4)

window.mainloop()
