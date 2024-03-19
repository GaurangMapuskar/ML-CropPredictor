
import tkinter
from tkinter import *

root = Tk()

root.title('This is our Mini-Project')
root.geometry("1920x1080")

# define image
bg = PhotoImage(file="C:\\Users\\ASUS\\Desktop\\farm.png")
crop_predictor = PhotoImage(file="C:\\Users\\ASUS\\Desktop\\farm.png")
yield_predictor = PhotoImage(file="C:\\Users\\ASUS\\Desktop\\farm.png")
crop_analysis = PhotoImage(file="C:\\Users\\ASUS\\Desktop\\farm.png")
# create a canvas
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
my_canvas = Canvas(root, width=1920, height=1080, yscrollcommand=scrollbar.set)

my_canvas.pack(fill="both", expand=True)

# set image in canvas
my_canvas.create_image(0, 0, image=bg, anchor="nw")

# add a label
text = Text(root, width=50, height=10)
text.insert(END, "Deep well drained loamy soils are the best for the cultivation of sweet orange. Heavy soils, if well drained, yield good crops but cultivation become difficult. The pH of soil should be 6.5 to 7.5 and EC of water should be less than 1.0. Plant is highly sensitive to water-logged soils. A dry climate with about 50-75 cm of rainfall from June-September and with well defined summer and winter season is ideal.\n\n Sweet orange can be grown even upto an elevation of 900m above mean sea level. The extreme of temperature are necessary for achieving higher yield. Temperature 25°C is most ideal and extreme cold and high temperatures are determinate.")

# add the text widget to the window
text.pack()

root.mainloop()
