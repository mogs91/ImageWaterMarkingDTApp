##imports
from tkinter import *

from PIL import ImageTk, Image

from tkinter import filedialog


def desktop_app():
    # Basic instantiation

    def openfilename():
        """it opens a file dialog box to select image,
        The dialogue box has a title 'Select image' """
        filename = filedialog.askopenfilename(title='Select image')
        return filename

    def open_img():
        """Select the Image name  from a folder,
        ,opens the image,resize the image and apply a high-quality down sampling filter
        ,PhotoImage class is used to add image to widgets, icons etc
        ,create a label  # set the image as img"""
        image = openfilename()
        img = Image.open(image)
        img = img.resize((450, 450))
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=2)

    ##TKinter Setup
    window = Tk()
    window.title("Image WaterMarking")
    window.minsize(width=800, height=800)
    window.resizable(width=True, height=True)
    window.config(padx=40, pady=40)

    upload_image_btn = Button(text='upload image', command=open_img).grid(
        row=1, columnspan=4)

#Todo: need to add the watermarking functionality
    watermark_btn = Button(text='watermark').grid(
        row=4, columnspan=4)



    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    desktop_app()

