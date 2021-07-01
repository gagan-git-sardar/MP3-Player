from tkinter import *
import pygame

root = Tk()

#initialize pygame mixer
pygame.mixer.init()

#create playlist box
song_box = Listbox(root, bg="black", fg="green", width=60)
song_box.pack(pady=20)

#define player control button
play_btn_img = PhotoImage(file="play.png")

#create player control frame
controls_frame = Frame(root)
controls_frame.pack()

#create player control buttons
play_button = Button(controls_frame,image=play_btn_img,borderwidth=0)

play_button.grid(row=0,column=0)

root.mainloop()
