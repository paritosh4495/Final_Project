from cProfile import label
from cgitb import handler, text
from lzma import MF_BT2
from tkinter import*
from tkinter import ttk
from tkinter import font
from turtle import title, width 
from PIL import Image,ImageTk
# from student import Student
from tkinter import messagebox
import mysql.connector
import cv2 


class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x700+0+0")
        self.root.title("Face Recognition System")

#          # Img1
#         img = Image.open(r"Images\\attendance.png")
#         img = img.resize((800,200),Image.Resampling.LANCZOS)
#         self.photoimg = ImageTk.PhotoImage(img)


#         f_lbl = Label(self.root,image=self.photoimg)
#         f_lbl.place(x=0,y=0,width=800,height=200)


# # Img 2
#         img1 = Image.open(r"Images\\attendance.png")
#         img1 = img1.resize((730,200),Image.Resampling.LANCZOS)
#         self.photoimg1 = ImageTk.PhotoImage(img1)


#         f_lbl = Label(self.root,image=self.photoimg1)
#         f_lbl.place(x=800,y=0,width=730,height=200)

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

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM",font=("helvetica", 25,"bold"),bg="white",fg="crimson")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1520,height=600)

         # #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("time new roman",12,"bold"))
        Left_frame.place(x=0,y=5,width=720,height=580)

        img_left=Image.open(r"Images\left.jpg")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS) 
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(Left_frame,image=self.photoimg_left)
        f_lb1.place(x=5,y=0,width=700,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=710,height=370)

        # Labels and Entries 

         #attendance id 
        attendanceId_label=Label(left_inside_frame,text="Attendance ID:",font=("time new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Name
        rollLabel=Label(left_inside_frame,text="Roll:",font=("time new roman",12,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=8)

        atten_roll=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=8)

        # Date
        nameLabel=Label(left_inside_frame,text="Name:",font=("time new roman",12,"bold"),bg="white")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        atten_name.grid(row=1,column=1, pady=7)

        # DEpt 
        depLabel=Label(left_inside_frame,text="Department:",font=("time new roman",12,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=7)

        atten_dep=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        atten_dep.grid(row=1,column=3,padx=7)

        #Time 
        timeLabel=Label(left_inside_frame,text="Time:",font=("time new roman",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=7)

        atten_time=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        atten_time.grid(row=2,column=1,padx=7)

        # Date
        dateLabel=Label(left_inside_frame,text="Date:",font=("time new roman",12,"bold"),bg="white")
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        atten_date.grid(row=2,column=3,pady=7)
        
        # Attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status:",font=("time new roman",12,"bold"),bg="white")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame, width=20,font="comicsansns 11 bold", state="readonly" )
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1,pady=7)
        self.atten_status.current(0)

         #bbuttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=70)

        save_btn=Button(btn_frame,text="Import csv",width=17,font=("times new roman",13,"bold"),bg="Beige",fg="black")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",width=17,font=("times new roman",13,"bold"),bg="Beige",fg="black")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="Beige",fg="black")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="Beige",fg="black")
        reset_btn.grid(row=0,column=3)

          # #right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("time new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=735,height=580)

        # img_right=Image.open(r"Images\right.png")
        # img_right=img_right.resize((700,130),Image.Resampling.LANCZOS) 
        # self.photoimg_right=ImageTk.PhotoImage(img_right)

        # f_lb1=Label(Right_frame,image=self.photoimg_right)
        # f_lb1.place(x=5,y=5,width=700,height=130)

        #   Right inside frame  table frame 

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=710,height=445)

        # Scroll bar and TABLE #######################
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

    
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
    

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        

       




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()


