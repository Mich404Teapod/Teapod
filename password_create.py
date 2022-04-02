from tkinter import *
import json
import webbrowser

def generator():
    password = open("pass.1", "w+")
    password.write("set pass:", passwordvalue)
    password.close()


root = Tk()
root.geometry("800x550")
root.minsize(250, 200)
root.title("Teapod")
root.iconbitmap("epiost.ico")
root.config(background='#353c3b')
# menu_bar
menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Générer", command=generator)
file_menu.add_command(label="Quitter", command=root.quit)
menu_bar.add_cascade(label="Projet", menu=file_menu)

passwordvalue = Entry(root)
passwordvalue.place(x = 15, y = 45)

root.config(menu=menu_bar)