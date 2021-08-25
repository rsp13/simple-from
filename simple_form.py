from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import Image,ImageTk
from tkinter import ttk
import re
page=Tk()
email=[]
password=[]

def sign_up(event):
    def check_nm(event):
        '''name checking'''
        key1 = nm.get()
        if key1.isalpha():
            return True
        else:
            nm.config(text='please valid name')
            return False

    def check_pd(event):
        '''Password checking function'''
        key2 = pwd.get()
        if len(key2) in range(0,8):
            if key2[0].isalpha() and key2[0].isupper():
                d = 0
                sp = 0
                for k in range(1, len(key2)):
                    if key2[k].isdigit():
                        d += 1
                    elif not key2[k].isalpha():
                        if not key2[k].isspace():
                            sp += 1
                        if d >= 1 and sp <= 1:
                            return True
                        else:
                            e2.config(text='Password must have special charcter')
                            return False
                    else:
                        e2.config(text='Password must have atleast one digit')
                        return False
            else:
                e2.config(text='Password first position is upper alphabet')
                return False
        else:
            e2.config(text='password not in range')
            return False

    def check_eml(event):
        '''Email checking function'''
        key3 = eml.get()
        s1, s2 = 0, 0
        for ch in key3:
            if ch == '@':
                s1 += 1
            elif ch == '.':
                s2 += 1
        if s1 == 1 and s2 <= 2:
            e3.config(text='')
            return True
        else:
            e3.config(text='please enter correct e-mail id')
            return False

    def check_mno(event):
        '''mobile_no checking function'''
        key4 = mno.get()
        if not key4.isdigit():
            e4.config(text='mobile number range is 1 to 10')
            return False
        elif len(key4) not in range(0,10):
            e4.config(text='please enter digit')
            return False
        else:
            e4.config(text='')
            return True

    def new_user(event):
        em = eml.get()
        if em not in email:
            email.append(em)
            p = pd.get()
            if p not in password:
                password.append(p)
                new_window.destroy()
            else:
                messagebox.showerror('Error', 'User already have..!!')
        else:
            messagebox.showerror('Error', 'Password already use')

    new_window=Toplevel(page)
    new_window.geometry('500x500')
    new_window.title('Sign_up')
    ig = Image.open(r'H:\python_project\flower.jpg')
    img2 = ImageTk.PhotoImage(ig)
    fm1 = Frame(new_window, bg='blue')
    fm1.pack(side=TOP, fill=X)
    Label(new_window, image=img2).place(x=0, y=0)
    Label(new_window, text='For new user,please fill the form', font='bold 24', height=5, width=500, bg='Purple', fg='white').pack(side=TOP)
    Label(new_window, text='Name', height=2, width=15, bg='Purple', fg='white', font='bold 16').place(x=350, y=250)
    nm = Entry(new_window, width=20, bd=10, fg='black', font='bold 16')
    nm.place(x=700, y=250)
    nm.bind('<KeyPress>', check_nm)
    e1 = Label(new_window, text='', font='bold 16', fg='red')
    e1.place(x=1000, y=250)
    Label(new_window, text='Password', height=2, width=15, bg='Purple', fg='white', font='bold 16').place(x=350, y=350)
    pd = Entry(new_window, width=20, bd=10, fg='black', font='bold 16')
    pd.place(x=700, y=350)
    pd.bind('<FocusOut>', check_pd)
    e2 = Label(new_window, text='', font='bold 16', fg='red')
    e2.place(x=1000, y=350)
    Label(new_window,text='E-mail',height=2,width=15,bg='purple',fg='white',font='bold 16').place(x=350,y=450)
    eml=Entry(new_window,width=20,bd=10,fg='black',font='bold 16')
    eml.place(x=700,y=450)
    e3=Label(new_window,text='',font='bold 16',fg='red')
    e3.place(x=1000,y=450)
    eml.bind('<FocusOut>',check_eml)
    Label(new_window,text='Mobile no.',height=2,width=15,bg='purple',fg='white',font='bold 16').place(x=350,y=550)
    mno=Entry(new_window,width=20,bd=10,fg='black',font='bold 16')
    mno.place(x=700,y=550)
    e4=Label(new_window,text='',font='bold 16',fg='red')
    e4.place(x=1000,y=550)
    mno.bind('<KeyPress>',check_mno)
    Label(new_window,text='City',height=2,width=15,bg='purple',fg='white',font='bold 16').place(x=350,y=650)
    c=StringVar()
    city=ttk.Combobox(new_window,width=15,justify='center',font='bold 16',textvariable=c)
    city.place(x=700,y=650)
    city['values']=('Mumbai','Pune','Nagpur','Nashik','Navi-Mumbai')
    city.current(0)
    city.bind('<Button-1>')
    submit=Button(new_window,text='Submit',height=2,width=15,relief=GROOVE,command=new_user,font='bold 16',fg='white',bg='purple')
    submit.place(x=500,y=750)
    submit.bind('<Button-1>',new_user)
    new_window.mainloop()

def check_mail(event):
    '''Email checking function'''
    key3 = mail.get()
    s1, s2 = 0, 0
    for ch in key3:
        if ch == '@':
            s1 += 1
        elif ch == '.':
            s2 += 1
    if s1 == 1 and s2 <= 2:
        error1.config(text='')
        return True
    else:
        error1.config(text='please enter correct e-mail id')
        return False

#For login Password
def check_pwd(event):
    '''Password checking login function'''
    key2=pwd.get()
    if len(key2)in range(1,8):
        if key2[0].isalpha() and key2[0].isupper():
            d=0
            sp=0
            for k in range(1,len(key2)):
                if key2[k].isdigit():
                    d+=1
                elif not key2[k].isalpha():
                    if not key2[k].isspace():
                        sp+=1
                    if d>=1 and sp<=1:
                        return True
                    else:
                        error2.config(text='Password must have special charcter')
                        return False
                else:
                    error2.config(text='Password must have atleast one digit')
                    return False
        else:
            error2.config(text='Password first position is upper alphabet')
            return False
    else:
        error2.config(text='password not in range')
        return False

def sign_in(event):
    '''sign_in function'''
    global em
    em = mail.get()
    if em in email:
        l = email.index(em)
        p = pwd.get()
        if p == password[l]:
            messagebox.showinfo('yes', 'login success')
            page.quit()
        else:
            messagebox.showinfo('Error','Password is not store..!!')
    else:
        messagebox.showinfo('Error','E-mail Id is not store..!!')

if __name__ == '__main__':
    '''main function'''
    page.geometry('500x500')
    page.title('Login from')
    img=Image.open(r'H:\python_project\flower.jpg')
    img1=ImageTk.PhotoImage(img)
    f1=Frame(page,bg='blue')
    Label(page,image=img1).place(x=0,y=0)
    f1.pack(side=TOP,fill=X)
    Label(page,text='Hello there,Welcome back',font='bold 26',height=5,width=500,bg='Purple',fg='white').pack(side=TOP)


    Label(page,text='E-mail',height=2,width=15,bg='Purple',fg='white',font='bold 16').place(x=350,y=250)
    mail=Entry(page,width=20,bd=10,fg='black',font='bold 16')
    mail.place(x=700,y=250)
    error1=Label(page,text='',font='bold 16',fg='red')
    mail.bind('<FocusOut>',check_mail)
    error1.place(x=1000,y=250)

    Label(page,text='Password',height=2,width=15,bg='Purple',fg='white',font='bold 16').place(x=350,y=350)
    pwd=Entry(page,show='*',width=20,bd=10,fg='black',font='bold 16')
    pwd.place(x=700,y=350)
    pwd.bind('<FocusOut>',check_pwd)
    error2=Label(page,text='',font='bold 16',fg='red')
    error2.place(x=1000,y=350)

    btn1=Button(page,text='Forgot your password',font='bold 16 underline',bg='purple',fg='white',width=25)
    btn1.place(x=500,y=450)
    btn1.bind('<Button-1>')

    btn2=Button(page,text='Sign In',font='bold 16',bg='purple',fg='white',height=2,width=10,relief=RIDGE)
    btn2.place(x=590,y=540)
    btn2.bind('<Button-1>',sign_in)

    new=Button(page,text='New here ? SignUp',bg='purple',font='bold 16 underline',fg='white',height=1,width=25)
    new.place(x=500,y=650)
    new.bind('<Button-1>',sign_up)
    page.mainloop()
print(email)
print(password)