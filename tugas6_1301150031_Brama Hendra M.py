# -*- coding: utf-8 -*-
"""
Created on Sun Sep  30 17:19:29 2018

@author: Brama Hendra Mahendra
"""

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np

class tugasPCD:
    
    def __init__(self, master):
        self.master = master
        self.gui_size = (600, 600)
        self.gui(self.gui_size)
        self.height = 300

    def openImg(self): #untuk membuka file gambar
        self.dir = filedialog.askopenfilename() #popup file gambar yang akan dipilih
        temp = Image.open(self.dir) #buka gambar dari directory
        new_size = int((float(temp.size[0])*float(self.height / float(temp.size[1])))) #sesuaikan gambar dgn height (tinggi)
        self.img = temp.resize((new_size, self.height)) #resize gambar berdasarkan size yang ditentukan
        self.gambar = ImageTk.PhotoImage(self.img) #create image menjadi format ImageTk
        self.canvas.delete(ALL) #menghampus semua canvas yang sudah ada
        self.canvas.create_image(self.img.size[0]/2, self.img.size[1]/2, anchor=CENTER, image=self.gambar) #menampilkan image pada canvas
  

    def showImg(self):
        self.gambar = ImageTk.PhotoImage(self.img)
        self.canvas.delete(ALL)
        self.canvas.create_image(self.img.size[0]/2, self.img.size[1]/2, anchor=CENTER, image=self.gambar)



    def grayIn(self):
        gambar = self.img.copy()
        for x in range(gambar.size[0]):
            for y in range(gambar.size[1]):
                r, g, b = gambar.getpixel((x, y))
                gambar.putpixel((x, y), (int((r+g+b)/3), int((r+g+b)/3), int((r+g+b)/3)))
        self.img = gambar
        self.showImg()


    def zoomIn(self):
        gambar = Image.new("RGB", (self.img.size[0]*2, self.img.size[1]*2))
        for x in range(0, gambar.size[0], 2):
            for y in range(0, gambar.size[1], 2):
                r, g, b = self.img.getpixel((int(x/2), int(y/2)))
                gambar.putpixel((x, y), (r, g, b))
                gambar.putpixel((x+1, y), (r, g, b))
                gambar.putpixel((x, y+1), (r, g, b))
                gambar.putpixel((x+1, y+1), (r, g, b))
        self.img = gambar
        self.showImg()


    def zoomOut(self):
        gambar = Image.new("RGB", (int(self.img.size[0]/2), int(self.img.size[1]/2)))
        for x in range(0, self.img.size[0], 2):
            for y in range(0, self.img.size[1], 2):
                r, g, b = self.img.getpixel((x+1, y))
                r1, g1, b1 = self.img.getpixel((x+1, y))
                r2, g2, b2 = self.img.getpixel((x, y+1))
                r3, g3, b3 = self.img.getpixel((x+1, y+1))
                gambar.putpixel((int(x/2), int(y/2)), (int((r+r1+r2+r3)/4), int((g+g1+g2+g3)/4), int((b+b1+b2+b3)/4)))
        self.img = gambar
        self.showImg()
    
    def bright(self):
        gambar = self.img.copy()
        bright = 10
        for x in range(gambar.size[0]):
            for y in range(gambar.size[1]):
                r, g, b = gambar.getpixel((x, y))
                
                if(r<255-bright):
                    if(g<255-bright):
                        if(b<255-bright):
                            gambar.putpixel((x, y), (r+bright,g+bright,b+bright))
                        else:
                            gambar.putpixel((x, y), (r+bright,g+bright,255))
                    else:
                        gambar.putpixel((x, y), (r+bright,255,255))
                else:
                    gambar.putpixel((x, y), (255,255,255))

        self.img = gambar
        self.showImg()
    
    def dark(self):
        gambar = self.img.copy()
        dark = 10
        print(gambar.size[0])
        print(gambar.size[1])
        
        for x in range(gambar.size[0]):
            for y in range(gambar.size[1]):
                r, g, b = gambar.getpixel((x, y))
                
                if(r>0+dark):
                    if(g>0+dark):
                        if(b>0+dark):
                            gambar.putpixel((x, y), (r-dark,g-dark,b-dark))
                        else:
                            gambar.putpixel((x, y), (r-dark,g-dark,0))
                    else:
                        gambar.putpixel((x, y), (r-dark,0,0))
                else:
                    gambar.putpixel((x, y), (0,0,0))

        self.img = gambar
        self.showImg()
        
    def geserKanan(self):
        gambar = self.img.copy()
        img_temp = gambar.copy()
        geser = 10
        for x in range(gambar.size[0]):
            for y in range(gambar.size[1]):
                cek = x+geser
                if(x<=geser):
                    gambar.putpixel((x+geser, y), (0,0,0))
                elif(cek<gambar.size[0]):                    
                    r, g, b = img_temp.getpixel((x, y))
                    gambar.putpixel((x+geser, y), (r,g,b))
        self.img = gambar
        self.showImg()
        
    def geserKiri(self):
        gambar = self.img.copy()
        img_temp = gambar.copy()
        geser = 10
        for x in range(gambar.size[0]):
            for y in range(gambar.size[1]):
                cek = x+geser
                if(x>=gambar.size[0]-geser):
                    gambar.putpixel((x, y), (0,0,0))
                elif(x>=0 and x<gambar.size[0]-geser):                    
                    r, g, b = img_temp.getpixel((x+geser, y))
                    gambar.putpixel((x, y), (r,g,b))
        self.img = gambar
        self.showImg()
        
    def geserBawah(self):
        gambar = self.img.copy()
        img_temp = gambar.copy()
        geser = 10
        for x in range(gambar.size[0]):
            for y in range(gambar.size[1]):
                cek = y+geser
                if(y<=geser):
                    gambar.putpixel((x, y+geser), (0,0,0))
                elif(cek<gambar.size[1]):                    
                    r, g, b = img_temp.getpixel((x, y))
                    gambar.putpixel((x, y+geser), (r,g,b))
        self.img = gambar
        self.showImg()
        
    def geserAtas(self):
        gambar = self.img.copy()
        img_temp = gambar.copy()
        geser = 10
        for x in range(gambar.size[0]):
            for y in range(gambar.size[1]):
                cek = y+geser
                if(y>=gambar.size[1]-geser):
                    gambar.putpixel((x, y), (0,0,0))
                elif(y>=0 and y<gambar.size[1]-geser):                    
                    r, g, b = img_temp.getpixel((x, y+geser))
                    gambar.putpixel((x, y), (r,g,b))
        self.img = gambar
        self.showImg()
        
    def histogram(self):
        gambar = self.img.copy()
        arrR = np.zeros(255)
        arrG = np.zeros(255)
        arrB = np.zeros(255)
        for x in range(gambar.size[0]):
            for y in range(gambar.size[1]):
                r, g, b = gambar.getpixel((x, y))
                arrR[r] = arrR[r] +1
                arrG[g] = arrG[g] +1
                arrB[b] = arrB[b] +1
                
#        for i in range(arrR.size):
#            print(i," = ",arrR[i]," | ",arrG[i]," | ",arrB[i])
        plt.plot(range(0,255),arrR)
        plt.plot(range(0,255),arrG)
        plt.plot(range(0,255),arrB)
        plt.show()    
        
    def edgedetection(self):
        gambar = self.img.copy()
        mask = [[-1,-1,-1],
                [-1,8,-1],
                [-1,-1,-1]]
        
        for x in range(1,self.img.size[0]-1):
            for y in range(1,self.img.size[1]-1):
                r_sum = 0
                g_sum = 0
                b_sum = 0
                for i in range(3):
                    for j in range(3):
                        if(i==0 and j == 0):
                            r,g,b = self.img.getpixel((x-1,y-1))
                        elif (i==0 and j==1):
                            r,g,b = self.img.getpixel((x-1,y))
                        elif (i==0 and j==2):
                            r,g,b = self.img.getpixel((x-1,y+1))
                        elif (i==1 and j==0):
                            r,g,b = self.img.getpixel((x,y-1))
                        elif (i== 1 and j==1):
                            r,g,b = self.img.getpixel((x,y))
                        elif (i==1 and j==2):
                            r,g,b = self.img.getpixel((x,y+1))
                        elif (i==2 and j==0):
                            r,g,b = self.img.getpixel((x+1,y-1))
                        elif (i==2 and j==1):
                            r,g,b = self.img.getpixel((x+1,y))
                        elif (i==2 and j==2):
                            r,g,b = self.img.getpixel((x+1,y+1))
                            
#                        r,g,b = self.img.getpixel((x,y))
                        r_sum = r_sum + (r*mask[i][j])
                        b_sum = b_sum + (b*mask[i][j])
                        g_sum = g_sum + (g*mask[i][j])
                gambar.putpixel((x, y),(r_sum, g_sum, b_sum))      
        self.img = gambar
        self.showImg()
        
    def blurIn(self):
        gambar = self.img.copy()
        mask = [[1,1,1],
                [1,1,1],
                [1,1,1]]
        
        for x in range(1,self.img.size[0]-1):
            for y in range(1,self.img.size[1]-1):
                r_sum = 0.0
                g_sum = 0.0
                b_sum = 0.0
                for i in range(3):
                    for j in range(3):
                        if(i==0 and j == 0):
                            r,g,b = self.img.getpixel((x-1,y-1))
                        elif (i==0 and j==1):
                            r,g,b = self.img.getpixel((x-1,y))
                        elif (i==0 and j==2):
                            r,g,b = self.img.getpixel((x-1,y+1))
                        elif (i==1 and j==0):
                            r,g,b = self.img.getpixel((x,y-1))
                        elif (i== 1 and j==1):
                            r,g,b = self.img.getpixel((x,y))
                        elif (i==1 and j==2):
                            r,g,b = self.img.getpixel((x,y+1))
                        elif (i==2 and j==0):
                            r,g,b = self.img.getpixel((x+1,y-1))
                        elif (i==2 and j==1):
                            r,g,b = self.img.getpixel((x+1,y))
                        elif (i==2 and j==2):
                            r,g,b = self.img.getpixel((x+1,y+1))
                            
#                        r,g,b = self.img.getpixel((x,y))
                        m = mask[i][j] * (1/9)
                        r_sum = r_sum + (r*m)
                        b_sum = b_sum + (b*m)
                        g_sum = g_sum + (g*m)
#                print(r_sum,g_sum,b_sum)
                gambar.putpixel((x, y),(int(r_sum), int(g_sum), int(b_sum)))      
        self.img = gambar
        self.showImg()
        
    def sharpIn(self):
        gambar = self.img.copy()
        mask = [[0,-1,0],
                [-1,5,-1],
                [0,-1,0]]
        
        for x in range(1,self.img.size[0]-1):
            for y in range(1,self.img.size[1]-1):
                r_sum = 0
                g_sum = 0
                b_sum = 0
                for i in range(3):
                    for j in range(3):
                        if(i==0 and j == 0):
                            r,g,b = self.img.getpixel((x-1,y-1))
                        elif (i==0 and j==1):
                            r,g,b = self.img.getpixel((x-1,y))
                        elif (i==0 and j==2):
                            r,g,b = self.img.getpixel((x-1,y+1))
                        elif (i==1 and j==0):
                            r,g,b = self.img.getpixel((x,y-1))
                        elif (i== 1 and j==1):
                            r,g,b = self.img.getpixel((x,y))
                        elif (i==1 and j==2):
                            r,g,b = self.img.getpixel((x,y+1))
                        elif (i==2 and j==0):
                            r,g,b = self.img.getpixel((x+1,y-1))
                        elif (i==2 and j==1):
                            r,g,b = self.img.getpixel((x+1,y))
                        elif (i==2 and j==2):
                            r,g,b = self.img.getpixel((x+1,y+1))
                            
#                        r,g,b = self.img.getpixel((x,y))
                        r_sum = r_sum + (r*mask[i][j])
                        b_sum = b_sum + (b*mask[i][j])
                        g_sum = g_sum + (g*mask[i][j])
                gambar.putpixel((x, y),(r_sum, g_sum, b_sum))      
        self.img = gambar
        self.showImg()  
        
    def thresholdIn(self):
        atas = int(t1.get())
        bawah = int(t2.get())
        gambar = self.img.copy()
        for x in range(gambar.size[0]):
            for y in range(gambar.size[1]):
                r, g, b = gambar.getpixel((x, y))
                if(r >= atas and r <= bawah):
                    r = 255
                else:
                    r = 0
                if(g >= atas and g <= bawah):
                    g = 255
                else:
                    g = 0
                if(b >= atas and b <= bawah):
                    b = 255
                else:
                    b = 0
                
                gambar.putpixel((x, y), (r, g, b))
        self.img = gambar
        self.showImg()
        
        
#    def growIn(self):
#        if(0 <= x <= gmbar.size[0] and 0 <= y <= gmbar.size[1]):
#            r, g, b = gmbar.getpixel((x, y))
#            gray = int((r+g+b)/3)
#            if(bawah <= gray <= atas):
#                gmbar.putpixel((x, y), (seed, seed, seed))
#                growIn(self,seed,bawah,atas,x-1,y)
#                growIn(self,seed,bawah,atas,x+1,y)
#                growIn(self,seed,bawah,atas,x,y-1)
#                growIn(self,seed,bawah,atas,x,y+1)
            
    def regionGrowth(self):
        seed = int(A1.get())
        bawah = int(A1.get()) - int(A2.get())
        atas = int(A1.get()) + int(A2.get())
        gmbar = self.img.copy()
        cek = True
        gray = -999
        for x in range(gmbar.size[0]):
                for y in range(gmbar.size[1]):
                    r, g, b = gmbar.getpixel((x, y))
                    gray = int((r+g+b)/3)
                    gmbar.putpixel((x, y), (gray, gray, gray))
        
        while(cek==True):
            for x in range(1, gmbar.size[0]-1):
                for y in range(1,gmbar.size[1]-1):
                    g, g, g = gmbar.getpixel((x, y))
                    gray = g
                    if(bawah <= gray <= atas):
                        if any(a==seed for a in gmbar.getpixel((x+1, y))) or any(a==seed for a in gmbar.getpixel((x-1, y))) or any(a==seed for a in gmbar.getpixel((x, y-1))) or any(a==seed for a in gmbar.getpixel((x, y+1))):
                            gmbar.putpixel((x, y), (seed, seed, seed))
                            self.img = gmbar
                            self.showImg()
                            cek = False
#                if(gray == seed):
#                    cek = False
#                    break
#                if(cek == False):
#                    break
            if(cek == False):
                cek= True
            elif(cek ==True):
                break
                
        print("done")
        self.img = gmbar
        self.showImg()
        
    
        
    
    def gui(self, size):
        self.frame_open = Frame(self.master, bd=2, bg="White")

        self.canvas = Canvas(self.master, height = self.gui_size[1]*0.9, width=self.gui_size[0]*0.9)
        self.canvas.grid(row = 1)

        self.menu = Frame(self.master, pady=3)
        self.menu.grid(row = 4, sticky=W)
        
        Button(self.menu, text='Browse', command=self.openImg).grid(row=3, column=1,sticky=N+S+E+W)
        Button(self.menu, text='Grayscale', command=self.grayIn).grid(row=3, column=2,sticky=N+S+E+W)
        Button(self.menu, text='Zoom In', command=self.zoomIn).grid(row=3, column=3,sticky=N+S+E+W)
        Button(self.menu, text='Zoom Out', command=self.zoomOut).grid(row=3, column=4,sticky=N+S+E+W)
        Button(self.menu, text='Brightness', command=self.bright).grid(row=3, column=5,sticky=N+S+E+W)
        Button(self.menu, text='Darken', command=self.dark).grid(row=3, column=6,sticky=N+S+E+W)
        Button(self.menu, text='Kanan', command=self.geserKanan).grid(row=3, column=7,sticky=N+S+E+W)
        Button(self.menu, text='Kiri', command=self.geserKiri).grid(row=3, column=8,sticky=N+S+E+W)
        Button(self.menu, text='Bawah', command=self.geserBawah).grid(row=3, column=9,sticky=N+S+E+W)
        Button(self.menu, text='Atas', command=self.geserAtas).grid(row=3, column=10,sticky=N+S+E+W)
        Button(self.menu, text='Histogram', command=self.histogram).grid(row=3, column=11,sticky=N+S+E+W)
        Button(self.menu, text='Edge Decetection', command=self.edgedetection).grid(row=3, column=12,sticky=N+S+E+W)
        Button(self.menu, text='Blur', command=self.blurIn).grid(row=3, column=13,sticky=N+S+E+W)
        Button(self.menu, text='Sharp', command=self.sharpIn).grid(row=3, column=14,sticky=N+S+E+W)
        
        Label(self.menu, text='Threshold').grid(row=4, column=1,sticky=N+S+E+W)
        global t1 
        t1 = Entry(self.menu)
        global t2 
        t2 = Entry(self.menu)
        t1.grid(row=4, column=2,sticky=N+S+E+W)
        t2.grid(row=4, column=3,sticky=N+S+E+W)
        Button(self.menu, text='Ok', command=self.thresholdIn).grid(row=4, column=4,sticky=N+S+E+W)
        
        Label(self.menu, text='Region Growth').grid(row=5, column=1,sticky=N+S+E+W)
        global A1 
        A1 = Entry(self.menu)
        global A2 
        A2 = Entry(self.menu)
        A1.grid(row=5, column=2,sticky=N+S+E+W)
        A2.grid(row=5, column=3,sticky=N+S+E+W)
        Button(self.menu, text='Ok', command=self.regionGrowth).grid(row=5, column=4,sticky=N+S+E+W)
        


window = Tk()
window.title("Tugas 5 - 1301150031 - Brama Hendra Mahendra")
tugasPCD(window)
window.mainloop()