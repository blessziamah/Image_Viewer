from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")

# Declaration of global variables
global index


my_img1 = ImageTk.PhotoImage(Image.open("image\\image1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("image\\image2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("image\\image3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("image\\image4.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4]


def forward(position):
    global my_label
    global button_forward
    global button_back
    global index
    global status

    index = position

    # First checks if we're at the end of image list. If True, button is disabled
    if index == (len(image_list) - 1):
        button_forward = Button(root, text=">>", state=DISABLED)
        button_forward.grid(row=1, column=2)
    else:
        my_label.grid_forget()  # If were not at end of list, displayed image is removed
        my_label = Label(image=image_list[index + 1])   # List index is increased to get next image and display it.
        my_label.grid(row=0, column=0, columnspan=3)
        button_forward = Button(root, text=">>", command=lambda: forward(index + 1))    # Forward button is updated
        button_forward.grid(row=1, column=2)

        # Update of count on the status bar
        status = Label(root, text=f"image {index + 2} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=EW)


def back():
    pass


my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

button_quit = Button(root, text="EXIT", command=root.quit)
button_quit.grid(row=1, column=1)

button_back = Button(root, text="<<", command=lambda: back())
button_back.grid(row=1, column=0)

button_forward = Button(root, text=">>", command=lambda: forward(0))
button_forward.grid(row=1, column=2, pady=10)

status = Label(root, text=f"image 1 of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=EW)

root.mainloop()
