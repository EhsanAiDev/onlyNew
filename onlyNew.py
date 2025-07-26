import os 
import shutil
import threading
from customtkinter import *
from tkinter.filedialog import askdirectory

######## functions ########
status = [0,0]
def askMainFolder():
    global main_path
    main_path = askdirectory()
    t2.configure(text=f"main Path: {main_path}")

    status[0] = 1
    if status == [1,1] and main_path != "" :
        submit_button.configure(state="normal")
    else:
        submit_button.configure(state="disabled")


def askDirectionFolder():
    global direction_path

    direction_path = askdirectory()
    t4.configure(text=f"direction Path: {direction_path}")


    status[1] = 1
    if status == [1,1] and direction_path != "":
        submit_button.configure(state="normal")
    else:
        submit_button.configure(state="disabled")



def moveFiles():
    b1.configure(state="disabled")
    b2.configure(state="disabled")
    submit_button.configure(state="disabled")

    window.maxsize(600,350)
    window.minsize(600,350)

    logs.pack(pady=(10,0))
    logs.configure(state='normal')
    logs.delete('0.0', "end")

    def task():
        main_files = os.listdir(main_path)
        direction_files = os.listdir(direction_path)
        files = [file for file in main_files if file not in direction_files]
        x = 0

        for file in files:
            file_path = f"{main_path}/{file}".replace(" " , "\ ")

            x += 1
            logs.insert("end",f"moving {file}...({x}/{len(files)})\n")
            os.system(f"cp -r {file_path} {direction_path}")

        logs.insert("end" , "Done.")
        logs.configure(state='disabled') # set it as read-only
        window.after(0, lambda: [b1.configure(state="normal"), b2.configure(state="normal"), submit_button.configure(state="normal")])

    threading.Thread(target=task).start()

    
######## init ########
set_appearance_mode("Dark")
set_default_color_theme("themes/lavender.json")
window = CTk()
window.maxsize(600,230)
window.minsize(600,230)

window.title("onlyNew")

######## frames ########
frame1 = CTkFrame(window)
frame2 = CTkFrame(window)
frame3 = CTkFrame(window)
frame4 = CTkFrame(window)


######## wigets ########
title = CTkLabel(window,text="onlyNew" , font=("Arial",25,"bold"))
title.pack(pady=5)

t1 = CTkLabel(frame1, text="the folder path that contains files:  ",font=("Arial",16,"bold"),bg_color='gray14')
b1 = CTkButton(frame1, text="Choice", command=askMainFolder, width=60, bg_color="gray14")

t2 = CTkLabel(frame2, text="main Path: ?", font=("Arial", 11, "bold"), height=20, text_color="#707070", bg_color="gray14",wraplength=270)

t3 = CTkLabel(frame3, text="the folder path you want to copy files into:  ",font=("Arial",16,"bold"), bg_color="gray14")
b2 = CTkButton(frame3, text="Choice", command=askDirectionFolder, width=60, bg_color="gray14")

t4 = CTkLabel(frame4, text="direction Path: ?", font=("Arial", 11, "bold"), height=20, text_color="#707070", bg_color="gray14", wraplength=650)

submit_button = CTkButton(window , text="Move New Files", command=moveFiles, font=("Arial", 18, "bold"),state="disabled" ,height=40, width=120)


logs = CTkTextbox(window, width=570, height=120, border_color="#707070", border_width=2)

logs.pack_forget()
######## frames palcing ########
frame1.place(x=7,y=48)
frame2.place(x=7,y=71)
frame3.place(x=7,y=105)
frame4.place(x=7,y=128)


######## packing wigets ########
t1.grid(row=1 , column=1)
b1.grid(row=1 , column=2)

t2.pack()

t3.grid(row=1 , column=1)
b2.grid(row=1 , column=2)

t4.pack()

submit_button.pack(pady=(135, 0))

window.mainloop()