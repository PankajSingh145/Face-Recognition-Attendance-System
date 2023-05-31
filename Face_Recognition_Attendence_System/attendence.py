from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Attendence:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1840x720+0+0")
        self.root.title("Face Recognition Attendence System")

        
        #First Background Image
        img = Image.open(r"college images\bi2.jpeg")
        img = img.resize((920,140),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)


        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x= 0,y=0,width=920,height=140)

        #Second Image
        img_1 = Image.open(r"college images\bi3.jpg")
        img_1 = img_1.resize((920,140),Image.ANTIALIAS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        s_lbl = Label(self.root,image=self.photoimg_1)
        s_lbl.place(x=920,y=0,width=920,height=140)


        #Student Form for the attendence

        main_frame = Frame(self.root,bd=2)
        main_frame.place(x=0,y=0,width=1840,height=720)

        #Left Frame

        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=650,height=650)

        #department lbl

        department_lbl = Label(left_frame,text="Department",font=("times new roman",12))
        department_lbl.grid(row=0,column=0,padx=10,pady=8)

        #Image 
        
        #Combo
        department_combo = ttk.Combobox(left_frame,state="readonly")
        department_combo["values"] = ("Select","CSE","ECE","ME","CE","EE","Other")
        department_combo.current(0)
        department_combo.grid(row=0,column=1,padx=10,pady=10)

        #Student Name
        




if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop() 