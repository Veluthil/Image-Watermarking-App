# Image-Watermarking-App
App that allows to add a custom watermark to the provided image file. 

This Python project uses Tkinter, Pillow and Matplotlib libraries to create GUI and all of the features.

GUI layout:
-----
![Screenshot 2023-02-08 171927](https://user-images.githubusercontent.com/108438343/217624072-634945a0-7cdc-41f9-aaec-4b8d99473a5d.png)

Image file selection:
-----
![Screenshot 2023-02-08 181910](https://user-images.githubusercontent.com/108438343/217625061-3f624887-4257-45c1-99b9-8ffbb0d5ee1f.png)

Watermark text color selection:
-----
![Screenshot 2023-02-08 172136](https://user-images.githubusercontent.com/108438343/217624625-36e255db-d945-4022-a9ad-36562dda0c89.png)

Font type selection:
-----
![Screenshot 2023-02-08 224217](https://user-images.githubusercontent.com/108438343/217658028-bb467611-67d5-4c44-9f5d-a6209a73d446.png)

Saving process:
-----
![Screenshot 2023-02-08 173146](https://user-images.githubusercontent.com/108438343/217625026-59259d94-c367-4acc-95dd-7ae43192eae5.png)
![Screenshot 2023-02-08 173257](https://user-images.githubusercontent.com/108438343/217625569-3efd0e85-0e15-49a2-97ad-89fed247eb5b.png)
-----

Functionality
------

- Buttons, Scale, Spinbox, and OptionMenu allow you to adjust the Watermark position, rotation, font size, font type, opacity, and color.

- The "Select file" button opens a new window, where you can choose any of the jpeg, .jpg, .jpeg, png, .png, bitmap, bmp, gif, .gif files to load.

- Watermark label allows you to provide a text that will be made into a custom watermark that you can modify with all of the stated above options.

- The "Save as:" label allows you to name your watermarked image, and later save it to the previously hard-coded directory thanks to the "Save" button. 


I want to change this project into an OOP app, to avoid using global variables.