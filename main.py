from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import os

height = 0
width = 0

def file_path():
    root = Tk()
    root.withdraw()
    folder = filedialog.askdirectory()

    file_directory.set(folder)

    return folder

def rename():
    user_input = new_name.get()
    new_name.set("")
    global height
    global width

    input_folder = file_directory.get()
    files = os.listdir(input_folder)
    i = counter_input.get()
    # counter_direction.set(1)
    counter_input.set(0)
    
    for index, file in enumerate(files):
        # file_name = os.path.splitext(file)[0]
        file_extension = os.path.splitext(file)[1]

        if file_extension == ".png" or file_extension == ".jpg":
            src = os.path.join(input_folder, file)

            if i < 10:
                if user_input == '':
                    dst = '0000' + str(i) + file_extension
                else:
                    dst = user_input + '_0000' + str(i) + file_extension
            elif i < 100:
                if user_input == '':
                    dst = '000' + str(i) + file_extension
                else:
                    dst = user_input + '_000' + str(i) + file_extension
            elif i < 1000:
                if user_input == '':
                    dst = '00' + str(i) + file_extension
                else:
                    dst = user_input + '_00' + str(i) + file_extension
            else:
                if user_input == '':
                    dst = '0' + str(i) + file_extension
                else:
                    dst = user_input + '_0' + str(i) + file_extension
            
            dst = os.path.join(input_folder, dst)

            os.rename(src, dst)
            if counter_direction.get()==1:
                i += 1
            elif counter_direction.get()==2:
                i -= 1

    messagebox.showinfo("Done", "All files have been successfully renamed!")

if __name__ == '__main__':
    renamer= Tk()
    renamer.geometry("600x500")
    renamer.title("Image File Renamer")
    renamer.configure(background="#075E94")
    renamer.resizable(0,0)

    title = Label(renamer,
                  text="Image Renamer",
                  bg="#075E94",
                  fg="#E0DE16",
                  font=(458)
                  )
    title.pack(pady=50, side=TOP)

    folder_label = Label(renamer,
                         text="Folder path:",
                         bg="#075E94",
                         fg="#E0DE16").place(x=30, y=170)
    file_directory = StringVar()
    file_directory_path = Entry(renamer,
                                textvariable=file_directory,
                                width=60).place(x=150, y=170)
    browse_button = Button(renamer,
                           text="Browse",
                           command=file_path,
                           bg="#1692E0",
                           fg="#E0DE16").place(x=520, y=165)
    
    name_entry_label = Label(renamer, 
                             text="Enter a new name:", 
                             bg="#075E94",
                             fg="#E0DE16").place(x=30, y=200)
    new_name = StringVar()
    new_name_entry = Entry(renamer,
                           textvariable=new_name,
                           width=70).place(x=150, y=200)
    
    number_entry_label = Label(renamer, 
                               text="Enter counter start:", 
                               bg="#075E94",
                               fg="#E0DE16").place(x=30, y=230)
    
    counter_input = IntVar()
    counter_entry = Entry(renamer,
                          textvariable=counter_input,
                          width=5).place(x=150, y=230)

    counter_direction = IntVar()
    list_ascending = Radiobutton(renamer,
                                 text="Ascending",
                                 variable=counter_direction,
                                 value=1,
                                 bg="#075e94",
                                 fg="#E0DE16",
                                 selectcolor="black").place(x=200, y=260)
    list_descending = Radiobutton(renamer,
                                  text="Descending",
                                  variable=counter_direction,
                                  value=2,
                                  bg="#075e94",
                                  fg="#E0DE16",
                                  selectcolor="black").place(x=300, y=260)

    submit_button = Button(renamer,
                           text="Start",
                           command=rename,
                           bg="#1692E0",
                           fg="#E0DE16").place(x=275, y=310)
    
    renamer.mainloop()
