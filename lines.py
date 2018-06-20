#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
"""
ZetCode Tkinter tutorial

This script draws lines on
the Canvas.

Author: Jan Bodnar
Last modified: July 2017
Website: www.zetcode.com
http://zetcode.com/gui/tkinter/drawing/
"""

from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        #canvas.create_line(15, 25, 200, 25)
        #canvas.create_line(15, 25, 200, 25, fill = "#00f" , width=5)
        #canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        #canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

        i = 0
        j = 0
        while (i < 16):
            canvas.create_line(250, 250, math.cos(j) * 250 + 250, math.sin(j) * 250 + 250)
            j += math.pi / (8)
            i += 1
        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example()
    root.geometry("400x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
