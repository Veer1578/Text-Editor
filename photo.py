from tkinter import * 
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()

def openImage():
    root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\veean\OneDrive\Desktop\Codingal Python\Module 7", title="Open an image file", filetypes=(('JPG file', '*.jpg'), ('All files', '*.*')))
    global my_image

    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    image_label = Label(root, image=my_image)
    image_label.pack(pady=10)

my_button = Button(root, text="Image", command=openImage)
my_button.pack(pady=10)

root.mainloop()
