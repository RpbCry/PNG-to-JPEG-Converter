# PNG to JPEG Converter
This is a simple Python application that allows users to convert PNG images to JPEG format using a graphical user interface (GUI). The application uses the tkinter library for the GUI and the Pillow library for image processing.

## Requirements
Before running the application, make sure you have the following installed:
`Python (3.x recommended)`
`Pillow library
```
pip install Pillow
```
Usage
Clone or download this repository to your local machine.
Open a terminal or command prompt and navigate to the project directory.
Run the Python script `png_to_jpeg_converter.py`.

## Instructions
Upon running the script, a GUI window will appear.
Click on the "Convert to JPEG" button to start the conversion process.
A file dialog will open, allowing you to select the PNG image you want to convert.
After selecting the image, another file dialog will open, prompting you to choose the destination path and filename for the converted JPEG image.
Click "Save" to save the converted JPEG image.

## Note
The application will handle PNG images with transparency (RGBA mode) by converting them to RGB mode before saving as JPEG.
The output JPEG image will be saved with the ".jpeg" extension, even if you provide a different extension in the file dialog.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it according to the terms of the license.

## Disclaimer
This application is intended for simple conversion tasks and may not handle extremely large or complex images efficiently. It is provided as-is without any warranties. Use it responsibly and at your own risk.

Enjoy converting your PNG images to JPEG hassle-free! If you encounter any issues or have suggestions for improvements, feel free to raise an issue or submit a pull request. Happy converting!
