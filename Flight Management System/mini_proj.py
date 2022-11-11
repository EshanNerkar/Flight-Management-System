from tkinter import *
from tkinter import font
from PIL import ImageTk,Image
from tkinter import messagebox
import pymongo
from pymongo import collection

root = Tk()
root.geometry('1250x600')
root['bg'] = "#F8EEEC"
root.iconbitmap("main_pics/new_logo.png")

#functions
#drop_down-language
def drop_down1(str1):
    
    greet= drop1.get()
    l2=messagebox.showinfo(str1 + " selected ","You've selected " + str1)
    l2.grid(row=5,column=3)

#search2
def search_bar():
    
    greetings = e.get()
    l1=messagebox.showinfo("You've searched for " + greetings,"Thanks for searching for " + e.get())
    l1.grid(row=5,column=3)
#drop_down2
def drop_down2(str1):
    greet= drop1.get()
    l2=messagebox.showinfo(str1 + " selected ","You've selected " + str1)
    l2.grid(row=5,column=3)
#img-
def img():
    Label(root,text="hello!").grid(row=3,column=3)

def  open_login():
    top = Toplevel()
    top.geometry('800x800')
    top['bg'] = "#F8EEEC"
    global img_logo1 
    img_logo1 =  ImageTk.PhotoImage(Image.open("main_pics/new_logo.png"))
    img_lab1 = Label(top,image=img_logo1)
    img_lab1.grid(row=0,column=0,pady=25,padx=15)
    lab_head = Label(top,text="LOG IN",fg="BLACK",bg="#F8EEEC",font=("DM Sans",40))
    lab_head.grid(row=0,column=1,columnspan=2)
    lg_name=Entry(top,font=("DM Sans",15),text = name1)
    lg_name.insert(0,"Name:")
    lg_name.grid(row=2,column=0,padx=15,pady=30,ipadx=30,ipady=8)
    lg_age=Entry(top,font=("DM Sans",15),text = age_)
    lg_age.insert(0,"Age:")
    lg_age.grid(row=2,column=1,padx=15,pady=30,ipadx=30,ipady=8)
    lg_address=Entry(top,font=("DM Sans",15),text = address_)
    lg_address.insert(0,"Address:")
    lg_address.grid(row=3,column=0,padx=15,pady=30,ipadx=30,ipady=8)
    lg_email=Entry(top,font=("DM Sans",15),text = email_)
    lg_email.insert(0,"Email:")
    lg_email.grid(row=3,column=1,padx=15,pady=30,ipadx=30,ipady=8)
    lg_contact=Entry(top,font=("DM Sans",15),text = contact_)
    lg_contact.insert(0,"Contact:")
    lg_contact.grid(row=4,column=0,padx=15,pady=30,ipadx=30,ipady=8)
    lg_sex=Entry(top,font=("DM Sans",15),text = sex_)
    lg_sex.insert(0,"Sex:")
    lg_sex.grid(row=4,column=1,padx=15,pady=30,ipadx=30,ipady=8)
    login = Button(top,text=" LOGIN ",font=("DM Sans",15),command=sub).grid(row=5,column=0)

name1 = StringVar()
age_ = StringVar()
contact_ = StringVar()
address_ = StringVar()
email_ = StringVar()
sex_ = StringVar()

def  open_search():
    top1 = Toplevel()
    top1.geometry('800x800')
    top1['bg'] = "#F8EEEC"
    global img_logo1 
    img_logo1 =  ImageTk.PhotoImage(Image.open("main_pics/new_logo.png"))
    img_lab1 = Label(top1,image=img_logo1)
    img_lab1.grid(row=0,column=0,pady=25,padx=15)
    lab_head = Label(top1,text="Search Flight",fg="BLACK",bg="#F8EEEC",font=("DM Sans",40))
    lab_head.grid(row=0,column=1,columnspan=2)
    e1=Entry(top1,font=("DM Sans",15),text = srch1)
    e1.insert(0,"Enter flight number:")
    e1.grid(row=2,column=0,padx=15,pady=30,ipadx=30,ipady=8)
    b_search = Button(top1,text=" SEARCH ",font=("DM Sans",15),command=srch).grid(row=2,column=1)

    

def sub():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["gui"]
    collection = db["user_list"]
    dic = {"name":name1.get(),
           "age_":age_.get(),
           "address":address_.get(), 
           "email":email_.get(),
           "contact":contact_.get(),
           "sex":sex_.get(),      
    }
    collection.insert_one(dic)
    greetings = e.get()
    l1=messagebox.showinfo("Entry Added!" + greetings,"Entry added to database : " + e.get()+" added! ")
    l1.grid(row=5,column=3)

srch1 = StringVar()
def srch():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["gui"]
    collection = db["flights"]
    cl1 = collection.find({"flight_no": srch1.get()})
    if{'cl1': {'$exists': True}}:
        l1=messagebox.showinfo("Entry found" ,"Entry : " + srch1.get()+" found! ")
        l1.grid(row=5,column=3)
    
    else:
        l1=messagebox.showinfo("NOT FOUND" ,"Entry Not found! " )
        l1.grid(row=5,column=3)

cust_nam1 = StringVar()    
dep_= StringVar()
arr_ = StringVar()
depd_ = StringVar()
arrd__ = StringVar()
dur_ = StringVar()

def  open_book():
         top2 = Toplevel()
         top2.geometry('800x800')
         top2['bg'] = "#F8EEEC"
         global img_logo1 
         img_logo1 =  ImageTk.PhotoImage(Image.open("main_pics/new_logo.png"))
         img_lab1 = Label(top2,image=img_logo1)
         img_lab1.grid(row=0,column=0,pady=25,padx=15)
         lab_head = Label(top2,text="Flight Booking",fg="BLACK",bg="#F8EEEC",font=("DM Sans",40))
         lab_head.grid(row=0,column=1,columnspan=2)
         r = StringVar()
         r1 = Radiobutton(top2,text="One Way Trip",variable=r,value=1)
         r1.grid(row=1,column=0)
         r2 = Radiobutton(top2,text="Round Trip",variable=r,value=2)
         r2.grid(row=1,column=1)
         r3 = Radiobutton(top2,text="Multi City",variable=r,value=3)
         r3.grid(row=1,column=2)
         cust_nam=Entry(top2,font=("DM Sans",15),text = cust_nam1)
         cust_nam.insert(0,"Customer Full Name:")
         cust_nam.grid(row=2,column=0,padx=15,pady=30,ipadx=40,ipady=8)
         bk_from=Entry(top2,font=("DM Sans",15),text = dep_)
         bk_from.insert(0,"Departure From:")
         bk_from.grid(row=2,column=1,padx=15,pady=30,ipadx=40,ipady=8)
         bk_to=Entry(top2,font=("DM Sans",15),text = arr_)
         bk_to.insert(0,"Arrival To:")
         bk_to.grid(row=3,column=0,padx=15,pady=30,ipadx=40,ipady=8)
         bk_dep_dat=Entry(top2,font=("DM Sans",15),text = depd_)
         bk_dep_dat.insert(0,"Departure At:")
         bk_dep_dat.grid(row=3,column=1,padx=15,pady=30,ipadx=40,ipady=8)
         bk_arr_dat=Entry(top2,font=("DM Sans",15),text = arrd__)
         bk_arr_dat.insert(0,"Arrival At:")
         bk_arr_dat.grid(row=4,column=0,padx=15,pady=30,ipadx=40,ipady=8)
         bk_dur=Entry(top2,font=("DM Sans",15),text = dur_)
         bk_dur.insert(0,"Duration:")
         bk_dur.grid(row=4,column=1,padx=15,pady=30,ipadx=40,ipady=8)
         book = Button(top2,text=" Confirm Booking ",font=("DM Sans",15),command=bk).grid(row=5,column=0)

def bk():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["gui"]
    collection = db["bookings"]
    dic = {"cus_nam":cust_nam1.get(),
        "from":dep_.get(),
           "to:":arr_.get(),
           "dep_at_time":depd_.get(), 
           "arr_at_time":arrd__.get(),
           "duration":dur_.get(),      
    }
    collection.insert_one(dic)
    greetings = e.get()
    l1=messagebox.showinfo("Entry Added!" + greetings,"Booking for " + cust_nam1.get()+" confirmed! ")
    l1.grid(row=5,column=3)

         
         


frame1 = LabelFrame(root,padx=100).grid(row=0,column=0)
img_logo = ImageTk.PhotoImage(Image.open("main_pics/new_logo.png"))
img_lab1 = Label(frame1,image=img_logo)
img_lab1.grid(row=0,column=0,pady=15,padx=15)



#heading
lab_head = Label(frame1,text="AIRBOOK",fg="black",bg="#F8EEEC",font=("DM Sans",40))
lab_head.grid(row=0,column=1,columnspan=2)

#language
languages = ["ENGLISH","HINDI","MARATHI","GERMAN","SPANISH","FRENCH"]
drop1 = StringVar()
drop1.set("SELECT LANGUAGE")
dr1 = OptionMenu(frame1,drop1,*languages,command=drop_down1)
dr1.config(bg="#F5FEFD",fg="black")
dr1.grid(row=1,column=3,padx=10)

#search
e=Entry(root,font=("DM Sans",15),text = srch1)


#imagesforbuttons
img1 = ImageTk.PhotoImage(Image.open("main_pics/2.png"))
img2 = ImageTk.PhotoImage(Image.open("main_pics/3.png"))
img3 = ImageTk.PhotoImage(Image.open("main_pics/4.png"))
img4 = ImageTk.PhotoImage(Image.open("main_pics/5.png"))
img5 = ImageTk.PhotoImage(Image.open("main_pics/6.png"))
img6 = ImageTk.PhotoImage(Image.open("main_pics/7.png"))
img7 = ImageTk.PhotoImage(Image.open("main_pics/8.png"))
img8 = ImageTk.PhotoImage(Image.open("main_pics/9.png"))
img9 = ImageTk.PhotoImage(Image.open("main_pics/10.png"))


#buttons
bt1 = Button(root,text="LOG IN",image=img1,compound="top",command=open_login,bg="#247676",border=5,fg="white").grid(row=3,column=0,ipadx=70,ipady=20,padx=30,pady=10,)
bt2 = Button(root,text=" SEARCH FLIGHTS ",command=open_search,image=img2,compound="top",bg="#247676",border=5,fg="white").grid(row=3,column=1,ipadx=75,ipady=10,padx=30,pady=10,)
bt3 = Button(root,text="FLIGHT BOOKING",command=open_book,image=img3,compound="top",bg="#247676",border=5,fg="white").grid(row=3,column=2,ipadx=80,ipady=10,padx=50,pady=10,)



root.mainloop()