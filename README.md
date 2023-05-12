# Image Watermarking App

The Image Watermarking App is a Python project that allows you to add a custom watermark to an image file and save it to the chosen directory. It uses Tkinter, Pillow, and Matplotlib libraries to create a GUI and implement all the features.

## GUI Layout

The app's GUI consists of several components, including buttons, scales, spinboxes, and option menus, which allow you to adjust the watermark's position, rotation, font size, font type, opacity, and color. The layout is shown in the following image:

![App Layout](https://user-images.githubusercontent.com/108438343/218153810-81981fe6-6c76-42ef-9278-e2cc427edde8.png)

## Image File Selection

The "Select file" button opens a new window, where you can choose any of the jpeg, .jpg, .jpeg, png, .png, bitmap, bmp, gif, .gif files to load. Once the image is loaded, you can add your custom watermark to it.

![File Selection](https://user-images.githubusercontent.com/108438343/218153915-d8dfd35c-eab2-4229-8082-c0f101a1237a.png)

## Watermark Customization

The app allows you to customize the watermark by providing text that will get transformed into a custom watermark. You can adjust the watermark's position, rotation, font size, font type, opacity, and color using the various components in the GUI.

![Watermark Customization](https://user-images.githubusercontent.com/108438343/218153952-aaf0a595-eaa3-4bed-86c4-9adc9de6e254.png)

## Saving Process

Once you have customized your watermark, you can save the watermarked image by clicking the "Save" button. This allows you to name your watermarked image and save it in the chosen file path. The app automatically converts the image file into RGB before saving it.

![Saving Process](https://user-images.githubusercontent.com/108438343/218154068-513d9ec6-9b82-4bf2-911d-b73141c58e36.png)

## Dependencies

The Image Watermarking App uses the following libraries:

- Tkinter
- Pillow
- Matplotlib
