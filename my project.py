from tkinter import*
from tkinter.messagebox import*
from tkinter. filedialog import askopenfilename,asksaveasfilename
import os
from threading import Thread

root=Tk()
root.geometry("900x600")
root.minsize(500,300)
root.title("My notepad")


# tKinter icon chnaging
tkinter_icon=PhotoImage(file="C:\\Users\\thete\\OneDrive\\Pictures\\file-file-32.png")
root.iconphoto(False,tkinter_icon)


# Text Area creating!
textarea=Text(root,font="Arial 15",background="#dee3cc")
file=None 
textarea.pack(expand=True,fill=BOTH)
# Text area background colors
# background_color= #7a8ed6   
# background_color= #bfa8f7
# background_color= #ebd2a7
# background_color= #cfe0b1
# background_color= #dee3cc
# background_color= #b1e0ba


# Bottom Lable
l1=Label(textarea,text="This is the notepad made by owes mansuri using tkinter module",padx=250,pady=2,background="white",foreground="Black")
l1.pack(side=BOTTOM,fill=X)



# File menu functions
def New_file():
    global file
    root.title("Untitled - Notepad")
    file=None
    textarea.delete(1.0,END)


def open_file():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("all files","*,*"),("Text documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close


def Save():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text documents")])

        if file=="":
            file==None

        else:
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close

            root.title(os.path.basename(file)+" - Notepad")
    else:
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()



def Save_as():
    textarea.event_generate("<<Save As>>")


def Exit():
    root.destroy()



# Edit menu functions
def Cut():
    textarea.event_generate("<<Cut>>")

def Copy():
    textarea.event_generate("<<Copy>>")

def paste():
    textarea.event_generate("<<Paste>>")


# This is the help function
def help():
    showinfo("Help","I will be help you!")


# File menu images
new=PhotoImage(file="C:\\Users\\thete\\OneDrive\\Pictures\\new_document-1-16.png")
open=PhotoImage(file="C:\\Users\\thete\\OneDrive\\Pictures\\open_folder-4-16.png")
save=PhotoImage(file="C:\\Users\\thete\\OneDrive\\Pictures\\save-32-16.png")
save_as=PhotoImage(file="C:\\Users\\thete\\OneDrive\\Pictures\\save-as-10-16.png")
exit=PhotoImage(file="C:\\Users\\thete\\OneDrive\\Pictures\\exit-42-16.png")


# Edit menu images
cut=PhotoImage(file="C:\\Users\\thete\\OneDrive\\Pictures\\cut-69-16.png")
copy=PhotoImage(file="C:\\Users\\thete\\OneDrive\\Pictures\\copy-95-16.png")
Paste=PhotoImage(file="C:\\Users\\thete\\OneDrive\\Pictures\paste-81-16.png")


# Help menu images
help_menu=PhotoImage(file="C:\\Users\\thete\\OneDrive\\Pictures\\help-108-16.png")


# File menu
main_menu=Menu(root)
file_menu=Menu(main_menu,tearoff=0)
file_menu.add_command(label="New File",image=new,compound=LEFT,accelerator="       Ctr + N",command=New_file)
file_menu.add_command(label="Open File",image=open,compound=LEFT,accelerator="     Ctr + O",font="lucida 10",command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save",image=save,compound=LEFT,accelerator="     Ctr + S",font="lucida 10",command=Save)
file_menu.add_command(label="Save as",image=save_as,compound=LEFT,accelerator="     Ctr + S",font="lucida 10",command=Save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit",image=exit,compound=LEFT,accelerator="     Ctr + Q",font="lucida 10",command=Exit)

root.config(menu=main_menu)
main_menu.add_cascade(label="File",menu=file_menu,font="Lucida 20")



# Edit menu
file_menu1=Menu(main_menu,tearoff=0)
file_menu1.add_command(label=" Cut",image=cut,compound=LEFT,accelerator="    Ctr + X",font="lucida 10",command=Cut)
file_menu1.add_separator()
file_menu1.add_command(label=" Copy",image=copy,compound=LEFT,accelerator="    Ctr + C",font="lucida 10",command=Copy)
file_menu1.add_separator()
file_menu1.add_command(label=" Paste",image=Paste,compound=LEFT,accelerator="    Ctr + V",font="lucida 10",command=paste)
# file_menu1.add_separator()

root.config(menu=main_menu)
main_menu.add_cascade(label="Edit",menu=file_menu1,font="Lucida 20")



# help menubar
Filemenu2=Menu(main_menu,tearoff=0)
Filemenu2.add_command(label="  Help",image=help_menu,compound=LEFT,command=help)
file_menu.add_separator()
root.config(menu=main_menu)
main_menu.add_cascade(label="Help",menu=Filemenu2)



# scrollbar adding in notepad
scroll=Scrollbar(textarea)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)


root.mainloop()