from pytube import*
from tkinter   import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import*
file_size=0
def startDownload():
    global file_size

    try:
        url=urlField.get()
        #changing Button change
        dBtn.config(text="Please wait..")
        dBtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return
        # YouTube is an object
        ob = YouTube(url)
        # return a list throught stream object
        """strms = ob.streams.all()
        #ob has inner class streams and have all method
        for i in strms:
            print(i)
        """
        strm = ob.streams.all()
        strms = strm[1]
        file_size=strms.filesize
        strms.download(path_to_save_video)
        dBtn.config(text="start download")
        dBtn.config(state=NORMAL)
        showinfo("download finished","downloaded succesfully")
        urlField.delete(0,END)
    except Exception as e:
        print("YOU GET INVALID URL",e)
#Thread
def startDownloadThread():
    thread=Thread(target=startDownload)
    thread.start()
#starting GUI BUILDING
main=Tk()
main.title("YT DOWNLOADER")
#set the icon
main.iconbitmap("download.ico")

#set height
main.geometry("500x600")

#heading icon
file=PhotoImage(file='youtube.png')#key variable
headingIcon=Label(main,image=file)
headingIcon.pack(side=TOP,fill=X)
#pasete url
Pst=Label(main,text="PASTE  VIDEO URL HERE :",font=("bold",20))
Pst.pack(side=TOP,pady=10)
Pst.configure(bg="YELLOW")
#textfield
urlField=Entry(main,font=("verdana",18))
urlField.pack(side=TOP,fill=X,padx=10,pady=20)
#configure the background
main.configure(bg="orange")

#button download
dBtn=Button(main,text="Start download",font=("verdana",18),relief='ridge',command=startDownloadThread)
dBtn.pack(side=TOP)
dBtn.configure(bg="yellow")
main.mainloop()
