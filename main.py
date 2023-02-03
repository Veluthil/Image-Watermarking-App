import tkinter.messagebox
from tkinter import *
import PIL
from PIL import Image, ImageDraw, ImageFont, ImageTk

save_route = "D:/Photos/WatermarkApp/"


def show_image():
    img = (Image.open(file_entry.get().replace('"', '')))
    size = img.size
    f_size = (700, 600)
    factor = min(float(f_size[1]) / size[1], float(f_size[0]) / size[0])
    width = int(size[0] * factor)
    height = int(size[1] * factor)
    r_img = img.resize((width, height), Image.LANCZOS)
    r_img = ImageTk.PhotoImage(r_img)
    panel.configure(image=r_img)
    panel.image = r_img


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
                d.text((10, width), f"{wmark_entry.get()}", font=fnt, fill=(255, 255, 255, 200))

                out = Image.alpha_composite(base, txt)

                marked_img = out.convert("RGBA")
                clean_save_route = save_route.replace('"', '')
                file_name = name_entry.get()
                with open("data.txt", mode="r") as file:
                    names = file.read()
                    if file_name not in names:
                        # w_img = ImageTk.PhotoImage(marked_img)
                        # panel.configure(image=w_img)
                        # panel.image = w_img
                        out.show()
                        answer = tkinter.messagebox.askyesno("Procced", "Do you want to save?")
                        if answer:
                            with open("data.txt", mode="a") as file:
                                file.write(f"{file_name}\n")
                            marked_img.save(f"{clean_save_route}/{file_name}.bmp")
                            tkinter.messagebox.showinfo("Success", f"Image got watermarked and saved to"
                                                                   f" {save_route}{file_name}.bmp.")
                            out.show()
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
window.config(padx=20, pady=20, bg="#000000")

blank_photo = Image.new(mode="RGBA", size=(700, 600), color="#696969")
image1 = ImageTk.PhotoImage(blank_photo)
panel = Label(window, image=image1)
panel.image = image1 #keep a reference
panel.grid(column=0, rowspan=10)

label = Label(text="Image full file path:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
label.grid(column=1, row=0)
file_entry = Entry(width=70)
file_entry.grid(column=2, row=0, columnspan=5)
file_entry.get()

wmark = Label(text="Watermark text:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
wmark.grid(column=1, row=2)
wmark_entry = Entry(width=70)
wmark_entry.grid(column=2, row=2, columnspan=5)
wmark_entry.get()

name = Label(text="Watermarked image file name:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
name.grid(column=1, row=3)
name_entry = Entry(width=70)
name_entry.grid(column=2, row=3, columnspan=5)
name_entry.get()

watermark = Button(text="Add watermark", bg="#000000", fg="#fafafa", command=watermark)
watermark.grid(column=5, row=4)

show = Button(text="Show image", bg="#000000", fg="#fafafa", command=show_image)
show.grid(column=3, row=1)

window.mainloop()
