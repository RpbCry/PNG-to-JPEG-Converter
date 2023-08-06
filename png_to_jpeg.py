import tkinter as tk
from tkinter import filedialog
from PIL import Image

def convert_to_jpeg():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    
    if not file_path:
        return

    img = Image.open(file_path)

    # Convert RGBA image to RGB mode
    img = img.convert("RGB")

    jpeg_file_path = filedialog.asksaveasfilename(defaultextension=".jpeg", filetypes=[("JPEG files", "*.jpeg")])

    if not jpeg_file_path:
        return

    if not jpeg_file_path.lower().endswith('.jpeg'):
        jpeg_file_path += '.jpeg'

    img.save(jpeg_file_path, format='JPEG')
    tk.messagebox.showinfo("Conversion Successful", f"Image converted and saved as {jpeg_file_path}")

# Create a simple GUI window
root = tk.Tk()
root.title("PNG to JPEG Converter")

# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert to JPEG", command=convert_to_jpeg)
convert_button.pack(pady=20)

root.mainloop()
