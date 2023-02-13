# Image-Watermarking-App
The app allows to add a custom watermark to the provided image file, then name it and save it to the chosen directory. 

This Python project uses Tkinter, Pillow and Matplotlib libraries to create GUI and all of the features.

GUI layout:
-----
![Screenshot 2023-02-10 175604](https://user-images.githubusercontent.com/108438343/218153810-81981fe6-6c76-42ef-9278-e2cc427edde8.png)

Image file selection:
-----
![Screenshot 2023-02-10 181129](https://user-images.githubusercontent.com/108438343/218153915-d8dfd35c-eab2-4229-8082-c0f101a1237a.png)

Watermark text color selection:
-----
![Screenshot 2023-02-10 180525](https://user-images.githubusercontent.com/108438343/218153952-aaf0a595-eaa3-4bed-86c4-9adc9de6e254.png)

Font type selection:
-----
![Screenshot 2023-02-10 175732](https://user-images.githubusercontent.com/108438343/218154003-be9013b2-1978-4d89-a282-c2ee183500f5.png)

Saving process:
-----
![Screenshot 2023-02-10 180237](https://user-images.githubusercontent.com/108438343/218154068-513d9ec6-9b82-4bf2-911d-b73141c58e36.png)

-----

Functionality
------

- Buttons, Scale, Spinbox, and OptionMenu allow you to adjust the Watermark position, rotation, font size, font type, opacity, and color.

- The "Select file" button opens a new window, where you can choose any of the jpeg, .jpg, .jpeg, png, .png, bitmap, bmp, gif, .gif files to load.

- The watermark label allows you to provide a text that will get transformed into a custom watermark that you can modify with all of the options given above.

- The "Save" button allows you to name your watermarked image and save it in the chosen file path - app automatically converts .jpg image file into RGB. 


I will change this project into an OOP app to avoid using global variables.
