from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help :
    def __init__(self,root):
        self.root=root
        self.root. geometry ( "1530x790+0+0")
        self.root.title("face Recogniton System")

        title_lbl = Label(self.root, text="HELP DESK ",font=("helvetica", 25,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
# img 1
        img_top=Image.open(r"Images\help2.jpg")
        img_top=img_top.resize((1530,710),Image.Resampling.LANCZOS) 
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=40,width=1530,height=720)

        help_lbl = Label(f_lb1, text="Email: paritoshpal7796@gmail.com",font=("helvetica", 20,"bold"),bg="beige",fg="black")
        help_lbl.place(x=550,y=460)

        help_lb2 = Label(f_lb1, text="Contact: 9403191396",font=("helvetica", 20,"bold"),bg="beige",fg="black")
        help_lb2.place(x=550,y=499)




        
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()

