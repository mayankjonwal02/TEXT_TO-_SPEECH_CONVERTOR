import tkinter as t
import pyttsx3 as p
e=p.init()
#/e1=p.init()
e.setProperty('rate',140)
voices=e.getProperty('voices')
def a():
    e.setProperty('voice',voices[int(q.get())].id)
    e.say(txt.get("1.0","end"))
    e.runAndWait()

#//e1.setProperty('rate',140)
window=t.Tk()
#//window.border=110
l=t.Label(text="TEXT TO SPEECH",height=5,width=100,bg="black",fg="white")
l.pack()
v=t.Label(text="VOICE KEY",height=3,width=30,bg="grey",fg="black")
v.pack()
q=t.Entry(width=20,border=2)#.grid(row=10,column=0)

q.pack()
#l=t.Label(text="ENTER TEXT",height=3,width=100,bg="black",fg="white")
#l.pack()
txt=t.Text(border=4)
txt.pack()

b=t.Button(text="AUDIO",command=a)
b.pack()




#//e1.setProperty('voice',voices[0].id)



window.mainloop()
    
    
