import tkinter.messagebox
from tkinter import *
import PIL
from PIL import Image, ImageDraw, ImageFont

save_route = "D:/Photos/WatermarkApp/"


def watermark():
    if len(file_entry.get()) != 0:
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
                # draw text
                d.text((10, width), "©Veluthil", font=fnt, fill=(255, 255, 255, 200))

                out = Image.alpha_composite(base, txt)
                out.show()
                marked_img = out.convert("RGBA")
                clean_save_route = save_route.replace('"', '')
                file_name = name_entry.get()
                with open("data.txt", mode="r") as file:
                    names = file.read()
                    if file_name not in names:
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

        except FileNotFoundError:
            tkinter.messagebox.showerror("Error", "No such file.")
        except PIL.UnidentifiedImageError:
            tkinter.messagebox.showerror("Error", "Wrong file extension.")

    else:
        tkinter.messagebox.showerror("Error", "You have to provide a file path to continue.")


# ------------ Creating a GUI -------------------
window = Tk()
window.title("Image Watermarking App")
window.minsize(height=100, width=500)
window.config(padx=20, pady=20)

label = Label(text="Insert file path of the image:")
label.grid(column=0, row=0)
file_entry = Entry(width=90)
file_entry.grid(column=1, row=0, columnspan=5)
file_entry.get()

name = Label(text="Watermarked image name:")
name.grid(column=0, row=1)
name_entry = Entry(width=90)
name_entry.grid(column=1, row=1, columnspan=5)
name_entry.get()

watermark = Button(text="Add watermark", command=watermark)
watermark.grid(column=5, row=3)

window.mainloop()
