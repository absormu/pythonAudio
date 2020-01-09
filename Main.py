# pip install pygame
# python --version
# Python 3.6.9
# python3 Main.py
# pygame 1.9.6
# absoralvord07@gmail.com


import pygame
from tkinter import *


class PemutarMusik(Frame):


    def __init__(self,parent):
        Frame.__init__(self, parent)
        parent.geometry("300x200")
        self.parent = parent
        self.nama = StringVar()
        self.nama.set("Python Play Audio Mp3")

        self.buatTeks1()

        self.buatTombolPlay1()
        self.buatTombolStop1()
        self.buatTeks1()
        self.buatTombolPlay2()
        self.buatTombolStop2()


    def putarMusik1(self):
        try :
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load("audio1.mp3")
            pygame.mixer.music.play()
        except :
            pass

    def putarMusik2(self):
        try :
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load("audio2.mp3")
            pygame.mixer.music.play()
        except :
            pass


    def stopMusik1(self):
        try :
            pygame.mixer.music.stop()
        except:
            pass

    def stopMusik2(self):
        try:
            pygame.mixer.music.stop()
        except:
            pass


    def buatTeks1(self):
        Label(textvariable=self.nama, fg="black", bg="light blue", font="Verdana 8 bold").pack(fil=X)


    def buatTombolStop1(self):
        Button(text="Stop 1", command=self.stopMusik1).pack(fill=X)


    def buatTombolPlay1(self):
        Button(text="Play 1", command=self.putarMusik1).pack(fill=X)




    def buatTombolStop2(self):
        Button(text="Stop 2", command=self.stopMusik2).pack(fill=X)


    def buatTombolPlay2(self):
        Button(text="Play 2", command=self.putarMusik2).pack(fill=X)




root = Tk()
PemutarMusik(root)
mainloop()
pygame.quit()