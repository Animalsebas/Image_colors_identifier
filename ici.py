from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import sys
def load_image():
    image_dir = filedialog.askopenfilename()
    img= (Image.open(image_dir))
    resized_image= img.resize((400,600), Image.ANTIALIAS)
    img_forshow = ImageTk.PhotoImage(resized_image)
    print(image_dir)
    panel = Label(aci_window, image = img_forshow)
    panel.image = img_forshow
    panel.pack(pady=30 , fill = "none", expand = "no")
    image_button.configure(text = "Exit", command = exit)
    img = (Image.open(image_dir)).resize((10,10), Image.ANTIALIAS)
    img.convert('RGB')
    width, height = img.size
    colors = []
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x,y))
            colors.append(img.getpixel((x,y)))
    results_window = Tk()
    results_window.resizable(True, True)
    results_window.geometry("250x450")
    results_window.title("RESULTS")
    listbox = Listbox(results_window)
    listbox.pack(side = LEFT, fill = BOTH)
    scrollbar = Scrollbar(results_window)
    scrollbar.pack(side = RIGHT, fill = BOTH)
    result_rgb = []
    for values in colors:
        if values not in result_rgb:
            result_rgb.append(values)
    result_hex =[]
    for items in result_rgb:
        result_hex.append("#" + str('%02x%02x%02x' % items))
    for items in result_hex:
        listbox.insert(END, items)
    count = 0
    for items in result_hex:
        listbox.itemconfig(count, {'bg':(str(result_hex[count]))})
        count = count + 1
    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)
    results_window.mainloop()
aci_window = Tk()
aci_window.resizable(True, True)
aci_window.geometry("500x900")
aci_window.title("Image Colors Identifier")
aci_window.configure(bg = "gray8")
image_button = Button(aci_window, width=25, height=2, bg = "white", fg = "black", text="Load image", font="Arial 14", command = load_image)
image_button.pack(pady=15)
aci_window.mainloop()