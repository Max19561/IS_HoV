from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import PIL
import os
from tkinter.messagebox import showerror, showwarning, showinfo
win = Tk()
win.state("zoomed")
win.minsize(900,600)
x=win.winfo_width()
y=win.winfo_height()

#defs
def news_open():
    frame_news.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
    frame_reg.place_forget()
    frame_auth.place_forget()
    frame_shop.place_forget()
    frame_lib.place_forget()
    frame_frens.place_forget()
    frame_lk.place_forget()
def shop_open():
    frame_shop.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
    frame_reg.place_forget()
    frame_auth.place_forget()
    frame_news.place_forget()
    frame_lib.place_forget()
    frame_frens.place_forget()
    frame_lk.place_forget()
def lib_open():
    frame_lib.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
    frame_reg.place_forget()
    frame_auth.place_forget()
    frame_news.place_forget()
    frame_shop.place_forget()
    frame_frens.place_forget()
    frame_lk.place_forget()
def lk_open(event):
    if enter==True:
        frame_lk.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
        frame_reg.place_forget()
        frame_auth.place_forget()
        frame_news.place_forget()
        frame_shop.place_forget()
        frame_frens.place_forget()
        frame_lib.place_forget()
    elif enter==False:
        frame_auth.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
        frame_reg.place_forget()
        frame_lk.place_forget()
        frame_news.place_forget()
        frame_shop.place_forget()
        frame_frens.place_forget()
        frame_lib.place_forget()
def frens_open():
    frame_frens.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
    frame_reg.place_forget()
    frame_auth.place_forget()
    frame_news.place_forget()
    frame_lib.place_forget()
    frame_shop.place_forget()
    frame_lk.place_forget()
def auth_open(event):
    frame_auth.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
    frame_reg.place_forget()
    frame_frens.place_forget()
    frame_news.place_forget()
    frame_lib.place_forget()
    frame_shop.place_forget()
    frame_lk.place_forget()
def reg_open(event):
    frame_reg.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
    frame_frens.place_forget()
    frame_auth.place_forget()
    frame_news.place_forget()
    frame_lib.place_forget()
    frame_shop.place_forget()
    frame_lk.place_forget()
def clear_entry(event, entry,pht):
    if entry.get()==pht:
        entry.delete(0, END)
def add_entry(event, entry,pht):
    if entry.get()=='':
        entry.insert(0,pht)
def registration():
    login=input_reg_login.get()
    password=input_reg_password.get()
    for i in range (len(login_arr)):
        if any(login in sublist for sublist in login_arr)==True:
            showwarning('Error','Данный пользователь уже зарегистрирован')
            break
        elif login=='Логин':
            showwarning('Error','Данные введены некорректно')
            break
        else:
            login_arr.append([login,password])
            global enter
            enter=True
            showinfo('Succes',f'Пользователь {login} успешно зарегистророван')
            print(enter,login_arr)
            break

def authorization():
    i=0
    for i in range (len(login_arr)):
        print(login_arr[i][0])
        i+=1

def prepare_mask(size, LANCZOS):
    mask = Image.new('L', (size[0] * LANCZOS, size[1] * LANCZOS), 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + mask.size, fill=255)
    return mask.resize(size, Image.LANCZOS)

def crop(im, s):
    w, h = im.size
    k = w / s[0] - h / s[1]
    if k > 0: im = im.crop(((w - h) / 2, 0, (w + h) / 2, h))
    elif k < 0: im = im.crop((0, (h - w) / 2, w, (h + w) / 2))
    return im.resize(s, Image.LANCZOS)

#arrays and global variables
enter=False
login_arr=[['admin','12345678']]

#frames header
frame_head=Frame()
frame_head.configure(bg="#04396C")
frame_head.place(relwidth=1,relheight=0.08)

frame_upmenu=Frame(frame_head)
frame_upmenu.configure(bg="#04396C")
frame_upmenu.place(rely=0.08,relwidth=0.8,relheight=1)
news_icon=ImageTk.PhotoImage(Image.open("assets/news.png"))
shop_icon=ImageTk.PhotoImage(Image.open("assets/shop.png"))
lib_icon=ImageTk.PhotoImage(Image.open("assets/lib.png"))
fren_icon=ImageTk.PhotoImage(Image.open("assets/fren.png"))
label_news=Button(frame_upmenu,font=("Arial",14),text="Новости",image=news_icon,compound="left",bg="#0060BE",foreground="#C1C6CB", command=news_open)
label_news.place(relx=0.25)
label_shop=Button(frame_upmenu,font=("Arial",14),text="Магазин",image=shop_icon,compound="left",bg="#0060BE",foreground="#C1C6CB", command=shop_open)
label_shop.place(relx=0.42)
label_lib=Button(frame_upmenu,font=("Arial",14),text="Библиотека",image=lib_icon,compound="left",bg="#0060BE",foreground="#C1C6CB", command=lib_open)
label_lib.place(relx=0.58)
label_fren=Button(frame_upmenu,font=("Arial",14),text="Друзья",image=fren_icon,compound="left",bg="#0060BE",foreground="#C1C6CB", command=frens_open)
label_fren.place(relx=0.78)

#menu frames
frame_menu=Frame()
frame_menu.configure(bg="#0060BE")
frame_menu.place(relwidth=0.2,relheight=1)

logo=Image.open("assets/logo.png")
logo=logo.resize((500,80),Image.Resampling.LANCZOS)
logo=ImageTk.PhotoImage(logo)
label=Label(frame_menu,image=logo)
label.place(relwidth=1,relheight=0.08)
label.configure(bg="#04396C")

frame_urgames=Frame(frame_menu)
frame_urgames.configure(bg="#0060BE")
frame_urgames.place(rely=0.08,relwidth=1,relheight=0.3)
game_icon=ImageTk.PhotoImage(Image.open("assets/game.png"))
label_games=Label(frame_urgames,font=("Arial",16),text="Ваши игры",image=game_icon,compound="left",bg="#0060BE",foreground="#C1C6CB")
label_games.place(rely=0.01)
label_game1=Label(frame_urgames,font=("Arial",14),text="Игра 1",image=game_icon,compound="left",bg="#0060BE",foreground="#679ED2")
label_game1.place(rely=0.25,relx=0.1)
label_game2=Label(frame_urgames,font=("Arial",14),text="Игра 2",image=game_icon,compound="left",bg="#0060BE",foreground="#679ED2")
label_game2.place(rely=0.49,relx=0.1)
label_game3=Label(frame_urgames,font=("Arial",14),text="Игра 3",image=game_icon,compound="left",bg="#0060BE",foreground="#679ED2")
label_game3.place(rely=0.73,relx=0.1)

frame_conf=Frame(frame_menu)
frame_conf.configure(bg="#0060BE")
frame_conf.place(rely=0.7,relwidth=1,relheight=0.3)
down_icon=ImageTk.PhotoImage(Image.open("assets/download.png"))
settings_icon=ImageTk.PhotoImage(Image.open("assets/settings.png"))
prof_icon=ImageTk.PhotoImage(Image.open("assets/user.png"))
label_down=Label(frame_conf,font=("Arial",16),text="Загрузки",image=down_icon,compound="left",bg="#0060BE",foreground="#C1C6CB")
label_down.place(rely=0.01)
label_settings=Label(frame_conf,font=("Arial",16),text="Настройки",image=settings_icon,compound="left",bg="#0060BE",foreground="#C1C6CB")
label_settings.place(rely=0.30)
label_prof=Label(frame_conf,font=("Arial",16),text="Имя аккаунта",image=prof_icon,compound="left",bg="#0060BE",foreground="#C1C6CB")
label_prof.place(rely=0.59)

#frames pages
frame_reg=Frame()
frame_reg.configure(bg="#3B89D2")
frame_reg.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)

frame_auth=Frame()
frame_auth.configure(bg="#3B89D2")
frame_auth.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
frame_auth.place_forget()

frame_news=Frame()
frame_news.configure(bg="#3B89D2")
frame_news.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
frame_news.place_forget()

frame_shop=Frame()
frame_shop.configure(bg="#3B89D2")
frame_shop.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
frame_shop.place_forget()

frame_lib=Frame()
frame_lib.configure(bg="#3B89D2")
frame_lib.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
frame_lib.place_forget()

frame_frens=Frame()
frame_frens.configure(bg="#3B89D2")
frame_frens.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
frame_frens.place_forget()

frame_lk=Frame()
frame_lk.configure(bg="#3B89D2")
frame_lk.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
frame_lk.place_forget()

#frames footer
frame_foot=Frame()
frame_foot.configure(bg="#2B73B8")
frame_foot.place(relx=0.2,rely=0.92,relwidth=0.8,relheight=0.08)

#for frame_reg
label_reg_header=Label(frame_reg,anchor='center',text="Регистрация",bg='#3B89D2',fg='#00CCFF',font='a 24')
label_reg_header.place(relwidth=1,relheight=0.05,rely=0.1)

input_reg_email=Entry(frame_reg, foreground="grey")
input_reg_email.place(relx=0.2, rely=0.2,relwidth=0.6,relheight=0.035)
input_reg_email.insert(0, "Электронная почта")

input_reg_login=Entry(frame_reg, foreground="grey")
input_reg_login.place(relx=0.2, rely=0.28,relwidth=0.6,relheight=0.035)
input_reg_login.insert(0, "Логин")

input_reg_name=Entry(frame_reg, foreground="grey")
input_reg_name.place(relx=0.2, rely=0.36,relwidth=0.6,relheight=0.035)
input_reg_name.insert(0, "Отображаемое имя пользователя")

input_reg_password=Entry(frame_reg, foreground="grey")
input_reg_password.place(relx=0.2, rely=0.44,relwidth=0.6,relheight=0.035)
input_reg_password.insert(0, "Пароль")

input_reg_rpw=Entry(frame_reg, foreground="grey")
input_reg_rpw.place(relx=0.2, rely=0.52,relwidth=0.6,relheight=0.035)
input_reg_rpw.insert(0, "Повтор пароля")

btn_reg=Button(frame_reg,text='Зарегистрироваться',font='a 12',command=registration)
btn_reg.configure(bg='#DEC585',fg='#2F51DC')
btn_reg.place(relwidth=0.25,relheight=0.05,relx=0.375,rely=0.6)

label_have_acc=Label(frame_reg,anchor='w',text="Уже есть аккаунт? Войти",bg='#3B89D2',fg='#00CCFF',font='a 11')
label_have_acc.place(relwidth=0.25,relheight=0.05,relx=0.375,rely=0.65)

#for frame_auth
label_auth_header=Label(frame_auth,anchor='center',text="Авторизация",bg='#3B89D2',fg='#00CCFF',font='a 24')
label_auth_header.place(relwidth=1,relheight=0.05,rely=0.1)

input_auth_email=Entry(frame_auth, foreground="grey")
input_auth_email.place(relx=0.2, rely=0.2,relwidth=0.6,relheight=0.035)
input_auth_email.insert(0, "Электронная почта или логин")

input_auth_password=Entry(frame_auth, foreground="grey")
input_auth_password.place(relx=0.2, rely=0.28,relwidth=0.6,relheight=0.035)
input_auth_password.insert(0, "Пароль")

btn_auth=Button(frame_auth,text='Войти',font='a 12',command=authorization)
btn_auth.configure(bg='#DEC585',fg='#2F51DC')
btn_auth.place(relwidth=0.25,relheight=0.05,relx=0.375,rely=0.36)

label_havent_acc=Label(frame_auth,anchor='w',text="Ещё нет аккаунта? Создать",bg='#3B89D2',fg='#00CCFF',font='a 11')
label_havent_acc.place(relwidth=0.25,relheight=0.05,relx=0.375,rely=0.41)

#for frame_lk
label_reg_header=Label(frame_lk,anchor='w',text="Личный кабинет",bg='#3B89D2',fg='#C1C6CB',font='a 22')
label_reg_header.place(relwidth=1,relheight=0.05,rely=0.02)

avatar=Image.open('assets/ex.jpg')
avatar=crop(avatar,(150,150))
avatar.putalpha(prepare_mask((150,150), 4))
avatar=ImageTk.PhotoImage(avatar)
label=Label(frame_lk,image=avatar)
label.place(relx=0.04,rely=0.1)
label.configure(bg='#3B89D2')

edit=Image.open('assets/edit.png')
edit=crop(edit,(50,50))
edit.putalpha(prepare_mask((50,50), 4))
edit=ImageTk.PhotoImage(edit)
label1=Label(frame_lk,image=edit)
label1.place(relx=0.5,rely=0.1)
label.configure(bg='#3B89D2')

#binds
label_settings.bind("<Button-1>",reg_open)
label_prof.bind("<Button-1>",lk_open)
input_reg_email.bind("<FocusIn>", lambda event: clear_entry(event, input_reg_email, "Электронная почта"))
input_reg_email.bind("<FocusOut>", lambda event: add_entry(event, input_reg_email, "Электронная почта"))
input_reg_login.bind("<FocusIn>", lambda event: clear_entry(event, input_reg_login, "Логин"))
input_reg_login.bind("<FocusOut>", lambda event: add_entry(event, input_reg_login, "Логин"))
input_reg_name.bind("<FocusIn>", lambda event: clear_entry(event, input_reg_name, "Отображаемое имя пользователя"))
input_reg_name.bind("<FocusOut>", lambda event: add_entry(event, input_reg_name, "Отображаемое имя пользователя"))
input_reg_password.bind("<FocusIn>", lambda event: clear_entry(event, input_reg_password, "Пароль"))
input_reg_password.bind("<FocusOut>", lambda event: add_entry(event, input_reg_password, "Пароль"))
input_reg_rpw.bind("<FocusIn>", lambda event: clear_entry(event, input_reg_rpw, "Повтор пароля"))
input_reg_rpw.bind("<FocusOut>", lambda event: add_entry(event, input_reg_rpw, "Повтор пароля"))
input_auth_email.bind("<FocusIn>", lambda event: clear_entry(event, input_auth_email, "Электронная почта или логин"))
input_auth_email.bind("<FocusOut>", lambda event: add_entry(event, input_auth_email, "Электронная почта или логин"))
input_auth_password.bind("<FocusIn>", lambda event: clear_entry(event, input_auth_password, "Пароль"))
input_auth_password.bind("<FocusOut>", lambda event: add_entry(event, input_auth_password, "Пароль"))
label_have_acc.bind("<Button-1>",auth_open)
label_havent_acc.bind("<Button-1>",reg_open)


win.mainloop()
