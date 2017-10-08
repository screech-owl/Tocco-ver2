# -*- coding: utf-8 -*-
import tkinter
import serial
import time

import tkinter as tk
root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

def Roop(event):
    for var in range(0, 100000):
        ++var
        ser = serial.Serial("COM3")  # Arduinoが接続されているコムポートを指定
        print(ser.readline())
        ser.close()
        time.sleep(2)
    print("End")

Button = tkinter.Button(text=u'ボタンです', width=50)
# 左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド
Button.pack()
Button.bind("<Button-1>", Roop)
root.mainloop()

if __name__ == '__Roop__':
    Roop()
