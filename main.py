from tkinter import *
from PIL import Image, ImageDraw, ImageFont

save_route = "D:/Photos/Watermark App/"


def read_image():
    image = entry.get()
    img = Image.open(image)
    img.show()
    search_success.config(text="File loaded.")
    return img


def watermark():
    with Image.open(entry.get()).convert("RGBA") as base:
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
        marked_img = out.convert("RGBA")
        # marked_img_name = entry.get()[:-4] + "watermarked.jpg"
        # marked_img.save(save_route, marked_img_name)


# Creating a GUI
window = Tk()
window.title("Image Watermarking App")
window.minsize(height=100, width=500)
window.config(padx=20, pady=20)

label = Label(text="File path:")
label.grid(column=0, row=0)
entry = Entry(width=70)
entry.grid(column=1, row=0, columnspan=5)
entry.get()

search = Button(text="Search", command=read_image)
search.grid(column=0, row=2)

search_success = Label()
search_success.grid(column=0, row=1)

watermark = Button(text="Add watermark", command=watermark)
watermark.grid(column=1, row=2)

window.mainloop()
