from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train_data import Training_data
from face_recognition import Face_Recognition


class Face_recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1840x720+0+0")
        self.root.title("Face Recognition Attendence System")

        #First Background Image
        img = Image.open(r"college images\upper_bg.png")
        img = img.resize((1840,720),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)


        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x= 0,y=0,width=1840,height=120)


        title_lbl = Label(f_lbl, text="FACE RECOGNITION ATTENDENCE SYSTEM",font=("times new roman",28,"bold"),bg="white",fg="black")
        title_lbl.place(x = 150,y=50,width=1000,height=30)

        #Student Button
        img1 = Image.open(r"college images\background.jpeg")
        img1 = img1.resize((1500,600),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        #STUDENE IMAGE

        img2 = Image.open(r"college images\bi2.jpeg")
        img2 = img2.resize((320,150),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img2)

        # Attendence Image for Face Recognition
        img3 = Image.open(r"college images\bi3.jpg")
        img3 = img3.resize((320,150),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img3)

        # Face Recognitio Images
        img4 = Image.open(r"college images\bi4.jpg")
        img4 = img4.resize((320,150),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img4)


        bg_img = Label(self.root,image=self.photoimg1)
        bg_img.place(x = 0,y=120,width=1500,height=600)
        #Student Button
        b1 = Button(bg_img,image=self.photoimg3,command=self.student_details,cursor="hand2")
        b1.place(x=120,y=80,width=320,height=150)
        b1_1 = Button(bg_img,text="STUDENT DETAILS",command=self.student_details,font=("times new roman",15,"bold"),bg="black",fg="white",cursor="hand2")
        b1_1.place(x=120,y=200,width=320,height=40)


        #Face Detection Button

        b2 = Button(bg_img,command=self.train_data,image=self.photoimg4,cursor="hand2")
        b2.place(x=540,y=80,width=320,height=150)
        b2_1 = Button(bg_img,command=self.train_data,text="FACE TRAIN",font=("times new roman",15,"bold"),bg="black",fg="white",cursor="hand2")
        b2_1.place(x=540,y=200,width=320,height=40)


        #Face Recognition Button
        b3 = Button(bg_img,command=self.Face_Recognition,image=self.photoimg5,cursor="hand2")
        b3.place(x=930,y=80,width=320,height=150)
        b3_1 = Button(bg_img,command=self.Face_Recognition,text="FACE RECOGNITION",font=("times new roman",15,"bold"),bg="black",fg="white",cursor="hand2")
        b3_1.place(x=930,y=200,width=320,height=40)

        #Photo Button
        img5 = Image.open(r"college images\collage.jpg")
        img5 = img5.resize((320,150),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img5)


        #Face Recognition Button
        b4 = Button(bg_img,command=self.open_img,image=self.photoimg6,cursor="hand2")
        b4.place(x=120,y=380,width=320,height=150)
        b4_1 = Button(bg_img,command=self.open_img,text="Photos",font=("times new roman",15,"bold"),bg="black",fg="white",cursor="hand2")
        b4_1.place(x=120,y=500,width=320,height=40)

      
        


    def open_img(self):
        os.startfile("data")

    # ========================= Functions =========================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    # ============== train data function ==================
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Training_data(self.new_window)

     # ============== Face Recognition function ==================
    def Face_Recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    

        
    








if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_System(root)
    root.mainloop()