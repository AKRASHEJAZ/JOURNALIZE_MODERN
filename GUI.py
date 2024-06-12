import customtkinter as ctk
import functionality as fxn
from PIL import Image
import sys

logo_img = ctk.CTkImage(dark_image=Image.open("BOOK.png"),size=(200,200))

window = ctk.CTk()
window.geometry('500x500')
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("Oceanix.json")

name = ctk.CTkLabel(window,text="JOURNALIZE",font=('Comic Sans',40),corner_radius=15,text_color='steelblue2')
name.place(relx=0.5, rely=0.1,anchor='center')

img = ctk.CTkLabel(window,image=logo_img,text='')
img.place(relx=0.7, rely=0.5,anchor='center')

b1=ctk.CTkButton(window, text ="ADD NOTE", command=lambda: fxn.Add_Gui(window),corner_radius=25)
b1.place(relx=0.2, rely=0.4,anchor='center')

b2=ctk.CTkButton(window, text ="READ NOTE", command=lambda: fxn.Read_Gui(window),corner_radius=25)
b2.place(relx=0.2, rely=0.5,anchor='center')

b3=ctk.CTkButton(window, text ="MODIFY NOTE", command=lambda: fxn.Modify_Gui(window),corner_radius=25)
b3.place(relx=0.2, rely=0.6,anchor='center')

b4=ctk.CTkButton(window, text ="DELETE NOTE", command=lambda: fxn.Delete_Gui(window),corner_radius=25)
b4.place(relx=0.2, rely=0.7,anchor='center')

b5=ctk.CTkButton(window, text ="QUIT", command=lambda: sys.exit(0),corner_radius=25)
b5.place(relx=0.2, rely=0.8,anchor='center')

window.mainloop()