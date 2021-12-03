# Baskerville Inc. 2021.
# Programmers:
#     - SH

from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
from scipy.spatial import KDTree
from webcolors import (css3_hex_to_names, hex_to_rgb)
import sys
import os

#Initial lists and variables
pixels = [10, 10] # The number of pixels changes the level of detail in the color detection

#Local path (This helps Pyinstaller to identify the path of the media like the window icon)
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Function (Loading the image and get the results)
def load_image(pixels):
    #Get results in HEX
    def results_hex():
        try:
            img = (Image.open(image_dir)).resize((int(pixels[0]), int(pixels[1])), Image.ANTIALIAS) # Changing the level of pixles in the image
        except:
            print("Error. .JPG IMAGE ")
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
        resultsHEX_window.iconbitmap(resource_path("windowIcon.ico"))
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
        global pixels
        try:
            img = (Image.open(image_dir)).resize((int(pixels[0]), int(pixels[1])), Image.ANTIALIAS)
        except:
            print("Error. .JPG IMAGE ")
        img.convert('RGB')
        width, height = img.size
        colors = []
        for x in range(0, width):
            for y in range(0, height):
                r, g, b = img.getpixel((x,y))
                colors.append(img.getpixel((x,y)))
        resultsRGB_window = Tk()
        resultsRGB_window.resizable(True, True)
        resultsRGB_window.geometry("250x450")
        resultsRGB_window.title("RGB RESULTS")
        resultsRGB_window.iconbitmap(resource_path("windowIcon.ico"))
        listbox = Listbox(resultsRGB_window, width=35)
        listbox.pack(side = LEFT, fill = BOTH)
        scrollbar = Scrollbar(resultsRGB_window)
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
        resultsRGB_window.mainloop()
    #Get results in CSS colors
    def results_webcolors():
        global pixels
        try:
            img = (Image.open(image_dir)).resize((int(pixels[0]), int(pixels[1])), Image.ANTIALIAS)
        except:
            print("Error. .JPG IMAGE ")
        img.convert('RGB')
        width, height = img.size
        colors = []
        for x in range(0, width):
            for y in range(0, height):
                r, g, b = img.getpixel((x,y))
                colors.append(img.getpixel((x,y)))
        resultsCSS_window = Tk()
        resultsCSS_window.resizable(True, True)
        resultsCSS_window.geometry("250x450")
        resultsCSS_window.title("WEB COLORS CSS3 RESULTS")
        resultsCSS_window.iconbitmap(resource_path("windowIcon.ico"))
        listbox = Listbox(resultsCSS_window, width=35)
        listbox.pack(side = LEFT, fill = BOTH)
        scrollbar = Scrollbar(resultsCSS_window)
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
        resultsCSS_window.mainloop()
    #Exit Function
    def exit():
        sys.exit()
    image_dir = filedialog.askopenfilename()
    try:
        img= (Image.open(image_dir))
    except:
        print("Error. Image not open")
    resized_image= img.resize((150,200), Image.ANTIALIAS)
    img_forshow = ImageTk.PhotoImage(resized_image)
    panel = Label(aci_window, image = img_forshow)
    panel.image = img_forshow
    panel.pack(pady=15 , fill = "none", expand = "no")
    image_button.configure(text = "Exit", height=1, command = exit)
    parematers_button.destroy()
    hex_button = Button(aci_window, width=25, height=1, bg = "white", fg = "black", text="HEX Results", font="Arial 14", command = results_hex)
    hex_button.pack(pady=7)
    rgb_button = Button(aci_window, width=25, height=1, bg = "white", fg = "black", text="RGB Results", font="Arial 14", command = results_rgb)
    rgb_button.pack(pady=7)
    webcolors_button = Button(aci_window, width=25, height=1, bg = "white", fg = "black", text="WEB COLORS CSS3 Results", font="Arial 14", command = results_webcolors)
    webcolors_button.pack(pady=7)
# This creates the GUI for setting up the pixels parameters
def parameters():
    parematers_button.configure(state= DISABLED)
    def save_parameters():
        global pixels
        pixels = []
        pixels.append(width_entry.get())
        pixels.append(height_entry.get())
        parameters_window.destroy()
    global pixels
    parameters_window = Tk()
    parameters_window.resizable(True, True)
    parameters_window.geometry("250x450")
    parameters_window.title("Parameters")
    def on_closing():
        if messagebox.askokcancel("Exit", "Exit without aplying changes?"):
            parematers_button.configure(state= NORMAL)
            parameters_window.destroy()
    parameters_window.protocol("WM_DELETE_WINDOW", on_closing)
    parameters_window.configure(bg = "gray8")
    parameters_window.iconbitmap(resource_path("windowIcon.ico"))
    parameters_label = Label(parameters_window, width=18, height = 2, bg = "white", fg = "black", text="Parameters")
    parameters_label.pack(pady=7)
    width_label = Label(parameters_window, width=15, height = 1, bg = "white", fg = "black", text="Width Pixels")
    width_label.pack(pady=7)
    width_entry = Entry(parameters_window, width=15, bg = "white", fg = "black")
    width_entry.pack(pady=3)
    width_entry.insert(0, str(pixels[0]))
    height_label = Label(parameters_window, width=15, height = 1, bg = "white", fg = "black", text="Height Pixels")
    height_label.pack(pady=7)
    height_entry = Entry(parameters_window, width=15, bg = "white", fg = "black")
    height_entry.pack(pady=3)
    height_entry.insert(0, str(pixels[1]))
    save_parematers_button = Button(parameters_window, width=15, height=1, bg = "white", fg = "black", text="Save Parameters", font="Arial 14", command = save_parameters)
    save_parematers_button.pack(pady=7)
    parameters_window.mainloop()
#Main window
aci_window = Tk()
aci_window.resizable(True, True)
aci_window.geometry("350x550")
aci_window.title("Image Colors Identifier")
aci_window.configure(bg = "gray8")
aci_window.iconbitmap(resource_path("windowIcon.ico"))
image_button = Button(aci_window, width=25, height=2, bg = "white", fg = "black", text="Load image (.JPG)", font="Arial 14", command = lambda:load_image(pixels))
image_button.pack(pady=7)
parematers_button = Button(aci_window, width=15, height=1, bg = "white", fg = "black", text="Parameters", font="Arial 14", command = parameters)
parematers_button.pack(pady=7)
autor_label = Label(aci_window, width=25, height = 2, bg = "white", fg = "black", text="Baskerville Inc. SH. v2.2")
autor_label.pack(pady=7)
aci_window.mainloop()
