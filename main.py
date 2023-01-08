#imports

from tkinter import *

from PIL import Image


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def desktop_app():
    # Basic instantiation

    ##TKinter
    window = Tk()
    window.title("Image WaterMarking")
    window.minsize(width=800, height=800)
    # Adding padding
    window.config(padx=40, pady=40)

    ##Pillow

    #Todo: We need to add two buttons on the bottom of the window
    #We can use a stack layout image on top and two buttons on the bottom
    #Todo:one button for adding the image - here we should use Pillow
    #Todo:one button for applying the watermark


    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    desktop_app()



#Todo: We will use Tkinter to create a  GUI that takes a image
#TODO: You can then click a button "WaterMark Image" to add a logo/text to the image
#Todo:  we might need to use Pillow https://pypi.org/project/Pillow/

