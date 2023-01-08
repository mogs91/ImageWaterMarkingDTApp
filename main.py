#imports
from tkinter import *

# loading Python Imaging Library
from PIL import ImageTk, Image

# To get the dialog box to open when required
from tkinter import filedialog

def desktop_app():
    # Basic instantiation

    def openfilename():
        # open file dialog box to select image
        # The dialogue box has a title "Open"
        filename = filedialog.askopenfilename(title='"pen')
        return filename

    def open_img():
        # Select the Imagename  from a folder
        x = openfilename()

        # opens the image
        img = Image.open(x)

        # resize the image and apply a high-quality down sampling filter
        img = img.resize((450, 450), Image.ANTIALIAS)

        # PhotoImage class is used to add image to widgets, icons etc
        img = ImageTk.PhotoImage(img)

        # create a label
        panel = Label(window, image=img)

        # set the image as img
        panel.image = img
        panel.grid(row=2)

    ##TKinter
    window = Tk()
    window.title("Image WaterMarking")
    window.minsize(width=800, height=800)
    # Allow Window to be resizable
    window.resizable(width=True, height=True)
    # Adding padding
    window.config(padx=40, pady=40)



    # Create a button and place it into the window using grid layout
    upload_image_btn = Button(window, text='upload image', command=open_img).grid(
        row=1, columnspan=4)



    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    desktop_app()



#Todo: We will use Tkinter to create a  GUI that takes a image
#TODO: You can then click a button "WaterMark Image" to add a logo/text to the image
#Todo:  we might need to use Pillow https://pypi.org/project/Pillow/

