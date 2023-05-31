from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import os
import numpy as np
import urllib.request


class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1840x720+0+0")
        self.root.title("Face Recognition Attendence System")
        


        #Image 1
        img = Image.open(r"college images\reco.jpg")
        img = img.resize((920,720),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=720,height=620)

        #Image 2

        img_second = Image.open(r'college images/face_recognition.jpg')
        img_second = img_second.resize((840,720),Image.ANTIALIAS)
        self.second_photoimage = ImageTk.PhotoImage(img_second)
        
        second_lbl = Label(self.root,image=self.second_photoimage)
        second_lbl.place(x=720,y=0,width=680,height=620)

        face_recognition_btn = Button(second_lbl,command=self.face_recog,text="Face Recognition Start",font=("arial",15,"bold"),bg="green",fg="white")
        face_recognition_btn.place(x=150,y=520,width=350,height=60)
        title_lbl = Label(f_lbl, text="FACE RECOGNITION",font=("courier",24,"bold"),fg="white",bg="black")
        title_lbl.place(x =60,y=60,width=580,height=50)


        
        
        
    # ---------------------------------------- Mark Attendence ----------------------
    def mark_attendence(self,n,d,r):
        with open("attendence.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((n not in name_list) and (d not in name_list) and (r not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{d},{r},{dtString},{d1},Present")


        # -------------------------------- Face Recognition Function ---------------------------

    def face_recog(self):
            def draw_boundray(img,classifier,scaleFactor,minNeighbours,color,text,clf):
                
                gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)
                coord = []
                for (x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                    confidence = int((100*(1-predict/300)))

                    conn = mysql.connector.connect(host="localhost",username="root",password="123456789@Pankaj",database="facerecognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("select Rollno from student where name="+str(id))
                    n = my_cursor.fetchone()
                    print(n)
                    n ="+".join(list(n))

                    my_cursor.execute("select Dep from student where name="+str(id))
                    d = my_cursor.fetchone()
                    d ="+".join(list(d))

                    my_cursor.execute("select name from student where name="+str(id))
                    r = my_cursor.fetchone()
                    r ="+".join(list(r))
                                                              
                    if confidence >50:
                        cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Dep:{d}",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        self.mark_attendence(n,d,r)
                        print(n)
                    
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,f"Unkown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        # cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        print(confidence)
                        # print(n)
                    coord = [x,y,w,h]
                return coord
            
            def recognize(img,clf,faceCascade):
                coord = draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
                return img
            
            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            # url = "http://192.168.223.76:81/stream"
            url = "http://192.168.98.76:81/stream"
            stream = urllib.request.urlopen(url)

            bytes = b''

            while True:
                bytes += stream.read(1024)
                a = bytes.find(b'\xff\xd8')
                b = bytes.find(b'\xff\xd9')
                if a != -1 and b != -1:
                    jpg = bytes[a:b+2]
                    bytes = bytes[b+2:]
                    try:
                        frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

                        # Recognize faces in the current frame
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        # Detect faces in the grayscale image
                        recognize(frame,clf,faceCascade)
                        cv2.imshow('Face Recognition', frame)

                    except cv2.error as e:
                        print(f"Error decoding frame: {e}")
                        continue

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

            cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
    