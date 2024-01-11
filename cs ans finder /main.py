from PIL import Image
from pytesseract import pytesseract
from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


def path():
    Tk().withdraw()
    filename = askopenfilename()
    return filename


# Defining paths to tesseract.exe
# and the image we would be using

image_path = path()

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the tesseract executable
# location to pytesseract library

text = pytesseract.image_to_string(img)

# Passing the image object to image_to_string() function
# This function will extract the text from the image


# Displaying the extracted text
print(text)

f = open("file.py","w")
f.write(text)