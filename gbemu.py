import tkinter as tk
import time
import os
from pyboy import PyBoy
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

start = time.perf_counter()

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=500)
canvas.pack()

class button:
    def __init__(self, x=50, y=50, width=50, height=50, text=None, command=None):
        self.button = tk.Button(root, text=text, command = lambda: gamerun(command))
        self.button.place(x=x, y=y, width=width, height=height)

romlist = os.listdir('ROMs')
romlist2 = os.listdir('ROMs')

def gamerun(rom):
    pyboy = PyBoy(f"ROMs/{rom}")
    if rom:
        while not pyboy.tick():
            pass
            root.withdraw()

for i, rom in enumerate(romlist):
    if rom.endswith(".gbc"):
        romlist[i] = rom[:-4]
    if rom.endswith(".gb"):
        romlist[i] = rom[:-3]
    if rom.endswith(".state"):
        romlist.remove(rom)

if len(romlist) < 16:
    for x in range(16 - len(romlist)):
        romlist.append("")
        x += 1

class gamegrid:
    def __init__(self, dimensions, text1="", text2="", text3="", text4="", text5="", text6="", text7="", text8="",
                text9="", text10="", text11="", text12="", text13="", text14="", text15="", text16=""):
        self.dimensions = dimensions
        if self.dimensions == "4x4":
            if not text1 == "":
                game1 = button(5, 5, 118.75, 118.75, text1, romlist2[0])
            if not text2 == "":
                game2 = button(128.75, 5, 118.75, 118.75, text2, romlist2[1])
            if not text3 == "":
                game3 = button(252.5, 5, 118.75, 118.75, text3, romlist2[2])
            if not text4 == "":
                game4 = button(376.25, 5, 118.75, 118.75, text4, romlist2[3])
            if not text5 == "":
                game5 = button(5, 128.75, 118.75, 118.75, text5, romlist2[4])
            if not text6 == "":
                game6 = button(128.75, 128.75, 118.75, 118.75, text6, romlist2[5])
            if not text7 == "":
                game7 = button(252.5, 128.75, 118.75, 118.75, text7, romlist2[6])
            if not text8 == "":
                game8 = button(376.25, 128.75, 118.75, 118.75, text8, romlist2[7])
            if not text9 == "":
                game9 = button(5, 252.5, 118.75, 118.75, text9, romlist2[8])
            if not text10 == "":
                game10 = button(128.75, 252.5, 118.75, 118.75, text10, romlist2[9])
            if not text11 == "":
                game11 = button(252.5, 252.5, 118.75, 118.75, text11, romlist2[10])
            if not text12 == "":
                game12 = button(376.25, 252.5, 118.75, 118.75, text12, romlist2[11])
            if not text13 == "":
                game13 = button(5, 376.25, 118.75, 118.75, text13, romlist2[12])
            if not text14 == "":
                game14 = button(128.75, 376.25, 118.75, 118.75, text14, romlist2[13])
            if not text15 == "":
                game15 = button(252.5, 376.25, 118.75, 118.75, text15, romlist2[14])
            if not text16 == "":
                game16 = button(376.25, 376.25, 118.75, 118.75, text16, romlist2[15])

grid = gamegrid("4x4", romlist[0], romlist[1], romlist[2], romlist[3], romlist[4], romlist[5], romlist[6], romlist[7],
                romlist[8], romlist[9], romlist[10], romlist[11], romlist[12], romlist[13], romlist[14], romlist[15])

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 3)} seconds(s)')

root.mainloop()