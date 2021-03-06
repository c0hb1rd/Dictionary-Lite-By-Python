#!/usr/bin/env python
# coding=utf-8
__author__ = 'c0hb1rd'
import requests
import re
import Tkinter


class MyWindow(Tkinter.Tk):
    def __init__(self, title, event=None):
        self.window = Tkinter.Tk(className=title)
        self.window.wm_minsize(320, 320)
        self.window.bind("<Escape>", lambda e: self.window.quit())
        self.edit = self.new_edit(20, 20)
        self.edit.bind('<Return>', self.refresh_result)
        self.edit.bind('<Control-BackSpace>', lambda e:self.edit.delete(0, len(self.edit.get()))) 
        self.new_button('Translate', 20 + 150, 20 - 5, self.refresh_result).bind('<Return>', self.refresh_result)
        self.list = []

    def new_label(self, text=None, x=None, y=None):
        label = Tkinter.Label(self.window, text=text)
        label.place(x=x, y=y)
        return label

    def new_edit(self, x=None, y=None):
        entry = Tkinter.Entry(self.window, width=15)
        entry.place(x=x, y=y)
        entry.focus()
        return entry

    def new_button(self, text=None, x=None, y=None, bind=None):
        button = Tkinter.Button(self.window, text=text, command=bind)
        button.place(x=x, y=y)
        return button

    def refresh_result(self, event=None):
        x, y = 20, 20
        for i in self.list:
            i.place_forget()
        y = 20
        value = self.edit.get()
        url = r'http://dict.youdao.com/search?q=%s&keyfrom=dict.index' % value
        response = requests.get(url)
        content = response.text
        REGX = r'li>(\w.*)</li>'
        result = re.findall(REGX, content)
        ls = []
        for value2 in set(result):
            ls.append(value2)
        ls = sorted(ls)
        for value in ls:
            y += 25
            self.list.append(self.new_label(value, x, y))

    def mainloop(self):
        self.window.mainloop()

MyWindow(' Dict').mainloop()
