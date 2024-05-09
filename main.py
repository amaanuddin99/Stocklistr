import tkinter as tk
import json
from tkinter import messagebox
import time
import pandas as pd
window=tk.Tk()
window.minsize(height=500,width=500)
window.config(bg="black")
pas=""
def view():
     global pas
     with open ("data.json","r") as dt:
      datar=json.load(dt)
      del datar["password"]
      datar=pd.DataFrame(datar).T
       
     pop2=tk.Toplevel(window)
     pop2.grab_set()
     pop2.title("List of stocks to buy")
     pop2.minsize(height=300,width=400)
     pop2.config(bg="#141E46")
     canva=tk.Canvas(pop2,height=500,width=500,bg="#141E46")
     canva.create_text(220,150,text=datar,font=("Arial",18,"bold"),fill="#FFF5E0")
     print(datar)
     
     canva.pack()


     
     
def finale():
    stock=text1.get()
    book=text2.get()
    cmp=text3.get()


    if(len(cmp)==0 or len(book)==0 or len(stock)==0):
           messagebox.showerror(title="EMPTY FIELDS",message="Fill all the fields and try again")
           return
    with open ("data.json","r") as dt:
        final=json.load(dt)
    with open ("data.json","w") as dt:
        
      
        text1.delete("0","end")
        text2.delete("0","end")
        text3.delete("0","end")
       
        final.update({stock:{"current price":cmp,"book value":book}})
        json.dump(final,fp=dt,indent=4)
def newp():
     global pas
     pop1=tk.Toplevel(window)
     pop1.grab_set()
     pop1.title("Set a new password")
     pop1.minsize(height=300,width=400)
     #pop1.config(bg="#")
     def saverr():
          with open("data.json","r") as dt:
               data=json.load(fp=dt)
          with open("data.json","w") as dt:
               data.update({"password":pas})
               json.dump(data,fp=dt,indent=4)
          
     def final():
          global pas
          if(pas==tex1.get() and tex2.get()==tex3.get() and len(tex1.get())>6):
               pas=tex2.get()
               saverr()
               messagebox.showinfo(title="Successful",message="Your password was successfully saved")
               #newpass["text"]="Update Password"
               #newpass["command"]=newp
               

               pop1.destroy()
          elif(pas!=tex1.get()):
               messagebox.showinfo(title="Failed",message="Old password entered is incorrect")
          elif(tex3.get()!=tex2.get()):
             messagebox.showerror(title="Re-enter password",message="Both passwords do not match")
          elif(len(tex1.get())==0 or len(tex2.get())==0):
               messagebox.showinfo(title="Empty fields",message="Fill both the fields and try again")
      
          else:
               messagebox.showerror(title="Too short",message="Try again with a longer password")
     pop1.config(bg="#141E46")
     can=tk.Canvas(pop1,height=80,width=350,bg="#141E46")
     can.grid(row=0,column=0,columnspan=1,padx=100)
     can.create_text(175,39,text="Password reset",font=("Raleway",20,"bold"),fill="#FFF5E0")
     lab1=tk.Label(pop1,text="Old Password :",font=("Raleway",10,"bold"),fg="#FFF5E0")
     lab1.config(highlightthickness=1,bg="#141E46")
     lab1.grid(column=0,row=2,pady=20,sticky="w")
     tex1=tk.Entry(pop1,width=30)
     tex1.grid(column=0,row=2,sticky="w",padx=130)
     tex2=tk.Entry(pop1,width=30)
     tex2.grid(column=0,row=3,sticky="w",padx=130)
     tex3=tk.Entry(pop1,width=30)
     tex3.grid(column=0,row=4,sticky="w",padx=130)

     lab2=tk.Label(pop1,text="New Password :",font=("Raleway",10,"bold"),fg="#FFF5E0")
     lab2.config(highlightthickness=1,bg="#141E46")
     lab2.grid(column=0,row=3,pady=20,sticky="w")
     lab3=tk.Label(pop1,text="Confirm Password :",font=("Raleway",8,"bold"),fg="#FFF5E0")
     lab3.config(highlightthickness=1,bg="#141E46")
     lab3.grid(column=0,row=4,pady=20,sticky="w")
     saver=tk.Button(pop1,text="Save",width=8,bg="#E1F7F5",font=("Raleway",8,"normal"),command=final)
     saver.grid(column=0,row=5,sticky="w",padx=190,)
     
     pop1.mainloop()
def createp():
     global pas
     global newpass
     def saverr():
          with open("data.json","r") as dt:
               data=json.load(fp=dt)
          with open("data.json","w") as dt:
               data.update({"password":pas})
               json.dump(data,fp=dt,indent=4)
     def final():
          global pas
          if(tex1.get()==tex2.get() and len(tex1.get())>6):
               pas=tex1.get()
               saverr()
               messagebox.showinfo(title="Successful",message="Your password was successfully saved")
               newpass["text"]="Update Password"
               newpass["command"]=newp
            
               
               

               newwin.destroy()
               
          elif(tex1.get()!=tex2.get()):
             messagebox.showerror(title="Re-enter password",message="Both passwords do not match")
          elif(len(tex1.get())==0 or len(tex2.get())==0):
               messagebox.showinfo(title="Empty fields",message="Fill both the fields and try again")
      
          else:
               messagebox.showerror(title="Too short",message="Try again with a longer password")
               
     newwin=tk.Toplevel(window)
     newwin.grab_set()
     newwin.minsize(height=300,width=400)
     newwin.title("Create a password")
     newwin.config(bg="#141E46")
     can=tk.Canvas(newwin,height=80,width=350,bg="#141E46")
     can.grid(row=0,column=0,columnspan=1,padx=100)
     can.create_text(175,39,text="Create a Password",font=("Raleway",20,"bold"),fill="#FFF5E0")
     lab1=tk.Label(newwin,text="Create Password :",font=("Raleway",9,"bold"),fg="#FFF5E0")
     lab1.config(highlightthickness=1,bg="#141E46")
     lab1.grid(column=0,row=2,pady=20,sticky="w")
     tex1=tk.Entry(newwin,width=30)
     tex1.grid(column=0,row=2,sticky="w",padx=130)
     lab2=tk.Label(newwin,text="Confirm Password :",font=("Raleway",9,"bold"),fg="#FFF5E0")
     lab2.config(highlightthickness=1,bg="#141E46")
     lab2.grid(column=0,row=3,pady=20,sticky="w")
     tex2=tk.Entry(newwin,width=30)
     tex2.grid(column=0,row=3,sticky="w",padx=130)
     saver=tk.Button(newwin,text="Save",width=8,bg="#E1F7F5",font=("Raleway",8,"normal"),command=final)
     saver.grid(column=0,row=4,sticky="w",padx=190,pady=5,)
     
     
     

     newwin.mainloop()

     
canvas=tk.Canvas(height=150,width=300)
canvas.config(bg="black")
canvas.create_text(150,75,text="STOCK SCREEN",font=("Raleway",20,"bold"),fill="#F0EBE3")
canvas.grid(row=0,column=1,sticky="n",padx=230,pady=20)
label1=tk.Label(text="Stock Name :",fg="#C5FF95",font=("Raleway",20,"bold"))
label1.config(bg="black")
label1.grid(column=1,row=6,sticky="w",padx=10,pady=10)
label2=tk.Label(text="Book Value :",fg="#C5FF95",font=("Raleway",20,"bold"))
label2.config(bg="black")
label2.grid(column=1,row=8,sticky="w",padx=10,pady=10)
label3=tk.Label(text="Current Price :",fg="#C5FF95",font=("Raleway",20,"bold"))
label3.config(bg="black")
label3.grid(column=1,row=10,sticky="w",padx=10,pady=10)
text3=tk.Entry(width=30)
text3.grid(column=1,row=10,sticky="w",padx=220,pady=10)
text3.config(bg="#FFF5E0")

text1=tk.Entry(width=30)
text1.grid(column=1,row=6,sticky="w",padx=220,pady=10)
text1.config(bg="#FFF5E0")
text2=tk.Entry(width=30)
text2.grid(column=1,row=8,sticky="w",padx=220,pady=10)
text2.config(bg="#FFF5E0")
save=tk.Button(text="Save",width=10,bg="#E1F7F5",font=("Raleway",10,"normal"),command=finale)
save.grid(column=1,row=12,pady=20,sticky="w",padx=220,)
#gdata=tk.Button(text="Get Data",font=("Raleway",10,"normal"))
#newpass=tk.Button(text="New password set",font=("Raleway",10,"normal"),bg="#E1F7F5",command=newp)
#newpass.grid(column=3,row=6)
viewst=tk.Button(text="View list of stocks",command=view,font=("Raleway",10,"normal"),bg="#E1F7F5")
viewst.grid(column=3,row=8)
with open ("data.json","r") as dt:
     pas=json.load(fp=dt)["password"]
    
     
if(len(pas)>0):
     
     existing=pas
     newpass=tk.Button(text="Set a new password ",font=("Raleway",10,"normal"),bg="#E1F7F5",command=newp)
     newpass.grid(column=3,row=6)
else:
     newpass=tk.Button(text="Create a password",font=("Raleway",10,"normal"),bg="#E1F7F5",command=createp)
     newpass.grid(column=3,row=6)


window.mainloop()