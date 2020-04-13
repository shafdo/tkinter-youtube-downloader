from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from pytube import YouTube
import pytube
import subprocess
import re

class Program():
    def __init__(self):
        self.root = Tk()
        self.root.resizable(False, False)

        #GUI Starts
        self.layout()

        #GUI Ends
        self.root.mainloop()

    def layout(self):
        self.mainframe = Frame(self.root,width=600,height=150,bg="white")
        self.mainframe.grid(sticky="W")
        # self.mainframe.grid_propagate(0)


        heading = Label(self.mainframe, text = "Video URL", fg="blue", bg="white")
        heading.config(font=("Arial", 20))
        heading.grid(row=0,padx=10,pady=10,sticky="W")

        locationbtn = Button(self.mainframe, text="SELECT", padx=5, pady=5)
        locationbtn.grid(row=0,column=1, sticky=W,padx=5)
        locationbtn.bind("<Button-1>",self.locationget)

        exitbtn = Button(self.mainframe, text="Exit", padx=5, pady=5)
        exitbtn.grid(row=0,column=2, sticky=W,padx=5)
        exitbtn.bind("<Button-1>",self.exitprogram)

        self.urltab = Entry(self.mainframe,width=95,fg="grey",relief=GROOVE)
        self.urltab.insert(0,"Enter Your Video URL")
        self.urltab.bind("<FocusIn>", self.clear_placeholder)
        self.urltab.grid(row=1,column=0,padx=5)

        self.check = Button(self.mainframe, text="Proceed", bg="lightgreen")
        self.check.bind("<Button-1>",self.downloader)
        self.check.grid(row=2,column=0,sticky="W",pady=10,padx=15)
       
        self.currentstatus = Label(self.mainframe, text="STATUS  :  Wating For URL",padx=200, bg="lightgreen")
        self.currentstatus.grid(row=2,column=1, padx=50)
        



        #Frame Scroller
        self.videoContainer = Frame(self.root,width="600", height="350", bg="white")
        self.videoContainer.grid(row=3,sticky=W)

        p1080label = Label(self.videoContainer, text="Video 1080p", pady=10, padx=11)
        p720label = Label(self.videoContainer, text="Video 720p", pady=10, padx=15)
        p480label = Label(self.videoContainer, text="Video 480p", pady=10, padx=15)
        p360label = Label(self.videoContainer, text="Video 360p", pady=10, padx=15)
        p240label = Label(self.videoContainer, text="Video 240p", pady=10, padx=15)
        p144label = Label(self.videoContainer, text="Video 144p", pady=10, padx=15)

        #Changing Font Size
        p1080label.config(font=("Arial", 13))
        p720label.config(font=("Arial", 13))
        p480label.config(font=("Arial", 13))
        p360label.config(font=("Arial", 13))
        p240label.config(font=("Arial", 13))
        p144label.config(font=("Arial", 13))

        
        # Video status
        self.stat1 = Label(self.videoContainer, text="Not Avaliable", pady=12, padx=100, fg="red")
        self.stat2 = Label(self.videoContainer, text="Not Avaliable", pady=12, padx=100, fg="red")
        self.stat3 = Label(self.videoContainer, text="Not Avaliable", pady=12, padx=100, fg="red")
        self.stat4 = Label(self.videoContainer, text="Not Avaliable", pady=12, padx=100, fg="red")
        self.stat5 = Label(self.videoContainer, text="Not Avaliable", pady=12, padx=100, fg="red")
        self.stat6 = Label(self.videoContainer, text="Not Avaliable", pady=12, padx=100, fg="red")

        #Download buttons
        self.btn1 = Button(self.videoContainer, text="Download", padx=30, pady=9)
        self.btn1.bind("<Button-1>",self.btndownload1)
        self.btn2 = Button(self.videoContainer, text="Download", padx=30, pady=9)
        self.btn2.bind("<Button-1>",self.btndownload2)
        self.btn3 = Button(self.videoContainer, text="Download", padx=30, pady=9)
        self.btn3.bind("<Button-1>",self.btndownload3)
        self.btn4 = Button(self.videoContainer, text="Download", padx=30, pady=9)
        self.btn4.bind("<Button-1>",self.btndownload4)
        self.btn5 = Button(self.videoContainer, text="Download", padx=30, pady=9)
        self.btn5.bind("<Button-1>",self.btndownload5)
        self.btn6 = Button(self.videoContainer, text="Download", padx=30, pady=9)
        self.btn6.bind("<Button-1>",self.btndownload6)


        # Adding to the frame
        p1080label.grid(row=3)
        self.stat1.grid(row=3,column=1)
        self.btn1.grid(row=3,column=3)

        p720label.grid(row=4)
        self.stat2.grid(row=4,column=1)
        self.btn2.grid(row=4,column=3)

        p480label.grid(row=5)
        self.stat3.grid(row=5,column=1)
        self.btn3.grid(row=5,column=3)

        p360label.grid(row=6)
        self.stat4.grid(row=6,column=1)
        self.btn4.grid(row=6,column=3)

        p240label.grid(row=7)
        self.stat5.grid(row=7,column=1)
        self.btn5.grid(row=7,column=3)

        p144label.grid(row=8)
        self.stat6.grid(row=8,column=1)
        self.btn6.grid(row=8,column=3)


    #Sub Functions
    def clear_placeholder(self,event):
         self.urltab.delete("0", "end")
         self.urltab.config(fg="black")

    def exitprogram(self,event):
        if messagebox.askyesno('Verify', 'Do you Wish To quit?'):
            self.root.destroy()

        else:
            pass

    def locationget(self, event):
        self.folder_selected = filedialog.askdirectory()



    def downloader(self,event):
        self.check.config(bg="yellow")
        self.stat1.config(text="Not Avaliable",fg="red",padx=100,pady=12)
        self.btn1.config(bg="lightgrey", pady=9, padx=30)
        self.stat2.config(text="Not Avaliable",fg="red",padx=100,pady=12)
        self.btn2.config(bg="lightgrey", pady=9, padx=30)
        self.stat3.config(text="Not Avaliable",fg="red",padx=100,pady=12)
        self.btn3.config(bg="lightgrey", pady=9, padx=30)
        self.stat4.config(text="Not Avaliable",fg="red",padx=100,pady=12)
        self.btn4.config(bg="lightgrey", pady=9, padx=30)
        self.stat5.config(text="Not Avaliable",fg="red",padx=100,pady=12)
        self.btn5.config(bg="lightgrey", pady=9, padx=30)
        self.stat6.config(text="Not Avaliable",fg="red",padx=100,pady=12)
        self.btn6.config(bg="lightgrey", pady=9, padx=30)



        try:
            url = self.urltab.get()
            if not self.folder_selected:
                self.currentstatus.config(text="STATUS  :  SELECT A FOLDER TO DOWNLOAD", bg="red",padx=20)
            else:
                self.path = self.folder_selected

                print(url)

                yt = YouTube(url)
                yt_code = str(yt.streams.filter(file_extension='mp4',progressive=True).all()).split(",")

                print(yt_code)

                
                for i in yt_code:
                    if ('res="1080"p' in i):
                        print("Entered 1080p")
                        self.stat1.config(text="Avaliable",fg="green",padx=100,pady=12)
                        self.btn1.config(bg="yellow", pady=9, padx=30)
                        self.downloadlink1 = yt.streams.filter(file_extension='mp4', progressive=True).all()[yt_code.index(i)]

                    if ('res="720p"' in i):
                        print("Entered 720p")
                        self.stat2.config(text="Avaliable",fg="green",padx=100,pady=12)
                        self.btn2.config(bg="yellow", pady=9, padx=30)
                        self.downloadlink2 = yt.streams.filter(file_extension='mp4', progressive=True).all()[yt_code.index(i)]
                    
                    if ('res="480p"' in i):
                        print("Entered 480p")
                        self.stat3.config(text="Avaliable",fg="green",padx=100,pady=12)
                        self.btn3.config(bg="yellow", pady=9, padx=30)
                        self.downloadlink3 = yt.streams.filter(file_extension='mp4', progressive=True).all()[yt_code.index(i)]

                    if ('res="360p"' in i):
                        print("Entered 360p")
                        self.stat4.config(text="Avaliable",fg="green",padx=100,pady=12)
                        self.btn4.config(bg="yellow", pady=9, padx=30)
                        self.downloadlink4 = yt.streams.filter(file_extension='mp4', progressive=True).all()[yt_code.index(i)]

                    if ('res="240p"' in i):
                        print("Entered 240p")
                        self.stat5.config(text="Avaliable",fg="green",padx=100,pady=12)
                        self.btn5.config(bg="yellow", pady=9, padx=30)
                        self.downloadlink5 = yt.streams.filter(file_extension='mp4', progressive=True).all()[yt_code.index(i)]
                    
                    if ('res="144p"' in i):
                        print("Entered 144p")
                        self.stat6.config(text="Avaliable",fg="green",padx=100,pady=12)
                        self.btn6.config(bg="yellow", pady=9, padx=30)
                        self.downloadlink6 = yt.streams.filter(file_extension='mp4', progressive=True).all()[yt_code.index(i)]

                    self.currentstatus.config(text="STATUS  : Please Choose Prefered Video Quality", bg="lightgreen")
                    self.currentstatus.config(padx=20)
                    self.check.config(bg="lightgreen")
                
            
        except pytube.exceptions.RegexMatchError:
            self.currentstatus.config(padx=50)
            self.currentstatus.config(text="STATUS  :  Invalid Video URL", bg="red")

        except pytube.exceptions.VideoUnavailable:
            self.currentstatus.config(padx=50)
            self.currentstatus.config(text="STATUS  :  Video Unavailable", bg="red")

        except AttributeError:
            self.currentstatus.config(padx=50)
            self.currentstatus.config(text="STATUS  :  Select Folder", bg="red")



    def btndownload1 (self, event):
        self.downloadlink1.download(self.path)
        self.btn1.config(text="Downloaded",bg="lightgreen", pady=9, padx=30)
        self.stat1.config(text="Downloaded",fg="red",padx=100,pady=12)
    
    def btndownload2 (self, event):
        self.downloadlink2.download(self.path)
        self.btn2.config(text="Downloaded",bg="lightgreen", pady=9, padx=30)
        self.stat2.config(text="Downloaded",fg="red",padx=100,pady=12)
    
    def btndownload3 (self, event):
        self.downloadlink3.download(self.path)
        self.btn3.config(text="Downloaded",bg="lightgreen", pady=9, padx=30)
        self.stat3.config(text="Downloaded",fg="red",padx=100,pady=12)
    
    def btndownload4 (self, event):
        self.downloadlink4.download(self.path)
        self.btn4.config(text="Downloaded",bg="lightgreen", pady=9, padx=30)
        self.stat4.config(text="Downloaded",fg="red",padx=100,pady=12)
    
    def btndownload5 (self, event):
        self.downloadlink5.download(self.path)
        self.btn5.config(text="Downloaded",bg="lightgreen", pady=9, padx=30)
        self.stat5.config(text="Downloaded",fg="red",padx=100,pady=12)
    
    def btndownload6 (self, event):
        self.downloadlink5.download(self.path)
        self.btn6.config(text="Downloaded",bg="lightgreen", pady=9, padx=30)
        self.stat6.config(text="Downloaded",fg="red",padx=100,pady=12)

p = Program()



