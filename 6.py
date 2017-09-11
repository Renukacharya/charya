#!/usr/bin/python3
import smtplib
s = smtplib.SMTP('smtp.gmail.com',587 )
s.starttls()
s.login("charya1418@gmail.com","1418charya")
message ="hello"
s.sendmail("charya1418@gmail.com","charya1418@gmail.com","billgates is coming to meet u soon bro")
s.quit()