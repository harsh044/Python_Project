# import Packages
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import shutil
import tkinter.messagebox as msg
from tkinter import messagebox as mess
import cv2, os
import csv
import numpy as np
import datetime
import time
import face_recognition
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

################################Start###################################################
# creating File and folder
path = ""
Newfolder = "images"
file = "Attendance.csv"
if not os.path.exists(Newfolder):
    os.makedirs(Newfolder)
else:
    pass
if not os.path.exists(file):
    with open('Attendance.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time"])

# Time function
def tick():
    time_string = time.strftime('%H:%M')
    clock.config(text=time_string)
    clock.after(200, tick)

# About Message Box
def about():
    mess._show(title='About us', message="This Project Is created by: \n (1) Harshad Patil \n (2) Saimohan Sahu \n (3) Saquib \n (4) Heena "
                                         "khan")


# Display Time and Date function
global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day, month, year = date.split("-")

mont = {'01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
        }

# Capture the Photo And save function
def capture():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    img_counter = 0
    save_path = 'Images'
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k % 256 == 8:
            # Press Backspace To Close=8
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # Press Spacebar To capture=32
            name = simpledialog.askstring("Input", "What is your first name?")
            img_name = os.path.join(save_path, name + "_{}.jpg".format(img_counter))
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))

    cam.release()
    cv2.destroyAllWindows()

# Capture the Photo And save function
def send_email():
    emailfrom = "Email-ID"
    emailto = "Email-ID"
    fileToSend = "Attendance.csv"
    username = "email-ID"
    password = "password"

    msg = MIMEMultipart()
    msg["From"] = emailfrom
    msg["To"] = emailto
    msg["Subject"] = "Attendance Sheet"
    msg.preamble = "Attendance Sheet"

    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "text":
        fp = open(fileToSend)
        # Note: we should handle calculating the charset
        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
    msg.attach(attachment)

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username,password)
    server.sendmail(emailfrom, emailto, msg.as_string())
    server.quit()
    print('Email Sent')


# Upload Images function
def TakeImages():
    source = filedialog.askopenfilename()
    # print("Source Adddress"+source.filename)

    destination = 'images'
    dest = shutil.move(source, destination)
    print("Move to " + dest)
    msg.showinfo("Message", "Upload successfully")


# Track Images And Take Attanedance function
def TrackImages():
    path = 'Images'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cls in myList:
        curImg = cv2.imread(f'{path}/{cls}')
        images.append(curImg)
        classNames.append(os.path.splitext(cls)[0])
    print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def markAttendance(name):
        with open('Attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.datetime.now()
                date = datetime.date.today()
                dtString = now.strftime('%H:%M')
                f.writelines(f'\n{name},{date},{dtString}')

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if faceDis[matchIndex] < 0.50:
                name = classNames[matchIndex].upper()
                markAttendance(name)
            else:
                name = 'Unknown'
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow('Webcam', img)
        k=cv2.waitKey(1) & 0xFF
        if k == 27:  # close on ESC key
            cv2.destroyAllWindows()
            break

# GUI Interface
window = tk.Tk()
window.geometry("1235x650+50+30")
window.resizable(False, False)
window.title("Attendance System")
window.configure(background='#262523')
p1 = PhotoImage(file='icon1.png')

# Setting icon of master window
window.iconphoto(False, p1)

frame1 = tk.Frame(window, bg="#00aeff")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#00aeff")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="Face Recognition Based Attendance System", fg="white", bg="#262523", width=55,
                    height=1, font=('times', 29, ' bold '))
message3.place(x=10, y=10)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

frame5 = tk.Frame(frame1, bg="white")
frame5.place(relx=0.06, rely=0.33, relwidth=0.90, relheight=0.60)

datef = tk.Label(frame4, text=day + "-" + mont[month] + "-" + year + "  |  ", fg="orange", bg="#262523", width=80,
                 height=1, font=('times', 15, ' bold '))
datef.pack(fill='both', expand=1)

clock = tk.Label(frame3, fg="orange", bg="#262523", width=55, height=1, font=('times', 15, ' bold '))
clock.pack(fill='both', expand=1)
tick()

head2 = tk.Label(frame2, text="                       For New Registrations                       ", fg="black",
                 bg="#3ece48", font=('times', 17, ' bold '))
head2.grid(row=0, column=0)

head1 = tk.Label(frame1, text="                       For Already Registered                       ", fg="black",
                 bg="#3ece48", font=('times', 17, ' bold '))
head1.place(x=0, y=0)

message1 = tk.Label(frame2, text="*Note:Image name as your name ex.yourname.jpg", bg="#00aeff", fg="black", width=39,
                    height=1, activebackground="yellow", font=('times', 13, ' bold '))
message1.place(x=30, y=150)

imgcap = tk.Label(frame2, text="Press Spacebar to Click Image", bg="#00aeff", fg="black", width=25,
                    height=1, activebackground="yellow", font=('times', 13, ' bold '))
imgcap.place(x=40, y=310)
close = tk.Label(frame2, text="Press Backspace to Close", bg="#00aeff", fg="black", width=25,
                    height=1, activebackground="yellow", font=('times', 13, ' bold '))
close.place(x=20, y=340)


message = tk.Label(frame2, text="OR", bg="#00aeff", fg="black", width=39, height=1, activebackground="yellow",
                   font=('times', 16, ' bold '))
message.place(x=6, y=200)

lbl3 = tk.Label(frame1, text="Attendance", width=20, fg="black", bg="#00aeff", height=1, font=('times', 17, ' bold '))
lbl3.place(x=100, y=115)

# showing Attendance
with open("Attendance.csv", newline="") as file:
    reader = csv.reader(file)

    # r and c tell us where to grid the labels
    r = 0
    for col in reader:
        c = 0
        for row in col:
            # i've added some styling
            label = tk.Label(frame5, width=20, height=2, \
                             text=row, relief=tk.RIDGE)
            # label.place(x=25, y=100)
            label.grid(row=r, column=c)
            # label.pack
            c += 1
        r += 1

menubar = tk.Menu(window, relief='ridge')
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='About Us', command=about)
filemenu.add_command(label='Exit', command=window.destroy)
menubar.add_cascade(label='About', font=('times', 29, ' bold '), menu=filemenu)

trainImg = tk.Button(frame2, text="Upload Image", command=TakeImages, fg="white", bg="blue", width=30, height=1,
                     activebackground="white", font=('times', 15, ' bold '))
trainImg.place(x=50, y=100)

capImg = tk.Button(frame2, text="Capture Images", command=capture, fg="white", bg="blue", width=30, height=1,
                   activebackground="white", font=('times', 15, ' bold '))
capImg.place(x=50, y=250)

se_email = tk.Button(frame2, text="Send Email", command=send_email, fg="white", bg="Green", width=30, height=1,
                   activebackground="white", font=('times', 15, ' bold '))
se_email.place(x=50, y=380)

trackImg = tk.Button(frame1, text="Take Attendance", command=TrackImages, fg="black", bg="yellow", width=35, height=1,
                     activebackground="white", font=('times', 15, ' bold '))
trackImg.place(x=30, y=50)
quitWindow = tk.Button(frame2, text="Quit", command=window.destroy, fg="black", bg="red", width=35, height=1,
                       activebackground="white", font=('times', 15, ' bold '))
quitWindow.place(x=30, y=450)

window.configure(menu=menubar)
window.mainloop()

##################### END ######################################
