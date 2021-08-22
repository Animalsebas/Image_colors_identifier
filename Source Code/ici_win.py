from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from scipy.spatial import KDTree
from webcolors import (css3_hex_to_names, hex_to_rgb)
import sys
import os
#Loading the image
def load_image():
    #Get results in HEX
    def results_hex():
        img = (Image.open(image_dir)).resize((10,10), Image.ANTIALIAS)
        img.convert('RGB')
        width, height = img.size
        colors = []
        for x in range(0, width):
            for y in range(0, height):
                r, g, b = img.getpixel((x,y))
                colors.append(img.getpixel((x,y)))
        resultsHEX_window = Tk()
        resultsHEX_window.resizable(True, True)
        resultsHEX_window.geometry("250x450")
        resultsHEX_window.title("HEX RESULTS")
        listbox = Listbox(resultsHEX_window, width=35)
        listbox.pack(side = LEFT, fill = BOTH)
        scrollbar = Scrollbar(resultsHEX_window)
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
        resultsHEX_window.mainloop()
    #Get results in RGB
    def results_rgb():
        img = (Image.open(image_dir)).resize((10,10), Image.ANTIALIAS)
        img.convert('RGB')
        width, height = img.size
        colors = []
        for x in range(0, width):
            for y in range(0, height):
                r, g, b = img.getpixel((x,y))
                colors.append(img.getpixel((x,y)))
        resultsHEX_window = Tk()
        resultsHEX_window.resizable(True, True)
        resultsHEX_window.geometry("250x450")
        resultsHEX_window.title("RGB RESULTS")
        listbox = Listbox(resultsHEX_window, width=35)
        listbox.pack(side = LEFT, fill = BOTH)
        scrollbar = Scrollbar(resultsHEX_window)
        scrollbar.pack(side = RIGHT, fill = BOTH)
        result_rgb = []
        for values in colors:
            if values not in result_rgb:
                result_rgb.append(values)
        result_hex =[]
        for items in result_rgb:
            result_hex.append("#" + str('%02x%02x%02x' % items))
        for items in result_rgb:
            listbox.insert(END, items)
        count = 0
        for items in result_hex:
            listbox.itemconfig(count, {'bg':(str(result_hex[count]))})
            count = count + 1
        listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = listbox.yview)
        resultsHEX_window.mainloop()
    #Get results in CSS colors
    def results_webcolors():
        img = (Image.open(image_dir)).resize((10,10), Image.ANTIALIAS)
        img.convert('RGB')
        width, height = img.size
        colors = []
        for x in range(0, width):
            for y in range(0, height):
                r, g, b = img.getpixel((x,y))
                colors.append(img.getpixel((x,y)))
        resultsHEX_window = Tk()
        resultsHEX_window.resizable(True, True)
        resultsHEX_window.geometry("250x450")
        resultsHEX_window.title("WEB COLORS CSS3 RESULTS")
        listbox = Listbox(resultsHEX_window, width=35)
        listbox.pack(side = LEFT, fill = BOTH)
        scrollbar = Scrollbar(resultsHEX_window)
        scrollbar.pack(side = RIGHT, fill = BOTH)
        def convert_rgb_to_names(rgb_tuple):
            css3_db = css3_hex_to_names
            names = []
            rgb_values = []
            for color_hex, color_name in css3_db.items():
                names.append(color_name)
                rgb_values.append(hex_to_rgb(color_hex))
            
            kdt_db = KDTree(rgb_values)
            distance, index = kdt_db.query(rgb_tuple)
            return f'Closest match: {names[index]}'
        result_rgb = []
        for values in colors:
            if values not in result_rgb:
                result_rgb.append(values)
        result_hex =[]
        for items in result_rgb:
            result_hex.append("#" + str('%02x%02x%02x' % items))
        results_webcolorlist = []
        for items in result_rgb:
            results_webcolorlist.append(convert_rgb_to_names((items)))
        for items in results_webcolorlist:
            listbox.insert(END, items)
        count = 0
        for items in result_hex:
            listbox.itemconfig(count, {'bg':(str(result_hex[count]))})
            count = count + 1
        listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = listbox.yview)
        resultsHEX_window.mainloop()
    #Exict Function
    def exit():
        sys.exit()
    image_dir = filedialog.askopenfilename()
    img= (Image.open(image_dir))
    resized_image= img.resize((300,400), Image.ANTIALIAS)
    img_forshow = ImageTk.PhotoImage(resized_image)
    panel = Label(aci_window, image = img_forshow)
    panel.image = img_forshow
    panel.pack(pady=30 , fill = "none", expand = "no")
    image_button.configure(text = "Exit", command = exit)
    hex_button = Button(aci_window, width=25, height=2, bg = "white", fg = "black", text="HEX Results", font="Arial 14", command = results_hex)
    hex_button.pack(pady=15)
    rgb_button = Button(aci_window, width=25, height=2, bg = "white", fg = "black", text="RGB Results", font="Arial 14", command = results_rgb)
    rgb_button.pack(pady=15)
    webcolors_button = Button(aci_window, width=25, height=2, bg = "white", fg = "black", text="WEB COLORS CSS3 Results", font="Arial 14", command = results_webcolors)
    webcolors_button.pack(pady=15)
#Main window
aci_window = Tk()
aci_window.resizable(True, True)
aci_window.geometry("500x900")
aci_window.title("Image Colors Identifier")
aci_window.configure(bg = "gray8")
#---ATTENTION---
aci_window.iconbitmap((os.path.join(sys.path[0], "windowIcon.ico"))) #Not working on Pyinstaller Windows Builds
#---ATTENTION---
image_button = Button(aci_window, width=25, height=2, bg = "white", fg = "black", text="Load image (.JPG)", font="Arial 14", command = load_image)
image_button.pack(pady=15)
autor_label = Label(aci_window, width=25, height = 2, bg = "white", fg = "black", text="Baskerville Inc. SH. v2.1")
autor_label.pack(pady=15)
aci_window.mainloop()
