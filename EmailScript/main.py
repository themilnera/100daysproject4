import smtplib
from tkinter import *

BG_COLOR = "#ccffff"


    

window = Tk()
window.title("")
window.config(padx=50, pady=50, bg=BG_COLOR)
#label
subject_label = Label(text="Subject", bg=BG_COLOR, font=("Arial", 11))
subject_label.pack()

#subject
subject_text = StringVar()
subj_input = Entry(textvariable=subject_text)
subj_input.pack(pady=(0, 10), ipady=2)

#body
body_input = Text(height=5, padx=3, pady=3)
body_input.pack(pady=(0, 10))






def send_mail(subject, body):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login("amilner32@gmail.com", "nzqserufvzwgsamw")
            to_address = "amilner32@gmail.com"
            connection.sendmail(
                from_addr="amilner32@gmail.com",
                to_addrs="amilner32@gmail.com",
                msg=f"Subject: {subject}\nTo: {to_address}\n\n{body}"
            )
    except Exception as error:
        print(f"An error of type {type(error).__name__} occurred: {error}")
        
def get_fields_and_send():
    subject = subject_text.get()
    body = body_input.get()
    send_mail(subject, body)

button = Button(text="Send", command=get_fields_and_send, bg="blue", fg="white", font=("Arial", 14), padx=3, pady=3, relief="raised", bd=5)
button.pack()
    
window.mainloop()

#I built this into an exe just for fun