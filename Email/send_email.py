import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("praveenkumar.u@3edge.in","Praveen@1996")

def sendMail(email,intVal):
    s.sendmail("praveenkumar@3edge.in",'"'+email+'"',''+str(intVal)+'')
    return {"msg":intVal}

           