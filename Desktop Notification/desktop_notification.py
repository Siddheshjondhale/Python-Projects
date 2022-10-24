from plyer import notification as nd
from tkinter import *
import pyautogui
tkin = Tk()
tkin.title("Notification App") #Title of the applicaiton
tkin.geometry("500x500") #Size of the application

#labels
titleLabel = Label(tkin, text='Title of the notification')
titleLabel.grid(row=0,column=0)
messageLabel = Label(tkin, text='Message of the notification')
messageLabel.grid(row=1,column=0)
time = Label(tkin, text='After how much time notification should display')
time.grid(row=2,column=0)



#entryz
titleEntry = Entry(tkin)
titleEntry.grid(row = 0, column=1)
messageEntry = Entry(tkin)
messageEntry.grid(row = 1, column=1)
timeEntry = Entry(tkin)
timeEntry.grid(row = 2, column=1)
# e4 = Entry(Tk()).grid(row = 3, column=1)

#function
def data():
    try:
        title = titleEntry.get()
        message = messageEntry.get()
        Timeout = int(float((timeEntry.get()))) #because we cant put time in decimals it takes only integer value

    except:
        # validation
        if title == "" or message == "" or Timeout == "":
            pyautogui.alert(text='You need to enter all the values', title='Error', button='OK')
            print("THis ran 1")

    nd.notify(title=title, message=message, app_name='notifier', timeout=Timeout, ticker="notification App",toast=True)




#button
button = Button(tkin, text='Submit', width=25,command=data).place(x=0,y=85)






tkin.mainloop()
#this will help to run the application in a loop
tkin.resizable()
#this function helps to resize the application





#this gives desktop notification
nd.notify(title="Test", message='Test 123', app_name='12', app_icon='', timeout=10, toast=False,)

