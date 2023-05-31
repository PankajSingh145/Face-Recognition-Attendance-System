from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import face_recognition

class Training_data:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1840x720+0+0")
        self.root.title("Face Recognition Attendence System")

        img = Image.open(r"college images\upper_bg.png")
        img = img.resize((1840,720),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x= 0,y=0,width=1840,height=120)

        title_lbl = Label(f_lbl, text="Train Data",font=("times new roman",28,"bold"),fg="black",bg="white")
        title_lbl.place(x = 150,y=50,width=1000,height=30)
        

        train_btn = Button(self.root,command=self.train_classifier,text="Train Data",font=("times new roman",12,"bold"),bg="green",fg="white")
        train_btn.place(x=480,y=240,width=350,height=40)
    
    # ============= Fuction for train =============
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Train Data",imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        # =============== Train te classifier and Save ===============

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Your data is Trained.")



if __name__ == "__main__":
    root = Tk()
    obj = Training_data(root)
    root.mainloop()
    