from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1840x720+0+0")
        self.root.title("Face Recognition Attendence System")

        #===================Variables =====================
        self.var_course=StringVar()
        self.var_department=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_name=StringVar()
        self.var_rollno=StringVar()
    

        #First Background Image
        img = Image.open(r"college images\upper_bg.png")
        img = img.resize((1840,720),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)


        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x= 0,y=0,width=1840,height=120)


        title_lbl = Label(f_lbl, text="STUDENT DETAILS",font=("times new roman",28,"bold"),fg="black",bg="white")
        title_lbl.place(x = 150,y=50,width=1000,height=30)

        img1 = Image.open(r"college images\background.jpeg")
        img1 = img1.resize((1500,600),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        
        bg_img = Label(self.root,image=self.photoimg1)
        bg_img.place(x = 0,y=120,width=1800,height=720)

        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=0,y=0,width=1740,height=650)


        #Left Frame 
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=650,height=550)
        
        #Current Lable Frame
        Current_left_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="BAISC DETAILS",font=("times new roman",12,"bold"))
        Current_left_frame.place(x=10,y=10,width=620,height=170)


        #Courses
        
        course_lable = Label(Current_left_frame,text="COURSE",font=("times new roman",12))
        course_lable.grid(row=0,column=0,sticky=W)

        course_combo = ttk.Combobox(Current_left_frame,textvariable=self.var_course,font=("times new roman",12),state=" readonly")
        course_combo["values"]=('SELECT COURSE',"B.Tech","B.Sc","M.Sc")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=10,pady=8,sticky=W)
        
        
        #DEPARTEMENT
        dep_lable = Label(Current_left_frame,text="DEPARMENT",font=("times new roman",12))
        dep_lable.grid(row=0,column=2,sticky=W)

        dep_combo = ttk.Combobox(Current_left_frame,textvariable=self.var_department,font=("times new roman",12),state=" readonly")
        dep_combo["values"]=('SELECT DEPARMENT',"CSE","ECE","EE","CE","ME","Other")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=10,pady=8,sticky=W)
        
        #Year
        
        year_lable = Label(Current_left_frame,text="YEAR",font=("times new roman",12))
        year_lable.grid(row=1,column=0,sticky=W)

        year_combo = ttk.Combobox(Current_left_frame,textvariable=self.var_year,font=("times new roman",12),state=" readonly")
        year_combo["values"]=('SELECT YEAR',"2019","2020","2021","2022","2023","Other")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=8,sticky=W)
        
        
        #SEMISTER
        Sem_lable = Label(Current_left_frame,text="SEMISTER",font=("times new roman",12))
        Sem_lable.grid(row=1,column=2,sticky=W)

        Sem_combo = ttk.Combobox(Current_left_frame,textvariable=self.var_sem,font=("times new roman",12),state=" readonly")
        Sem_combo["values"]=('SELECT SEM',1,2,3,4,5,6,7,8)
        Sem_combo.current(0)
        Sem_combo.grid(row=1,column=3,padx=10,pady=8,sticky=W)

        #Class Student Details

        Class_student_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="CLASS DETAILS",font=("times new roman",12,"bold"))
        Class_student_frame.place(x=10,y=180,width=620,height=170)

        #STUDENT ID ENTRY

        student_ID = Label(Class_student_frame,text="Name",font=("times new roman",12))
        student_ID.grid(row=0,column=0,sticky=W)
        student_entry_ID = Entry(Class_student_frame,textvariable=self.var_rollno,width=20,font=("Courier",13,))
        student_entry_ID.grid(row=0,column=1,padx=2,pady=5)
        
        #STUDENT NAME
        student_ID = Label(Class_student_frame,text="Student ID",font=("times new roman",12))
        student_ID.grid(row=0,column=3,sticky=W)
        student_entry_ID = Entry(Class_student_frame,textvariable=self.var_name,width=20,font=("Courier",13,))
        student_entry_ID.grid(row=0,column=4,padx=2,pady=5)


        # GENDER
        self.var_gender = StringVar()
        student_ID = Label(Class_student_frame,text="GENDER",font=("times new roman",12))
        student_ID.grid(row=1,column=0)
        Student_combo = ttk.Combobox(Class_student_frame,textvariable=self.var_gender,font=("times new roman",12),state=" readonly")
        Student_combo["values"]=('SELECT',"MALE","FEMALE","OTHER")
        Student_combo.current(0)
        Student_combo.grid(row=1,column=1,padx=2,pady=5)
        

        # #DOB
        # self.var_dob = StringVar()
        # student_dob_ID = Label(Class_student_frame,text="DOB",font=("times new roman",12))
        # student_dob_ID.grid(row=1,column=3)
        # student_dob_entry_ID = Entry(Class_student_frame,textvariable=self.var_dob,width=20,font=("Courier",13,))
        # student_dob_entry_ID.grid(row=1,column=4,padx=2,pady=5)

        #radio button
        self.var_radio1 = StringVar()
        radiobutton1 = ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobutton1.grid(row=2,column=0)
        #radio button 2
        radiobutton2 = ttk.Radiobutton(Class_student_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobutton2.grid(row = 2,column=1)
        #Button Frame
        Button_frame = LabelFrame(left_frame,bd=2,relief=RIDGE)
        Button_frame.place(x=10,y=360,width=620,height=70)
        #Save Button
        save_btn = Button(Button_frame,command=self.add_data,text="Save",width=16,font=("times new roman",12,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)
        #Update Button
        update_btn = Button(Button_frame,command=self.update_data,text="Update",width=16,font=("times new roman",12,"bold"),bg="orange",fg="white")
        update_btn.grid(row=0,column=1)
        #Delete Button
        delete_btn = Button(Button_frame,command=self.delete_data,text="Delete",width=16,font=("times new roman",12,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=2)
        #Reset Button
        reset_btn = Button(Button_frame,command=self.reset_data,text="Reset",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        #Take a photo samples
        take_photos_btn = Button(Button_frame,command=self.generate_dataset,text="Collect Sample",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photos_btn.grid(row=1,column=0)
        #update a photo samples
        update_photos_btn = Button(Button_frame,text="Update Sample",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photos_btn.grid(row=1,column=1)


        #right Frame 
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        Right_frame.place(x=670,y=10,width=650,height=550)
        #Search Frame
        search_frame = LabelFrame(Right_frame,bd=2,relief=RIDGE,text="SEARCH DETAILS",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=10,width=620,height=100)
        # ============Lables=============
        search_lable = Label(search_frame,text="SEARCH BY: ",font=("times new roman",12))
        search_lable.grid(row=0,column=0,sticky=W)
        Search_combo = ttk.Combobox(search_frame,font=("times new roman",12),state=" readonly",width=8)
        Search_combo["values"]=('SELECT',"Name","Roll No")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=10,pady=8,sticky=W)
        #Search Entry
        search_entry = Entry(search_frame,width=16,font=("Courier",13,))
        search_entry.grid(row=0,column=2,padx=2,pady=5)
        #Search Button
        search_btn = Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="green",fg="white")
        search_btn.grid(row=0,column=3)
        #Show All Button
        search_all_btn = Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_all_btn.grid(row=0,column=4)
        tables_frame = LabelFrame(Right_frame,bd=2,relief=RIDGE)
        tables_frame.place(x=10,y=110,width=620,height=400)
        scroll_x = ttk.Scrollbar(tables_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tables_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(tables_frame,columns=('course','Dep','year','sem','name','rollno','photos'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("course",text="Course")
        self.student_table.heading('Dep',text="Department")
        self.student_table.heading('year',text="Year")
        self.student_table.heading('sem',text="Semister")
        self.student_table.heading('name',text="Student ID")
        self.student_table.heading("rollno",text="Name")
        self.student_table.heading("photos",text="Photos")
        self.student_table["show"]="headings"

        self.student_table.column('course',width=100)
        self.student_table.column('Dep',width=100)
        self.student_table.column('year',width=100)
        self.student_table.column('sem',width=100)
        self.student_table.column('name',width=100)
        self.student_table.column('rollno',width=100)
        self.student_table.column('photos',width=100)
       

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    # ==================== Function Declaration ================
    def add_data(self):
        if self.var_course.get() == 'SELECT COURSE' or self.var_department.get() == 'SELECT DEPARTMENT' or self.var_year.get() =='SELECT YEAR' or self.var_name.get()=="":
            messagebox.showerror("ERROR","Please fill required details.")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="123456789@Pankaj",database="facerecognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_course.get(),
                                                                                    self.var_department.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_sem.get(),
                                                                                    self.var_name.get(),
                                                                                    self.var_rollno.get(),
                                                                                    self.var_radio1.get()
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added successfully.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
# ======================= fetch data ===================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="123456789@Pankaj",database="facerecognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    
    # ================= get cursor =====================
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_course.set(data[0])
        self.var_department.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_name.set(data[4])
        self.var_rollno.set(data[5])
        self.var_radio1.set(data[6])

    # ===================== Update fuction =============
    def update_data(self):
        if self.var_course.get() == 'SELECT COURSE' or self.var_department.get() == 'SELECT DEPARTMENT' or self.var_year.get() =='SELECT YEAR' or self.var_name.get()=="":
            messagebox.showerror("ERROR","Please fill required details.")
        else:
            try:
                Update = messagebox.askyesno("UPDATE","Do you want to update?",parent= self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="123456789@Pankaj",database="facerecognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set course = %s,Dep=%s,year=%s,sem=%s,Rollno=%s,Photosample=%s where name = %s",(
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_department.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_sem.get(),
                                                                                                                    self.var_rollno.get(),
                                                                                                                    self.var_radio1.get(),
                                                                                                                    self.var_name.get()

                                                                                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details Updated!",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f'Due to {str(es)}',parent=self.root)
    
    # =================== Delete function =============

    def delete_data(self):
        if self.var_name.get()=="":
            messagebox.showerror("Error","Please Select First!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="123456789@Pankaj",database="facerecognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where name = %s"
                    val = (self.var_name.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)
    
    
    # ========= reset data ============
    def reset_data(self):
        self.var_course.set("SELECT COURSE")
        self.var_department.set("SELECT DEPARTMENT")
        self.var_year.set("SELECT YEAR")
        self.var_gender.set("SELECT")
        self.var_name.set("")
        self.var_rollno.set("")

    def generate_dataset(self):
        if self.var_course.get() == 'SELECT COURSE' or self.var_department.get() == 'SELECT DEPARTMENT' or self.var_year.get() =='SELECT YEAR' or self.var_name.get()=="":
            messagebox.showerror("ERROR","Please fill required details.")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="123456789@Pankaj",database="facerecognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set course = %s,Dep=%s,year=%s,sem=%s,Rollno=%s,Photosample=%s where name = %s",(
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_department.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_sem.get(),
                                                                                                                    self.var_rollno.get(),
                                                                                                                    self.var_radio1.get(),
                                                                                                                    self.var_name.get()

                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

        # =================== Load Predefined data from open cv ===========
                #If you want esp32 camera then you can use this command
                # url = "http://192.168.248.77:4747/video"
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_croped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    for(x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,frame_face = cap.read()
                    if face_croped(frame_face) is not None:
                        img_id+=1
                        face = cv2.resize(face_croped(frame_face),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user""."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,189),2)
                        cv2.imshow("Image Capture",face)

                    if cv2.waitKey(1)==13 or int(img_id==100):
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Success","Image Capture Success.👍")
                


            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}")

        

        






        





    
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()