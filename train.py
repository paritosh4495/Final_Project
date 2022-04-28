from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
# 37


class Train:
    def __init__(self,root):
        self.root=root
        self.root. geometry ( "1530x790+0+0")
        self.root.title("face Recogniton System")

 # Img1
        img = Image.open(r"Images\banner.jpg")
        img = img.resize((1530,130))
        self.photoimg = ImageTk.PhotoImage(img)


        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=130)

        img3 = Image.open(r"Images\help2.jpg")
        img3 = img3.resize((1530,710))
        self.photoimg3 = ImageTk.PhotoImage(img3)


        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img, text="TRAIN DATA SET",font=("helvetica", 25,"bold"),bg="Beige",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # title_lbl = Label(self.root, text="TRAIN DATA SET ",font=("helvetica", 25,"bold"),bg="white",fg="maroon")
        # title_lbl.place(x=0,y=0,width=1530,height=45)

        # img_top=Image.open(r"Images\banner.jpg")
        # img_top=img_top.resize((1530,325),Image.ANTIALIAS) 
        # self.photoimg_top=ImageTk.PhotoImage(img_top)

        # f_lb1=Label(self.root,image=self.photoimg_top)
        # f_lb1.place(x=5,y=55,width=1530,height=325)
# Buttonn
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier ,cursor="hand2",font=("helvetica", 30,"bold"),bg="beige",fg="crimson")
        b1_1.place(x=0,y=380,width=550,height=60)

        # img_bottom=Image.open(r"Images\help2.jpg")
        # img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS) 
        # self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        # f_lb1=Label(self.root,image=self.photoimg_bottom)
        # f_lb1.place(x=5,y=440,width=1530,height=325)


    def train_classifier(self):
        data_dir = ("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L') #Converting image to grayscale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

    # ////Train the classifier and save 

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result"," Training data set Completed!!")






if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()



