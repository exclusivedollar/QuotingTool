from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Qouting Tool')
root.iconbitmap("C:/Users/SammyM/Documents/Lombard/Project1/Building/LI.ico")


my_img = ImageTk.PhotoImage(Image.open("C:/Users/SammyM/Documents/Lombard/Project1/Building/MA.png"))
my_label = Label(image=my_img)
my_label.pack()












button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()






root.mainloop()