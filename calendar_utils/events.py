from tkinter import *
from PIL import Image, ImageTk
import time

class Event:
    def __init__(self, title, start_date, event_time, description):
        self.title       = title
        self.start_date  = start_date
        self.event_time  = event_time
        self.description = description


class EventWindow:
    def __init__(self, event):
        self.title       = event.title
        self.start_date  = event.start_date
        self.event_time  = event.event_time
        self.description = event.description

        self.WINDOW = Tk()
        self.WINDOW.title('Google Calendar Event')
        self.WINDOW.minsize(400, 300)

        self.init_components()
        self.init_labels()
        self.add_to_window()

        self.WINDOW.after(3000, lambda: self.WINDOW.destroy())
        mainloop()


    def init_components(self):

        self.clock_image = ImageTk.PhotoImage(
                            Image.open('calendar_utils/images/clock-32x32.png'))


    def init_labels(self):

        self.title_label   = Label(self.WINDOW,
                                    text=self.title,
                                    fg='#4286F6',
                                    font=('Arial', 26),
                                    wraplength=350)

        self.image_label   = Label(self.WINDOW,
                                    image=self.clock_image)

        self.header_label1 = Label(self.WINDOW,
                                    text='Today',
                                    fg='black',
                                    font=('Arial', 16))

        self.header_label2 = Label( self.WINDOW,
                                    text=(self.start_date),
                                    fg='black',
                                    font=('Arial', 16))

        self.time_label    = Label(self.WINDOW,
                                    text=self.event_time,
                                    fg='black',
                                    font=('Arial', 14))

        self.descr_label   = Label(self.WINDOW,
                                    text=self.description,
                                    fg='black',
                                    bg = '#E6E6E6',
                                    font=('Arial', 18),
                                    highlightbackground='#4286F6',
                                    highlightthickness=1,
                                    wraplength=350)

    def add_to_window(self):

        self.title_label.place(x=32, y=16)
        self.image_label.place(x=32, y=108)
        self.header_label1.place(x=76, y=92)
        self.header_label2.place(x=156, y=92)
        self.time_label.place(x=76, y=120)
        self.descr_label.place(x=32, y=180)

