print("Hello World")

from tkinter import *
from nltk.chat.util import Chat, reflections

root =Tk()
root.configure(background ="blue")
root.title("Raisoni ChatBot")

def send():
	send="You-> "+e.get();
	txt.insert(END,"\n"+send)

	if(e.get()== 'Hi'):
		txt.insert(END,"\n"+"Bot-> Here")
	else:
		txt.insert(END, "\n"+"Bot->Didn't Get that")




txt=Text(root)
txt.grid(row=0,column=0,columnspan=2) #for increasing text area
e=Entry(root,width=100)

send=Button(root, text="Send", command=send).grid(row=1,column=1)
e.grid(row=1,column=0)

root.mainloop()