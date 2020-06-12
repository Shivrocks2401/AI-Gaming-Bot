from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import os
import subprocess
import sys


def start():
        def pong():
            os.system("cd p-file & python pong.py")



        def snake():
            os.system('cd Game_Files/snake_game_project & python snake.py')


        def open_file(): 
            file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')])
            if file is not None: 
                ph=PhotoImage(file = r"plus.png")
                ph=ph.subsample(20,20)
                add_icono=Button(shiv_root, image = ph, command = lambda:newWindow(file.name))
                add_icono.place(relx=0.5, rely=0.4 , anchor= CENTER)






        shiv_root = Tk() # creating object of Tk class.

        screen_width=626
        screen_height=428
        #title
        shiv_root.title("AI GAMING BOT")
        shiv_root.iconbitmap(r'game_icon.ico')

        #gui logic
        shiv_root.geometry('626x428') #widthxheight
        shiv_root.minsize(screen_width,screen_height) #width,height
        shiv_root.maxsize(screen_width,screen_height) #width,height

        #adding image
        photo1 = Image.open('game.jpg')
        photo1 = ImageTk.PhotoImage(photo1)
        shiv_label= Label(image=photo1)

        #text over centre
        pic= Image.open('c.png')
        pic=pic.resize((626,40))
        pic= ImageTk.PhotoImage(pic)
        page_top_centre= Label(image=pic, bg='black')

        phot=PhotoImage(file = r"snk.png")
        phot=phot.subsample(10,10)
        add_ic=Button(shiv_root, image= phot , command=lambda:snake())
        add_ic.place(relx=0.2, rely=0.4 , anchor= CENTER)

        phot1=PhotoImage(file = r"pong.png")
        phot1=phot1.subsample(10,10)
        add_ic1=Button(shiv_root, image= phot1 , command=lambda:pong())
        add_ic1.place(relx=0.4, rely=0.4 , anchor= CENTER)

        photo2=PhotoImage(file = r"plus.png")
        photo2=photo2.subsample(10,10)
        add_icon=Button(shiv_root, image= photo2 , command=lambda:open_file())
        add_icon.place(relx=0.6, rely=0.4 , anchor= CENTER)








        page_top_centre.pack()
        shiv_label.pack()




        shiv_root.mainloop() 
