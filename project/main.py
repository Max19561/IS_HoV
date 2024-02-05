from tkinter import *
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
def shop_open():
    frame_shop.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
    frame_reg.place_forget()
    frame_auth.place_forget()
    frame_news.place_forget()
    frame_lib.place_forget()
    frame_frens.place_forget()
def lib_open():
    frame_lib.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
    frame_reg.place_forget()
    frame_auth.place_forget()
    frame_news.place_forget()
    frame_shop.place_forget()
    frame_frens.place_forget()
def frens_open():
    frame_frens.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
    frame_reg.place_forget()
    frame_auth.place_forget()
    frame_news.place_forget()
    frame_lib.place_forget()
    frame_shop.place_forget()
def auth_open():
    frame_auth.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
    frame_reg.place_forget()
    frame_frens.place_forget()
    frame_news.place_forget()
    frame_lib.place_forget()
    frame_shop.place_forget()
def reg_open(event):
    pass
    frame_reg.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
    frame_frens.place_forget()
    frame_auth.place_forget()
    frame_news.place_forget()
    frame_lib.place_forget()
    frame_shop.place_forget()

    
#frames header
frame_head=Frame()
frame_head.configure(bg="#04396C")
frame_head.place(relwidth=1,relheight=0.08)

frame_upmenu=Frame(frame_head)
frame_upmenu.configure(bg="#04396C")
frame_upmenu.place(rely=0.08,relwidth=0.8,relheight=1)
news_icon=PhotoImage(file="assets/news.png")
shop_icon=PhotoImage(file="assets/shop.png")
lib_icon=PhotoImage(file="assets/lib.png")
fren_icon=PhotoImage(file="assets/fren.png")
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

logo=PhotoImage(file="assets/logo.png")
label=Label(frame_menu,image=logo)
label.place(relwidth=1,relheight=0.08)
label.configure(bg="#04396C")

frame_urgames=Frame(frame_menu)
frame_urgames.configure(bg="#0060BE")
frame_urgames.place(rely=0.08,relwidth=1,relheight=0.3)
game_icon=PhotoImage(file="assets/game.png")
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
down_icon=PhotoImage(file="assets/download.png")
settings_icon=PhotoImage(file="assets/user.png")
prof_icon=PhotoImage(file="assets/game.png")
label_down=Label(frame_conf,font=("Arial",16),text="Загрузки",image=down_icon,compound="left",bg="#0060BE",foreground="#C1C6CB")
label_down.place(rely=0.01)
label_settings=Label(frame_conf,font=("Arial",16),text="Настройки",image=settings_icon,compound="left",bg="#0060BE",foreground="#C1C6CB")
label_settings.place(rely=0.30)
label_prof=Label(frame_conf,font=("Arial",16),text="Имя аккаунта",image=prof_icon,compound="left",bg="#0060BE",foreground="#C1C6CB")
label_prof.place(rely=0.59)

#frames footer
frame_foot=Frame()
frame_foot.configure(bg="#2A6CAB")
frame_foot.place(relx=0.2,rely=0.92,relwidth=0.8,relheight=0.08)

#frames pages
frame_reg=Frame()
frame_reg.configure(bg="#3B89D2")
frame_reg.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)

frame_auth=Frame()
frame_auth.configure(bg="red")
frame_auth.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
frame_auth.place_forget()

frame_news=Frame()
frame_news.configure(bg="orange")
frame_news.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
frame_news.place_forget()

frame_shop=Frame()
frame_shop.configure(bg="yellow")
frame_shop.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
frame_shop.place_forget()

frame_lib=Frame()
frame_lib.configure(bg="green")
frame_lib.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
frame_lib.place_forget()

frame_frens=Frame()
frame_frens.configure(bg="blue")
frame_frens.place(relx=0.2,rely=0.08,relwidth=0.8,relheight=0.92)
frame_frens.place_forget()

#binds
label_settings.bind("<Button-1>",reg_open)
label_prof.bind("<Button-1>",reg_open)

win.mainloop()
