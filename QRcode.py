# QR code generation using python

import pyqrcode
from PIL import Image
link = input("Enter anything to generate QR: ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale = 5)
Image.open("QRCode.png")

'''
The PyQRCode library is used to generate QR codes in Python. It is simple to use and can generate QR codes in various formats like SVG and PNG. 
It does not handle image manipulations directly but focuses solely on QR code generation.

Pillow is the Python Imaging Library (PIL) fork. It is widely used for image processing tasks, such as opening, 
manipulating, saving, and displaying images. You can crop, resize, rotate, apply filters, and much more with Pillow.

The PyPNG library is used to handle PNG images. It is often used alongside other libraries like PyQRCode to save images in PNG format. 
It is specifically designed for working with PNG images at a pixel level, providing control over pixel data manipulation.

Summary of Uses:
PyQRCode: Create QR codes in SVG or PNG formats.
Pillow (PIL): Perform image processing tasks like resizing, cropping, filtering, and color manipulation.
PyPNG: Work with PNG files at the pixel level and save PNGs when needed for QR codes.
'''


'''
Here's a line-by-line breakdown of this code, which generates a QR code from user input and opens the generated image:

1. import pyqrcode
This imports the pyqrcode module, which is used for generating QR codes in Python.
The library provides methods to create QR codes from various data inputs (e.g., text, URLs).

2. from PIL import Image
This imports the Image module from the Pillow library (PIL), which is used for opening, manipulating, and saving images in Python.

3. link = input("Enter anything to generate QR: ")
This prompts the user to input a string, which could be text, a URL, or anything they want to encode into a QR code.
The user's input is stored in the variable link.

4. qr_code = pyqrcode.create(link)
This line generates a QR code based on the user-provided input.
The pyqrcode.create() function converts the string in link into a QR code object, which is stored in the variable qr_code.

5. qr_code.png("QRCode.png", scale=5)
This saves the generated QR code as a PNG image file named "QRCode.png".
The scale=5 parameter sets the size of the QR code. Increasing the scale value makes the QR code image larger.

6. Image.open("QRCode.png")
This opens the "QRCode.png" image file using the Pillow library's Image.open() function.
It loads the QR code image into memory so that it can be viewed or manipulated further.

How the Code Works:
The user is asked to input a string (e.g., a URL).
The string is converted into a QR code and saved as a PNG file.
The saved QR code image is then opened for viewing.
'''