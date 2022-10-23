from plyer import notification as nd
from tkinter import *
tkin = Tk()
tkin.title("Notification App") #Title of the applicaiton
tkin.geometry("300x300") #Size of the application

#labels
label1 = Label(tkin, text='Title of the notification').grid(row=0,column=0,)
label2 = Label(tkin, text='Message of the notification').grid(row=1,column=0)
label3 = Label(tkin, text='After how much time notification should display').grid(row=2,column=0)

#entry
e1 = Entry(tkin).grid(row = 0, column=1)
e2 = Entry(tkin).grid(row = 1, column=1)
e3 = Entry(tkin).grid(row = 2, column=1)

#button

button = Button(tkin, text='Stop', width=25,).place(x=0,y=85)


tkin.mainloop() #this will help to run the application in a loop
# tkin.resizable() #this function helps to resize the application





#this gives desktop notification
nd.notify(title='Test', message='Test 123', app_name='12', app_icon='', timeout=10, toast=False,)

print("gel")