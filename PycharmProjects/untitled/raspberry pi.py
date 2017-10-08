from tkinter import *
import serial
import pygame.mixer
from time import sleep
from multiprocessing import Process

root = Tk()
root.option_add('*font', ('FixedSys', 24))

buff = StringVar()
buff.set('')

Label(textvariable = buff).pack()

ser = serial.Serial("COM3")  # Arduinoが接続されているコムポートを指定バグが多いばあいはtryの中に戻す

# 時刻の表示
def show_time():
    try:

        inf=ser.readline()
        inf2=inf.decode('utf-8')
        print(inf2)
        temp=(inf[7:12])#シリアル通信はバイト型なのでfloat型に変換が必要
        press = (inf[27:34])
        hum = (inf[46:51])
        touch=(inf[54:59])
        temp2=temp.decode('utf-8')#最初にバイト型をstring型に変換
        temp3=float(temp2)#そのあとにfloat型に変換
        press2 = press.decode('utf-8')
        press3 = float(press2)
        hum2 = hum.decode('utf-8')
        hum3 = float(hum2)
        touch2=touch.decode('utf-8')
        touch3=float(touch2)
        print(temp3,press3,hum3,touch3)
        kion="\n温度は"+temp2+"度だよー"
        situdo = "\n\n湿度は" + hum2 + "%だよー"
        kiatsu="\n\n気圧は"+press2+"だよー"
        DI=0.81*temp3+0.01*hum3*(0.99*temp3-14.3)+46.3
        sisu="\n\n不快指数は"+"%f"%DI+"だよー"
        if DI<55:
            taikan="\nさむいね"
        elif 60>=DI>55 :
            taikan="\n肌寒いね"
        elif 65>=DI>60:
            taikan="\n何も感じないね"
        elif 70>=DI>65:
            taikan="\n快いね"
        elif 75>=DI>70:
            taikan="\n暑くないね"
        elif 80>=DI>75:
            taikan="\nちょっと暑いね"
        elif 85>=DI>80:
            taikan="\n暑くて汗が出るね"
        elif DI>85:
            taikan="\n暑くてたまらないね"

        if touch3<600:
            tatti="\nたっちー"
            audio()
        else:
            tatti="\n"

        inf3 = kion + situdo + kiatsu + sisu + taikan+tatti
        buff.set(inf3)
        #ser.close()#バグが多い場合は戻す
    except ValueError:
        show_time()
        print("エラーだよ")
    root.after(1000, show_time)

def audio():
    # mixerモジュールの初期化
    pygame.mixer.init()
    # 音楽ファイルの読み込み
    pygame.mixer.music.load("wanko_w01.ogg")
    # 音楽再生、および再生回数の設定(-1はループ再生)
    pygame.mixer.music.play(1)
    sleep(5)
    # 再生の終了
    pygame.mixer.music.stop()


show_time()
root.mainloop()