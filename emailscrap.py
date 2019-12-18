# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 19:17:00 2019

@author: Devdarshan
"""
import imaplib 
import email
 
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('b117020@iiit-bh.ac.in', 'iiit1234')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.
 
result, data = mail.search(None, "UNSEEN")
 
ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-3:] # get the latest
 
result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
 
raw_email = data[0][1] # here's the body, which is raw text of the whole email
# including headers and alternate payloads
#raw_email = str(raw_email)
text = []
link=[]
raw_email_string = raw_email.decode('utf-8')
email_message = email.message_from_string(raw_email_string)
print(email_message)
for part in email_message.walk():
    if part.get_content_type() == "text/html": 
        body = part.get_payload(decode=True)
        text.append(body.decode('utf-8'))
        print(body.decode('utf-8'))
    
'''
  save_string = str("Dumpgmailemail_"  + ".eml")
  # location on disk
  myfile = open(save_string, 'a')
  myfile.write(body.decode('utf-8'))
  # body is again a byte literal
  myfile.close()
  '''
print(text[0])
from bs4 import BeautifulSoup
cleantext = BeautifulSoup(text[0], "lxml").text
print(cleantext)
import re
link=re.findall(r'(https?://\S+)', text[0])
