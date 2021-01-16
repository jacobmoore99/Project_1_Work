import tkinter as tk
from tkinter import *
from tkinter import messagebox
import lyricsgenius
import math
import requests

print ("Start Program")
master = tk.Tk() #builds main window

def lyricSearch():
	print("RUNNING")

	genius = lyricsgenius.Genius("XLFgo7rC1mmbKLLQKVnImOqwp7K0BccjrMtbbSBp1YWVIxELhWgjVBTG22r8VxM2")
	artist = genius.search_artist((str(entry1.get())), max_songs=3, sort="title")
	song = genius.search_song((str(entry2.get())), artist.name)
	text1.insert(tk.END, "\n\n" + song.lyrics)

def clear():
	print("RUNNING")

	text1.delete('1.0', END)
	text1.insert(tk.END, "Lyrics will appear here")

def on_closing():
	print("Closing program...")
	if messagebox.askokcancel("Quit", "Do you want to quit?"):

		master.destroy()

def checkSelect():
	state = checkvar.get()

	if state == 1:
		print("High Contrast")
		master.config(bg = "black")
		w.config(bg = "black", fg="white")
		w1.config(bg = "black", fg="white")
		w3.config(bg = "black", fg="white")
		text1.config(bg = "black", fg = "white")
		check.config(fg = "white", bg = "black")
	else:
		print("Low Constrast")
		master.config(bg = "white")
		w.config(bg = "white", fg="purple")
		w1.config(bg = "white", fg="purple")
		w3.config(bg = "white", fg="purple")
		text1.config(bg = "white", fg = "black")
		check.config(fg = "black", bg = "white")

master.title ("Master Lyrics")

w = Label(master, text="MASTER LYRICS", fg="purple", font=("Arial", 30))
w.grid(row = 0, column = 0, columnspan = 9, sticky = "NESW")

w1 = Label(master, text="Search Artist:", fg="purple", font=("Arial", 18))
w1.grid(row = 1, column = 0)

canvas1 = tk.Canvas(master, width = 600, height = 300)
entry1 = tk.Entry (master)
canvas1.create_window(200, 140, window=entry1)
entry1.grid(row = 1, column = 2)

w3 = Label(master, text="Search Song:", fg="purple", font=("Arial", 18))
w3.grid(row = 1, column = 5)

canvas1 = tk.Canvas(master, width = 600, height = 300)
entry2 = tk.Entry (master)
canvas1.create_window(200, 140, window=entry2)
entry2.grid(row = 1, column = 8)

btn2 = tk.Button(master, width = 30, height = 2)
#step 2: configure the widget
btn2.config(text = "Find Lyrics", font=("Anton", 18, "bold"), highlightbackground = "purple", command = lyricSearch)
#step 3: place the widget - pack(), grid()
btn2.grid(row = 2, column = 0, columnspan = 5)

btn3 = tk.Button(master, width = 30, height = 2)
#step 2: configure the widget
btn3.config(text = "Clear", font=("Anton", 18, "bold"), highlightbackground = "grey", command=clear)
#step 3: place the widget - pack(), grid()
btn3.grid(row = 2, column = 5, columnspan = 4)

text1 = tk.Text(master, width = 100, height = 20)
text1.config(font=("Times", 14))
text1.insert(tk.END, "Lyrics will appear here:")
text1.grid(row = 4, column = 0, columnspan = 9)

checkvar = tk.IntVar()
check = tk.Checkbutton(master, text = "High Contrast", variable = checkvar, command = checkSelect)
check.config(anchor = tk.W)
check.grid(row = 5, column = 0, columnspan = 1)

master.protocol("WM_DELETE_WINDOW", on_closing)

mainloop()

print("End Program")