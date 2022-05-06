#!/usr/bin/env python3

# modules
import smtplib
from email.message import EmailMessage

# content
sender = "augustine.technicals2020@gmail.com"
reciever = "augustine.technicals2020@gmail.com"
password = "Ap0l0getics2020"
msg_body = '''You are invited to Abraham's birthday party!
         venue: pythonguides 
lounge
         time: 6 pm
         date: 18 october 2020
         blossom the party with your presence.
        '''


# action
msg = EmailMessage()
msg['subject'] = 'Invitation to birthday party!'   
msg['from'] = sender
msg['to'] = reciever
msg.set_content(msg_body)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender,password)
    
    smtp.send_message(msg)
    print('Mail Sent')
