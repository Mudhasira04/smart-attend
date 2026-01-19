############################################# IMPORTING ################################################
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2, os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time

############################################# FUNCTIONS ################################################

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

##################################################################################

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)

###################################################################################

def contact():
    mess._show(title='Contact us', message="Please contact us on : 'xxxxxxxxxxxxx@gmail.com' ")

###################################################################################

def check_haarcascadefile():
    exists = os.path.isfile(r"haarcascade_frontalface_default.xml")
    if not exists:
        mess._show(title='Some file missing', message='Please contact us for help')
        window.destroy()

###################################################################################

def save_pass():
    assure_path_exists(r"TrainingImageLabel/")
    exists1 = os.path.isfile(r"TrainingImageLabel\psd.txt")
    if exists1:
        tf = open(r"TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas is None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open(r"TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    op = old.get()
    newp = new.get()
    nnewp = nnew.get()
    if op == key:
        if newp == nnewp:
            txf = open(r"TrainingImageLabel\psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
            return
    else:
        mess._show(title='Wrong Password', message='Please enter correct old password.')
        return
    mess._show(title='Password Changed', message='Password changed successfully!!')
    master.destroy()

###################################################################################

def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False, False)
    master.title("Change Password")
    master.configure(background="white")
    lbl4 = tk.Label(master, text='    Enter Old Password', bg='white', font=('times', 12, ' bold '))
    lbl4.place(x=10, y=10)
    global old
    old = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
    old.place(x=180, y=10)
    lbl5 = tk.Label(master, text='   Enter New Password', bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='Confirm New Password', bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
    nnew.place(x=180, y=80)
    cancel = tk.Button(master, text="Cancel", command=master.destroy, fg="black", bg="red", height=1, width=25,
                       activebackground="white", font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48", height=1, width=25,
                      activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()

#####################################################################################

def psw():
    assure_path_exists(r"TrainingImageLabel/")
    exists1 = os.path.isfile(r"TrainingImageLabel\psd.txt")
    if exists1:
        tf = open(r"TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas is None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open(r"TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if password == key:
        TrainImages()
    elif password is None:
        pass
    else:
        mess._show(title='Wrong Password', message='You have entered wrong password')

######################################################################################

def clear():
    txt.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)

def clear2():
    txt2.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)

#######################################################################################

def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    assure_path_exists(r"StudentDetails/")
    assure_path_exists(r"TrainingImage/")
    serial = 0
    exists = os.path.isfile(r"StudentDetails\StudentDetails.csv")
    if exists:
        with open(r"StudentDetails\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial += 1
        serial = serial // 2
    else:
        with open(r"StudentDetails\StudentDetails.csv", 'a+', newline='') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
    Id = txt.get()
    name = txt2.get()
    if name.replace(" ", "").isalpha():
        cam = cv2.VideoCapture(0)
        harcascadePath = r"haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleNum += 1
                cv2.imwrite(rf"TrainingImage\{name}.{serial}.{Id}.{sampleNum}.jpg", gray[y:y + h, x:x + w])
                cv2.imshow('Taking Images', img)
            if cv2.waitKey(100) & 0xFF == ord('q') or sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = f"Images Taken for ID : {Id}"
        row = [serial, '', Id, '', name]
        with open(r'StudentDetails\StudentDetails.csv', 'a+', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        message1.configure(text=res)
    else:
        message.configure(text="Enter Correct name")

########################################################################################

def TrainImages():
    check_haarcascadefile()
    assure_path_exists(r"TrainingImageLabel/")
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # Fixed for OpenCV contrib
    harcascadePath = r"haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels(r"TrainingImage")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='No Registrations', message='Please Register someone first!!!')
        return
    recognizer.save(r"TrainingImageLabel\Trainner.yml")
    res = "Profile Saved Successfully"
    message1.configure(text=res)
    message.configure(text='Total Registrations till now  : ' + str(len(ID)))

###############################################################################################

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids

###########################################################################################

def TrackImages():
    check_haarcascadefile()
    assure_path_exists(r"Attendance/")
    assure_path_exists(r"StudentDetails/")
    for k in tv.get_children():
        tv.delete(k)
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # Fixed
    exists3 = os.path.isfile(r"TrainingImageLabel\Trainner.yml")
    if exists3:
        recognizer.read(r"TrainingImageLabel\Trainner.yml")
    else:
        mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
        return
    faceCascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
    exists1 = os.path.isfile(r"StudentDetails\StudentDetails.csv")
    if exists1:
        df = pd.read_csv(r"StudentDetails\StudentDetails.csv")
    else:
        mess._show(title='Details Missing', message='Students details are missing, please check!')
        cam.release()
        cv2.destroyAllWindows()
        window.destroy()
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if conf < 50:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                ID = str(ID)[1:-1]
                bb = str(aa)[2:-2]
                attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]
            else:
                bb = "Unknown"
            cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow('Taking Attendance', im)
        if cv2.waitKey(1) == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
tick            
