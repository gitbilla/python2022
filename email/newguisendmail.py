# modules
import smtplib
from email.message import EmailMessage
from tkinter import *

#functions

def send():
    # calling values from entry boxes
    subj = subTf.get()
    frm = senTf.get()
    to = recTf.get()
    msg_body = bodyTf.get("1.0","end-1c")
    password = "Ap0l0getics2020"
   
   # Email sending code starts here
    msg = EmailMessage()
    msg['subject'] = subj   
    msg['from'] = frm
    msg['to'] = to
    msg.set_content(msg_body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(frm,password)
        smtp.send_message(msg)
        print("mail Sent")

# gui config
ws = Tk()
ws.title("Pythonguides: Gmail")
ws.geometry("500x400")


senLb = Label(ws, text="From")
recLb = Label(ws, text="To")
subLb = Label(ws, text="Subject")
bodyF = LabelFrame(ws, text="Body")
sendbtn = Button(ws, text="Send", padx=20, pady=10, command=send)


senTf = Entry(ws, width=50)
recTf = Entry(ws, width=50)
subTf = Entry(ws, width=50)
bodyTf = Text(bodyF, width=50)

senLb.place(x=50, y=20, anchor=CENTER)
recLb.place(x=50, y=60, anchor=CENTER)
subLb.place(x=50, y=100, anchor=CENTER)
bodyF.place(x=230, y=230, height=200, width=350, anchor=CENTER)

sendbtn.place(x=230, y=360, anchor=CENTER)

senTf.place(x=250, y=20, anchor=CENTER)
recTf.place(x=250, y=60, anchor=CENTER)
subTf.place(x=250, y=100, anchor=CENTER)
bodyTf.pack()

# infinite loop
ws.mainloop()